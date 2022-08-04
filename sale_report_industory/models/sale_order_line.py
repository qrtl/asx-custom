# Copyright 2019 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    industry_id = fields.Many2one(
    related="order_id.partner_id.industry_id", string="Industry", readonly=True,store=True)
