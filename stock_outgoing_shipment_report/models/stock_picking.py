# Copyright 2019-2021 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class StockPicking(models.Model):
    _inherit = "stock.picking"

    @api.multi
    def generate_stock_outgoing_shipment_report(self):
        moves = self.mapped("move_lines")
        self._cr.execute("DELETE FROM stock_outgoing_shipment_report")
        for move in moves:
            sale_line = move.sale_line_id
            order = sale_line.order_id
            picking = move.picking_id
            partner = move.picking_partner_id
            product = move.product_id
            vals = {
                "move_id": move.id,
                "carrier_id": sale_line
                and order.carrier_id
                and order.carrier_id.id
                or False,
                "ship_service_id": sale_line
                and order.delivery_carrier_service_id
                and order.delivery_carrier_service_id.id
                or False,
                "ship_account": sale_line
                and order.shipping_use_carrier_acct
                or False,
                "ship_date_edit": fields.Datetime.context_timestamp(self, picking.scheduled_date).date()
                or False,
                "ship_carrier": sale_line
                and order.carrier_id
                and order.carrier_id.name
                or False,
                "purchase_order_number": picking.client_order_ref or False,
                "ship_to_name": partner.name[:30]
                if partner and len(partner.name) > 30
                else partner and partner.name or False,
                "ship_to_company": partner.parent_id.name[:30]
                if partner
                and partner.parent_id
                and len(partner.parent_id.name) > 30
                else partner
                and partner.parent_id
                and partner.parent_id.name
                or False,
                "ship_to_address1": partner.street[:30]
                if partner
                and len(partner.street or "") > 30
                else partner
                and partner.street
                or False,
                "ship_to_address2": partner.street2[:30]
                if partner
                and len(partner.street2 or "") > 30
                else partner
                and partner.street2
                or False,
                "ship_to_city": partner.city[:30]
                if partner
                and len(partner.city or "") > 30
                else partner and partner.city or False,
                "ship_to_state": partner
                and partner.state_id
                and partner.state_id.code
                or False,
                "ship_to_country": partner
                and partner.country_id
                and partner.country_id.code
                or False,
                "ship_to_zip": partner
                and partner.zip
                or False,
                "ship_to_phone": partner
                and partner.phone
                or False,
                "order_notes": product.product_tmpl_id.delivery_report_desc
                or product.name[:40]
                if len(product.name) > 40
                else product.name,
            }
            self.env["stock.outgoing.shipment.report"].create(vals)
        return self.env.ref(
            "stock_outgoing_shipment_report.action_stock_outgoing_shipment_report"
        ).read()[0]
