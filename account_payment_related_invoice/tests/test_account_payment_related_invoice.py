# Copyright 2020 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo.tests.common import TransactionCase


class TestAccountPaymentRelatedInvoice(TransactionCase):

    def setUp(self):
        super(TestAccountPaymentRelatedInvoice, self).setUp()
        self.journal_sale = self.env['account.journal'].search([
            ('type', '=', 'sale')
        ], limit=1)
        self.receivable_account = self.env['account.account'].search([
            ('user_type_id.name', '=', 'Receivable')
        ], limit=1)
        self.partner = self.env.ref('base.res_partner_2')
        self.product1 = self.env.ref('product.product_product_8')

    def test01_payment_with_invoice(self):
        invoice_out1 = self.env['account.invoice'].create({
            'number': 'TEST001',
            'journal_id': self.journal_sale.id,
            'partner_id': self.partner.id,
            'type': 'out_invoice',
            'invoice_line_ids': [
                (0, 0, {
                    'quantity': 1.0,
                    'price_unit': 100,
                    'product_id': self.product1.id,
                    'account_id': self.product1.categ_id.property_account_income_categ_id.id,
                    'name': "Test1",
                })
            ]
        })
        invoice_out1.action_invoice_open()
        invoice_out1.pay_and_reconcile(self.env['account.journal'].search(
            [('type', '=', 'bank')], limit=1), 200.0)
        payment = invoice_out1.payment_ids[0]
        self.assertEqual(
            invoice_out1.number,
            payment.related_invoice_number
        )
        invoice_out2 = self.env['account.invoice'].create({
            'number': 'TEST002',
            'journal_id': self.journal_sale.id,
            'partner_id': self.partner.id,
            'type': 'out_invoice',
            'invoice_line_ids': [
                (0, 0, {
                    'quantity': 1.0,
                    'price_unit': 100,
                    'product_id': self.product1.id,
                    'account_id': self.product1.categ_id.property_account_income_categ_id.id,
                    'name': "Test2",
                })
            ]
        })
        invoice_out2.action_invoice_open()
        if invoice_out2.state == 'open':
            invoice_out2.assign_outstanding_credit(payment.move_line_ids.filtered(
                lambda l: not l.reconciled and l.credit > 0).id)
        payment._compute_related_invoice_number()
        self.assertEqual(
            ','.join([invoice_out2.number, invoice_out1.number]),
            payment.related_invoice_number
        )
