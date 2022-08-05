# Copyright 2022 Quartile Limited
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import fields, models


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    industry_id = fields.Many2one(
        related="order_id.partner_id.industry_id",
        string="Industry",
        readonly=True,
        store=True,
    )
