# Copyright 2020 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class AccountPayment(models.Model):
    _inherit = "account.payment"

    evidence_status = fields.Selection(
        [("more", "Need More"), ("done", "Done")], string="Evidence Status"
    )
    evidence_text = fields.Char()
