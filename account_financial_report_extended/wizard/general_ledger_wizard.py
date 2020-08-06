# Author: Yogesh Mahera
# Author: Tim Lai
# Copyright 2020 Quartile Limited
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class GeneralLedgerReportWizard(models.TransientModel):
    _inherit = "general.ledger.report.wizard"

    hide_partner_without_moves = fields.Boolean(
        string="Hide Partners without Moves",
        help="Hide the Accounts who don't have the partners",
    )

    def _prepare_report_general_ledger(self):
        res = super(GeneralLedgerReportWizard, self)._prepare_report_general_ledger()
        if self.hide_partner_without_moves and not self.partner_ids:
            domain = [
                ("date", ">=", self.date_from),
                ("date", "<=", self.date_to),
                ("company_id", "=", self.company_id.id),
            ]
            if self.target_move == "posted":
                domain += [("state", "=", self.target_move)]
            account_move = self.env["account.move"].search(domain)
            partner_ids = account_move.mapped("line_ids").mapped("partner_id")
            res.update({"filter_partner_ids": [(6, 0, partner_ids.ids)]})
        return res
