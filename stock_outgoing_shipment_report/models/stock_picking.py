# Copyright 2019 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields, api, _


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    @api.multi
    def generate_stock_outgoing_shipment_report(self):
        moves = self.mapped('move_lines')
        self._cr.execute("DELETE FROM stock_outgoing_shipment_report")
        for move in moves:
            self.env['stock.outgoing.shipment.report'].create({
                'move_id': move.id
            })
        return self.env.ref('stock_outgoing_shipment_report.action_stock_outgoing_shipment_report').read()[0]
