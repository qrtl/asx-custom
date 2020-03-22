# Copyright 2018 Eficent Business and IT Consulting Services S.L.
#   (http://www.eficent.com)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import models


class ActivityStatementWizard(models.TransientModel):
    _inherit = "activity.statement.wizard"

    def _export(self):
        report = self.env.ref('partner_statement.action_print_activity_statement')
        res_ids = self._context.get("active_ids")
        # FIXME update report name of user's language
        if len(res_ids) == 1:
            partner = self.env["res.partner"].browse(res_ids)
            report.write({"name": "Activity Statement (" + partner.name + ")"})
        else:
            report.write({"name": "Activity Statement"})
        return super(ActivityStatementWizard, self)._export()
