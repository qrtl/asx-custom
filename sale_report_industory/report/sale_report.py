

from odoo import fields, models


class SaleReport(models.Model):
    _inherit = 'sale.report'

    industry_id = fields.Many2one('res.partner.industry', string="Industory" ,readonly=True)

    def _query(self, with_clause='', fields={}, groupby='', from_clause=''):
        fields['industry_id'] = ", l.industry_id"
        groupby += ', l.industry_id'
        return super(SaleReport, self)._query(with_clause, fields, groupby, from_clause)
