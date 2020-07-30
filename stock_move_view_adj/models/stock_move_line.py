# Copyright 2020 Quartile Limited
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import fields, models


class StockMoveLine(models.Model):
    _inherit = "stock.move.line"

    picking_partner_id = fields.Many2one(
        "res.partner",
        "Transfer Destination Address",
        related="picking_id.partner_id",
        readonly=False,
    )
