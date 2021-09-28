# Copyright 2021 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo.tests import SavepointCase, tagged


@tagged("post_install", "-at_install")
class TestSaleOrder(SavepointCase):
    def _create_order_line(self, order, product):
        order.write(
            {
                "order_line": [
                    (
                        0,
                        0,
                        {
                            "product_id": product.id,
                            "product_uom_qty": 1.0,
                            "price_unit": 100.0,
                        },
                    )
                ],
            }
        )

    def _get_latest_history(self, order):
        return self.env["sale.order.amount.history"].search(
            [("order_id", "=", order.id)], order="id desc", limit=1,
        )

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.history_obj = cls.env["sale.order.amount.history"]
        cls.partner = cls.env.ref("base.res_partner_12")
        cls.product = cls.env["product.product"].create(
            {"name": "test product", "type": "service"}
        )
        cls.order = cls.env["sale.order"].create({"partner_id": cls.partner.id})

    def test_01_order_history(self):
        # Create and confirm a sales order.
        self._create_order_line(self.order, self.product)
        self.assertEqual(len(self.order.amount_history_ids), 0)
        self.order.action_confirm()
        self.assertEqual(len(self.order.amount_history_ids), 1)
        history = self._get_latest_history(self.order)
        self.assertEqual(history.history_type, "add")
        self.assertEqual(history.order_count, 1)
        self.assertEqual(history.amount, 100.0)
        self.assertEqual(history.amount_diff, 100.0)

        # Add a line to the confirmed sales order.
        self._create_order_line(self.order, self.product)
        self.assertEqual(len(self.order.amount_history_ids), 2)
        history = self._get_latest_history(self.order)
        self.assertEqual(history.history_type, "change")
        self.assertEqual(history.order_count, 0)
        self.assertEqual(history.amount, 200.0)
        self.assertEqual(history.amount_diff, 100.0)

        # Cancel the sales order.
        self.order.action_cancel()
        self.assertEqual(len(self.order.amount_history_ids), 3)
        history = self._get_latest_history(self.order)
        self.assertEqual(history.history_type, "delete")
        self.assertEqual(history.order_count, -1)
        self.assertEqual(history.amount, 0.0)
        self.assertEqual(history.amount_diff, -200.0)
