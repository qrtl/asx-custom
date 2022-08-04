# Copyright 2022 Quartile Limited
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import fields, models


class AccountInvoiceReport(models.Model):
    _inherit = 'account.invoice.report'

    industry_id = fields.Many2one('res.partner.industry', string="Industory" ,readonly=True)


    def _select(self):
        select_str = super()._select()
        return '%s, sub.industry_id' % select_str

    def _sub_select(self):
         select_str = super()._sub_select()
         return '%s, ail.industory_id'   % select_str
    
    def _group_by(self):
         group_by_str = super()._group_by()
         return '%s, ail.industory_id'   % group_by_str
