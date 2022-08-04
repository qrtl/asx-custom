# Copyright 2022 Quartile Limited
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import fields, models


class AccountInvoice(models.Model):
    _inherit = "account.invoice.line"

    industry_id = fields.Many2one(
    related="invoice_id.partner_id.industry_id", string="Industry", readonly=True,store=True)
