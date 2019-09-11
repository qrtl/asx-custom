# Copyright 2019 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class AccountInvoiceSend(models.TransientModel):
    _name = 'account.invoice.send'
    _inherit = 'account.invoice.send'
    _description = 'Account Invoice Send'

    @api.multi
    def send_and_print_action(self):
        super(AccountInvoiceSend, self).send_and_print_action()
        self.ensure_one()
        active_ids = self.env.context.get('active_ids', self.res_id)
        active_records = self.env[self.model].browse(active_ids)