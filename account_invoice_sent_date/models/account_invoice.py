# Copyright 2019 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields


class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    sent_date = fields.Datetime(
        string='Sent Date',
        readonly=True,
    )
