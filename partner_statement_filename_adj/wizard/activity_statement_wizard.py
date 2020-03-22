# Copyright 2020 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class ActivityStatementWizard(models.TransientModel):
    _inherit = "activity.statement.wizard"

    def _export(self):
        report = self.env.ref('partner_statement.action_print_activity_statement')
        report_name = "Activity Statement "
        str_today = fields.Date.to_string(fields.Date.context_today(self))
        res_ids = self._context.get("active_ids")
        if len(res_ids) == 1:
            partner_name = self.env["res.partner"].browse(res_ids).name.replace("/", "")
            report_name += "(" + partner_name + ") " + str_today
        else:
            report_name += str_today
        report.write({"name": report_name})
        return super(ActivityStatementWizard, self)._export()
