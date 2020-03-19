# Copyright 2019 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class StockIncomingShipmentReportWizard(models.TransientModel):
    _name = "stock.incoming.shipment.report.wizard"

    date_expected = fields.Datetime("Expected Date")

    @api.multi
    def generate_stock_incoming_shipment_report_action(self):
        self.ensure_one()
        picking_ids = self.env.context.get("picking_ids", [])
        moves = (
            self.env["stock.picking"]
            .browse(picking_ids)
            .mapped("move_lines")
            .filtered(lambda l: l.date_expected <= self.date_expected)
        )
        self._cr.execute("DELETE FROM stock_incoming_shipment_report")
        for move in moves:
            vals = {
                "move_id": move.id,
                "tracking_pro_num": move.picking_id.carrier_tracking_ref or False,
                "anticipated_arrival_date_edit": move.date_expected,
                "carrier_code": move.picking_id.carrier_id
                and move.picking_id.carrier_id.name
                or False,
            }
            self.env["stock.incoming.shipment.report"].create(vals)
        return self.env.ref(
            "stock_incoming_shipment_report.action_stock_incoming_shipment_report"
        ).read()[0]
