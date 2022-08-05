# Copyright 2022 Quartile Limited
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import fields, models


class AccountInvoiceReport(models.Model):
    _inherit = "account.invoice.report"

    industry_id = fields.Many2one(
        "res.partner.industry", string="Industry", readonly=True
    )

    def _select(self):
        select_str = super()._select()
        select_str += """
            , sub.industry_id AS industry_id
            """
        return select_str

    def _sub_select(self):
        select_str = super()._sub_select()
        select_str += """
            , ail.industry_id AS industry_id
            """
        return select_str

    def _group_by(self):
        _group_by = super()._group_by()
        _group_by += """
            , ail.industry_id
            """
        return _group_by
