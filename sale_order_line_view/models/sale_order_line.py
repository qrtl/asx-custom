# Copyright 2019 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    date_order = fields.Datetime(
        related="order_id.date_order", string="Order Date", readonly=True,
    )
    state = fields.Selection(
        related="order_id.state", string="Status", readonly=True, store=True,
    )
    partner_shipping_id = fields.Many2one(
        related="order_id.partner_shipping_id",
        string="Delivery Address",
        readonly=True,
        store=True,
    )
