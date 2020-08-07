# Copyright 2020 Quartile Limited
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import fields, models


class GeneralLedgerReportWizard(models.TransientModel):
    _inherit = "general.ledger.report.wizard"

    hide_partner_without_moves = fields.Boolean(
        string="Hide Partners without Moves",
        help="Hide the Accounts who don't have the partners",
    )

    def _prepare_report_general_ledger(self):
        res = super(GeneralLedgerReportWizard, self)._prepare_report_general_ledger()
        res["hide_partner_without_moves"] = self.hide_partner_without_moves
        return res
