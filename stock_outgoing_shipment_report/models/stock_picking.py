# Copyright 2019 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, models


class StockPicking(models.Model):
    _inherit = "stock.picking"

    @api.multi
    def generate_stock_outgoing_shipment_report(self):
        moves = self.mapped("move_lines")
        self._cr.execute("DELETE FROM stock_outgoing_shipment_report")
        for move in moves:
            vals = {
                "move_id": move.id,
                "carrier_id": move.sale_line_id
                and move.sale_line_id.order_id.carrier_id
                and move.sale_line_id.order_id.carrier_id.id
                or False,
                "shipping_service_id": move.sale_line_id
                and move.sale_line_id.order_id.delivery_carrier_service_id
                and move.sale_line_id.order_id.delivery_carrier_service_id.id
                or False,
                "ship_account": move.sale_line_id
                and move.sale_line_id.order_id.shipping_use_carrier_acct
                or False,
                "po_date_edit": move.sale_line_id
                and move.sale_line_id.order_id.date_order
                or False,
                "shipping_carrier": move.sale_line_id
                and move.sale_line_id.order_id.carrier_id
                and move.sale_line_id.order_id.carrier_id.name
                or False,
                "shipping_insurance_amount": move.sale_line_id
                and move.sale_line_id.order_id.shipping_insurance_amt
                and str(move.sale_line_id.order_id.shipping_insurance_amt)
                or False,
                "shipping_reference1": move.picking_id.client_order_ref or False,
                "ship_to_first_name": move.picking_partner_id.name[:30]
                if move.picking_partner_id and len(move.picking_partner_id.name) > 30
                else move.picking_partner_id and move.picking_partner_id.name or False,
                "ship_to_company": move.picking_partner_id.parent_id.name[:30]
                if move.picking_partner_id
                and move.picking_partner_id.parent_id
                and len(move.picking_partner_id.parent_id.name) > 30
                else move.picking_partner_id
                and move.picking_partner_id.parent_id
                and move.picking_partner_id.parent_id.name
                or False,
                "ship_to_address1": move.picking_partner_id.street[:30]
                if move.picking_partner_id
                and len(move.picking_partner_id.street or "") > 30
                else move.picking_partner_id
                and move.picking_partner_id.street
                or False,
                "ship_to_address2": move.picking_partner_id.street2[:30]
                if move.picking_partner_id
                and len(move.picking_partner_id.street2 or "") > 30
                else move.picking_partner_id
                and move.picking_partner_id.street2
                or False,
                "ship_to_city": move.picking_partner_id.city[:30]
                if move.picking_partner_id
                and len(move.picking_partner_id.city or "") > 30
                else move.picking_partner_id and move.picking_partner_id.city or False,
                "ship_to_state": move.picking_partner_id
                and move.picking_partner_id.state_id
                and move.picking_partner_id.state_id.code
                or False,
                "ship_to_country_code": move.picking_partner_id
                and move.picking_partner_id.country_id
                and move.picking_partner_id.country_id.code
                or False,
                "ship_to_zip": move.picking_partner_id
                and move.picking_partner_id.zip
                or False,
                "ship_to_phone": move.picking_partner_id
                and move.picking_partner_id.phone
                or False,
                "description": move.product_id.product_tmpl_id.delivery_report_desc
                or move.product_id.name[:40]
                if len(move.product_id.name) > 40
                else move.product_id.name,
            }
            self.env["stock.outgoing.shipment.report"].create(vals)
        return self.env.ref(
            "stock_outgoing_shipment_report.action_stock_outgoing_shipment_report"
        ).read()[0]
