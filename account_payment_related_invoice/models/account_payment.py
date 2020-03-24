# Copyright 2020 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class AccountPayment(models.Model):
    _inherit = "account.payment"

    related_invoice_number = fields.Char(
        string="Invoice(s)", compute="_compute_related_invoice_number",
    )

    @api.multi
    def _compute_related_invoice_number(self):
        for payment in self:
            if payment.invoice_ids:
                payment.related_invoice_number = ",".join(
                    payment.invoice_ids.mapped("number")
                )
