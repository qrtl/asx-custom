# Copyright 2021 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class SaleOrderAmountHistory(models.Model):
    _name = "sale.order.amount.history"
    _description = "Sales Order Amount History"
    _order = "id desc"

    date = fields.Date(default=fields.Date.context_today)
    order_id = fields.Many2one("sale.order")
    history_type = fields.Selection([("add", "Add"), ("change", "Change"), ("delete", "Delete")])
    order_count = fields.Integer()
    currency_id = fields.Many2one("res.currency")
    company_id = fields.Many2one(related="order_id.company_id", store=True)
    company_currency_id = fields.Many2one(related="company_id.currency_id", store=True)
    amount = fields.Monetary()
    amount_diff = fields.Monetary()
    amount_diff_company = fields.Monetary(currency_field="company_currency_id")
