# Copyright 2019 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from datetime import datetime

from odoo import api, models


class AccountInvoiceSend(models.TransientModel):
    _inherit = "account.invoice.send"

    @api.multi
    def send_and_print_action(self):
        self.ensure_one()
        super(AccountInvoiceSend, self).send_and_print_action()
        active_ids = self._context.get("active_ids", self.res_id)
        self.env["account.invoice"].browse(active_ids).write(
            {"sent_date": datetime.now()}
        )
