# Copyright 2019 Quartile Limited
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    credit_balance = fields.Monetary(compute="_compute_risk_exception")

    @api.multi
    @api.depends(lambda x: x._get_depends_compute_risk_exception())
    def _compute_risk_exception(self):
        super()._compute_risk_exception()
        for partner in self.filtered("customer"):
            partner.credit_balance = partner.credit_limit - partner.risk_total
