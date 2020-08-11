# Copyright 2020 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class GeneralLedgerReport(models.TransientModel):
    _inherit = "report_general_ledger"

    hide_partner_without_moves = fields.Boolean()

    @api.multi
    def compute_data_for_report(self, with_line_details=True, with_partners=True):
        super(GeneralLedgerReport, self).compute_data_for_report(
            with_line_details, with_partners
        )
        if self.hide_partner_without_moves:
            self.env["report_general_ledger_partner"].search(
                [("move_line_ids", "=", False)]
            ).unlink()
