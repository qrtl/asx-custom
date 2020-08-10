# Copyright 2020 Quartile Limited
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import fields, models


class AccountInvoice(models.Model):
    _inherit = "account.invoice"

    enduser_id = fields.Many2one("res.partner", "Enduser")
