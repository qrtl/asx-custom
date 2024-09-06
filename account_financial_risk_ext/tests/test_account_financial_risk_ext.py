from odoo.tests.common import SavepointCase


class TestPartnerFinancialRiskExt(SavepointCase):
    @classmethod
    def setUpClass(cls):
        super(TestPartnerFinancialRiskExt, cls).setUpClass()
        type_revenue = cls.env.ref('account.data_account_type_revenue')
        type_receivable = cls.env.ref('account.data_account_type_receivable')
        tax_group_taxes = cls.env.ref('account.tax_group_taxes')
        cls.account_sale = cls.env['account.account'].create({
            'name': 'Sale',
            'code': 'XX_700',
            'user_type_id': type_revenue.id,
            'reconcile': True,
        })
        cls.account_customer = cls.env['account.account'].create({
            'name': 'Customer',
            'code': 'XX_430',
            'user_type_id': type_receivable.id,
            'reconcile': True,
        })
        cls.partner = cls.env['res.partner'].create({
            'name': 'Partner test',
            'customer': True,
            'property_account_receivable_id': cls.account_customer.id,
            'credit_limit': 1000.0,
        })
        cls.journal_sale = cls.env['account.journal'].create({
            'name': 'Test journal for sale',
            'type': 'sale',
            'code': 'TSALE',
            'default_debit_account_id': cls.account_sale.id,
            'default_credit_account_id': cls.account_sale.id,
        })
        cls.tax = cls.env['account.tax'].create({
            'name': 'Tax for sale 10%',
            'type_tax_use': 'sale',
            'tax_group_id': tax_group_taxes.id,
            'amount_type': 'percent',
            'amount': 10.0,
        })
        cls.invoice = cls.env['account.invoice'].create({
            'partner_id': cls.partner.id,
            'account_id': cls.account_customer.id,
            'type': 'out_invoice',
            'journal_id': cls.journal_sale.id,
            'payment_term_id': False,
            'invoice_line_ids': [(0, 0, {
                'name': 'Test product',
                'account_id': cls.account_sale.id,
                'price_unit': 50,
                'quantity': 10,
                'invoice_line_tax_ids': [(6, 0, [cls.tax.id])],
            })],
        })

    def test_partner_credit_balance(self):
        self.partner.risk_invoice_draft_include = True
        self.assertEqual(self.partner.risk_total, 550.0)
        self.assertEqual(self.partner.credit_balance, 450.0)
