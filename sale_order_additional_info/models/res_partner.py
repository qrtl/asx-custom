# Copyright 2019 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    sale_additional_info = fields.Char(
        string="Additional Information",
        help="This field will be proposed to sales order.",
        oldname="additional_info",
        copy=False,
    )
