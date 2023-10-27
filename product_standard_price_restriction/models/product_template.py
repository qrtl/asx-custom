# Copyright 2023 Quartile Limited
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import _, fields, models
from odoo.exceptions import UserError


class ProductTemplate(models.Model):
    _inherit = "product.template"

    standard_price = fields.Float(track_visibility='onchange')
    update_cost = fields.Boolean(
        help="Set this field to True to allow you update the product cost")

    def write(self, vals):
        if "standard_price" in vals:
            if not vals.get('update_cost', self.update_cost):
                raise UserError(_(self.company_id.product_standard_price_warning_msg))
        vals['update_cost'] = False
        return super(ProductTemplate, self).write(vals)
