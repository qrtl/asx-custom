# Copyright 2020 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo.tests.common import TransactionCase


class TestSaleOrder(TransactionCase):
    def setUp(self):
        super(TestSaleOrder, self).setUp()
        self.partner = self.env.ref("base.res_partner_2")
        self.product1 = self.env["product.product"].create(
            {"name": "Test Product", "type": "service"}
        )
        self.enduser = self.env["res.partner"].create({"name": "Test Enduser"})

    def test_prepare_invoice(self):
        # Create the SO with four order lines
        self.sale_order = self.env["sale.order"].create(
            {
                "partner_id": self.partner.id,
                "enduser_id": self.enduser.id,
                "order_line": [
                    (
                        0,
                        0,
                        {
                            "product_id": self.product1.id,
                            "product_uom_qty": 1,
                            "price_unit": 100,
                        },
                    )
                ],
            }
        )
        self.sale_order.action_confirm()

        # Create the invoice
        self.sale_order.action_invoice_create()
        self.invoice = self.sale_order.invoice_ids

        # compare the `enduser_id` field data with invoice Enduser field
        # the values passing through `_prepare_invoice` method to invoice.
        self.assertEqual(
            self.invoice.enduser_id,
            self.enduser,
            "End User field from invoice does not"
            " matching with test records Enduser field",
        )
