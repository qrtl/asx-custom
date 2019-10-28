# Copyright 2019 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields, api


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    delivery_report_desc = fields.Char(
        string='Description (Delivery Report)',
    )
