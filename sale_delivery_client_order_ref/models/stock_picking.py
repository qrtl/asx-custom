# Copyright 2019 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    client_order_ref = fields.Char(
        related='sale_id.client_order_ref',
        string='Customer Reference',
        store=True,
        readonly=True,
    )
