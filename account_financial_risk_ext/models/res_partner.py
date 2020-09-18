# Copyright 2020 Quartile Limited
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    credit_balance = fields.Monetary(compute="_compute_credit_balance")

    @api.multi
    @api.depends(lambda x: x._get_depends_compute_risk_exception())
    def _compute_credit_balance(self):
        for partner in self:
            partner.credit_balance = partner.credit_limit - partner.risk_total
