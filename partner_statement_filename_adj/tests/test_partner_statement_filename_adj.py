# Copyright 2020 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo.tests.common import TransactionCase


class TestActivityStatement(TransactionCase):
    def setUp(self):
        super().setUp()

        self.report = self.env.ref("partner_statement.action_print_activity_statement")
        self.partner1 = self.env.ref("base.res_partner_1")
        self.partner2 = self.env.ref("base.res_partner_2")
        self.wizard = self.env["activity.statement.wizard"]

    def test01_filename_adj(self):
        wizard = self.wizard.with_context(active_ids=[self.partner1.id]).create({})
        wizard._export()
        self.assertTrue(self.partner1.name in self.report.name)
        self.assertTrue(self.partner2.name not in self.report.name)

    def test02_filename_adj(self):
        wizard = self.wizard.with_context(
            active_ids=[self.partner1.id, self.partner2.id],
        ).create({})
        wizard._export()
        self.assertTrue(self.partner1.name not in self.report.name)
        self.assertTrue(self.partner2.name not in self.report.name)
