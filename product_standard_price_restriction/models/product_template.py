# Copyright 2023 Quartile Limited
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import _, fields, models
from odoo.exceptions import UserError


class ProductTemplate(models.Model):
    _inherit = "product.template"

    standard_price = fields.Float(track_visibility='onchange')
    update_cost = fields.Boolean()

    def write(self, vals):
        if "standard_price" in vals:
            if not vals.get('update_cost', self.update_cost):
                raise UserError(
                    _(
                        "You are about to update the cost. This field is "
                        "auto-calculated by Odoo and is an 'Weighted Average Value' of "
                        "one unit of this product in current inventory. This is "
                        "not the 'Price' or 'Cost' to buy this item -- that is "
                        "set in the 'Purchase' TAB. This value should not be "
                        "modified unless there are very unusual circumstances. "
                        "In such a situation, please set the 'Update Cost' "
                        "field to 'True' and save the record again. Additionally, "
                        "please make sure to write a detailed 'Log' below "
                        "of what you are changing (from what to what) and why."
                    )
                )
        vals['update_cost'] = False
        return super(ProductTemplate, self).write(vals)
