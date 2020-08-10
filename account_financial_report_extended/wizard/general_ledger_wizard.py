# Copyright 2020 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class GeneralLedgerReportWizard(models.TransientModel):
    _inherit = "general.ledger.report.wizard"

    hide_partner_without_moves = fields.Boolean(
        string="Hide Partners without Moves",
        help="If selected, partners that do not have account moves will"
        " not show in the result for payable and receivable accounts.",
    )

    def _prepare_report_general_ledger(self):
        res = super(GeneralLedgerReportWizard, self)._prepare_report_general_ledger()
        res["hide_partner_without_moves"] = self.hide_partner_without_moves
        return res
