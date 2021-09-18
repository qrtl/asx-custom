# Copyright 2021 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    amount_history_ids = fields.One2many("sale.order.amount.history", "order_id", string="Amount History")
    # company_currency_id = fields.Many2one(related="company_id.currency_id", string="Company Currency", readonly=True)
    # amount_untaxed_company = fields.Monetary(
    #     string="Untaxed Amount in Company Currency",
    #     currency_field="company_currency_id",
    #     store=True,
    #     compute="_compute_amount_untaxed_company"
    # )

    # @api.depends("confirmation_date", "amount_untaxed_company", "currency_id", "company_id")
    # def _compute_amount_untaxed_company(self):
    #     for order in self:
    #         rate_date = fields.Date.to_date(
    #             fields.Datetime.context_timestamp(order, order.confirmation_date)
    #         ) if order.confirmation_date else fields.Date.context_today()
    #         order.amount_untaxed_company = order.currency_id._convert(
    #             order.amount_untaxed, order.company_currency_id, order.company_id, rate_date
    #         )

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
