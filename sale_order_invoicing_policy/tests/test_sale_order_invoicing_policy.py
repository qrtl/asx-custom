# Copyright 2023 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo.tests.common import TransactionCase


class TestSaleOrderInvoicingPolicy(TransactionCase):
    def setUp(self):
        super(TestSaleOrderInvoicingPolicy, self).setUp()
        self.partner = self.env.ref("base.res_partner_2")
        self.product1 = self.env["product.product"].create(
            {"name": "Test Product", "type": "consu"}
        )

    def test_sale_order_invoicing_policy_order(self):
        sale_order = self.env["sale.order"].create(
            {
                "partner_id": self.partner.id,
                "invoice_policy": "order",
                "order_line": [
                    (
                        0,
                        0,
                        {
                            "product_id": self.product1.id,
                            "product_uom_qty": 2,
                            "price_unit": 100,
                        },
                    )
                ],
            }
        )
        sale_order.action_confirm()
        self.assertEqual(sale_order.order_line.qty_to_invoice, 2)
    
    def test_sale_order_invoicing_policy_delivery(self):
        sale_order = self.env["sale.order"].create(
            {
                "partner_id": self.partner.id,
                "invoice_policy": "delivery",
                "order_line": [
                    (
                        0,
                        0,
                        {
                            "product_id": self.product1.id,
                            "product_uom_qty": 2,
                            "price_unit": 100,
                        },
                    )
                ],
            }
        )
        sale_order.action_confirm()
        self.assertEqual(sale_order.order_line.qty_to_invoice, 0)
