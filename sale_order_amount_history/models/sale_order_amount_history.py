# Copyright 2021 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class SaleOrderAmountHistory(models.Model):
    _name = "sale.order.amount.history"
    _description = "Sales Order Amount History"
    _order = "id desc"

    date = fields.Date(default=fields.Date.context_today)
    order_id = fields.Many2one("sale.order")
    partner_id = fields.Many2one(related="order_id.partner_id", store=True)
    history_type = fields.Selection(
        [("add", "Add"), ("change", "Change"), ("delete", "Delete")]
    )
    order_count = fields.Integer()
    currency_id = fields.Many2one("res.currency")
    company_id = fields.Many2one(related="order_id.company_id", store=True)
    company_currency_id = fields.Many2one(
        related="company_id.currency_id", string="Company Currency", store=True
    )
    amount = fields.Monetary()
    amount_diff = fields.Monetary()
    amount_company = fields.Monetary(
        string="Amount in Company Currency",
        currency_field="company_currency_id",
        store=True,
        compute="_compute_amount_company",
    )
    amount_diff_company = fields.Monetary(
        string="Amount Diff in Company Currency",
        currency_field="company_currency_id",
        store=True,
        compute="_compute_amount_company",
    )

    @api.depends(
        "order_id",
        "order_id.confirmation_date",
        "amount",
        "amount_diff",
        "currency_id",
        "company_id",
        "company_currency_id",
    )
    def _compute_amount_company(self):
        for rec in self:
            order = rec.order_id
            if not order.confirmation_date:
                continue
            rate_date = fields.Date.to_date(
                fields.Datetime.context_timestamp(rec, order.confirmation_date)
            )
            rec.amount_company = rec.currency_id._convert(
                rec.amount, rec.company_currency_id, rec.company_id, rate_date
            )
            rec.amount_diff_company = rec.currency_id._convert(
                rec.amount_diff, rec.company_currency_id, rec.company_id, rate_date
            )
