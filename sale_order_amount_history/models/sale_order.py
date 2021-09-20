# Copyright 2021 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    is_internal = fields.Boolean(
        related="fiscal_position_id.for_group_companies", store=True
    )
    amount_history_ids = fields.One2many(
        "sale.order.amount.history", "order_id", string="Amount History"
    )

    def _get_order_count(self, hist_type, amount_diff):
        """If the amount is zero, the order should not be "counted".
        """
        self.ensure_one()
        if hist_type == "add":
            return 1 if self.amount_untaxed > 0.0 else 0
        if hist_type == "delete":
            return -1 if self.amount_untaxed > 0.0 else 0
        # The following lines are for the history type "change".
        if self.amount_untaxed > 0.0 and self.amount_untaxed == amount_diff:
            # i.e. amount is changed from zero.
            return 1
        elif self.amount_untaxed == 0.0:
            # i.e. amount is changed to zero
            return -1
        return 0

    def _create_history_vals(self, hist_type, amount_diff):
        self.ensure_one()
        vals = {
            "history_type": hist_type,
            "order_id": self.id,
            # We pass the currency here instead of making the field a related field in
            # sale.order.amount.history in case the currency is changed in the sales
            # order after history is logged.
            "currency_id": self.currency_id.id,
            "order_count": self._get_order_count(hist_type, amount_diff),
            "amount": self.amount_untaxed if hist_type in ("add", "change") else 0.0,
            "amount_diff": amount_diff,
        }
        self.env["sale.order.amount.history"].sudo().create(vals)

    def write(self, vals):
        for order in self:
            if order.is_internal:
                continue
            if order.state in ("draft", "sent") and vals.get("state") in (
                "sale",
                "done",
            ):
                order._create_history_vals("add", order.amount_untaxed)
            elif order.state in ("sale", "done") and vals.get("state") == "cancel":
                order._create_history_vals("delete", -order.amount_untaxed)
        res = super().write(vals)
        for order in self:
            if order.is_internal:
                continue
            if order.state in ("sale", "done"):
                history_rec = self.env["sale.order.amount.history"].search(
                    [
                        ("order_id", "=", order.id),
                        ("history_type", "in", ("add", "change")),
                    ],
                    order="id desc",
                    limit=1,
                )
                last_amount = history_rec.amount if history_rec else 0.0
                amount_diff = order.amount_untaxed - last_amount
                if amount_diff:
                    order._create_history_vals("change", amount_diff)
        return res
