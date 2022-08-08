# Copyright 2022 Quartile Limited
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import fields, models


class SaleReport(models.Model):
    _inherit = "sale.report"

    industry_id = fields.Many2one(
        "res.partner.industry", string="Industry", readonly=True
    )

    def _query(self, with_clause="", fields=None, groupby="", from_clause=""):
        if fields is None:
            fields = {}
        fields["industry_id"] = ", partner.industry_id as industry_id"
        groupby += ", partner.industry_id"
        return super(SaleReport, self)._query(with_clause, fields, groupby, from_clause)
