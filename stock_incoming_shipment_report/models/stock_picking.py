# Copyright 2019 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models


class StockPicking(models.Model):
    _inherit = "stock.picking"

    def open_stock_incoming_shipment_report_wizard(self):
        return {
            "type": "ir.actions.act_window",
            "name": "Generate Incoming Shipment Data",
            "view_type": "form",
            "view_mode": "form",
            "res_model": "stock.incoming.shipment.report.wizard",
            "target": "new",
            "context": {"picking_ids": self.env.context.get("active_ids", [])},
        }
