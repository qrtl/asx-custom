# Copyright 2021 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    amount_history_ids = fields.One2many("sale.order.amount.history", "order_id", string="Amount History")

    def _get_history_vals(self, type=False):
        self.ensure_one()
        res = {
            "order_id": self.id,
            "currency_id": self.currency_id.id,
        }
        if type == "add":
            res["history_type"] = "add"
            res["order_count"] = 1
            res["amount"] = self.amount_untaxed
            res["amount_diff"] = self.amount_untaxed
        elif type == "delete":
            res["history_type"] = "delete"
            res["order_count"] = -1
            res["amount_diff"] = -self.amount_untaxed
        elif type == "change":
            res["history_type"] = "change"
            res["amount"] = self.amount_untaxed
        return res

    def write(self, vals):
        for order in self:
            history_obj = self.env["sale.order.amount.history"]
            history_vals = {}
            if order.state in ("draft", "sent") and vals.get("state") in ("sale", "done"):
                history_vals = order._get_history_vals(type="add")
            elif order.state in ("sale", "done") and vals.get("state") == "cancel":
                history_vals = order._get_history_vals(type="delete")
            if history_vals:
                history_obj.create(history_vals)
        res = super().write(vals)
        for order in self:
            if order.state in ("sale", "done"):
                history_rec = history_obj.search(
                    [
                        ("order_id", "=" , order.id),
                        ("history_type", "in" , ("add", "change")),
                    ], order="id desc", limit=1
                )
                last_amount = history_rec.amount if history_rec else 0.0
                amount_diff = order.amount_untaxed - last_amount
                if amount_diff:
                    history_vals = order._get_history_vals(type="change")
                    history_vals["amount_diff"] = amount_diff
                    history_obj.create(history_vals)
        return res
