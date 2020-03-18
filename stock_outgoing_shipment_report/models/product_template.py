# Copyright 2019 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import _, api, fields, models
from odoo.exceptions import ValidationError


class ProductTemplate(models.Model):
    _inherit = "product.template"

    delivery_report_desc = fields.Char(string="Description (Delivery Report)",)

    @api.constrains("delivery_report_desc")
    def _validate_delivery_report_desc(self):
        for rec in self:
            msg = _("%s should be at most %s digit(s).")
            if rec.delivery_report_desc and len(rec.delivery_report_desc) > 40:
                raise ValidationError(msg % (_("Description (Delivery Report)"), "40"))
