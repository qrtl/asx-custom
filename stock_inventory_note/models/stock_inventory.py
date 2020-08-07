# Copyright 2020 Quartile Limited
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import fields, models


class Inventory(models.Model):
    _inherit = "stock.inventory"

    note = fields.Text("Notes", copy=False)
