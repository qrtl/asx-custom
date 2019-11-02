# Copyright 2019 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields


class StockWarehouse(models.Model):
    _inherit = 'stock.warehouse'

    user_ids = fields.Many2many(
        'res.users', string='3PL Users',
        help="Set 3PL users who should be able to see picking records of "
        "this warehouse.")
