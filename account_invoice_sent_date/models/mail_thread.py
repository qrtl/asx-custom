# Copyright 2019 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from datetime import datetime

from odoo import api, models


class MailThread(models.AbstractModel):
    _inherit = "mail.thread"

    # this method is used when an invoice is created by payment via portal.
    @api.multi
    def message_post_with_template(self, template_id, **kwargs):
        res = super(MailThread, self).message_post_with_template(template_id, **kwargs)
        if self._name == "account.invoice" and template_id:
            self.write({"sent_date": datetime.now()})
        return res
