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
            order = move.sale_line_id.order_id if move.sale_line_id else False
            picking = move.picking_id
            partner = move.picking_partner_id
            product = move.product_id
            vals = {"move_id": move.id}
            if order:
                carrier = order.carrier_id
                vals["carrier_id"] = carrier.id if carrier else False
                vals["ship_service_id"] = (
                    order.delivery_carrier_service_id
                    and order.delivery_carrier_service_id.id
                )
                vals["ship_account"] = order.shipping_use_carrier_acct
            vals["ship_date_edit"] = fields.Datetime.context_timestamp(
                self, picking.scheduled_date
            ).date()
            vals["purchase_order_number"] = picking.client_order_ref
            if partner:
                vals["ship_to_name"] = partner.name[:30]
                if partner.parent_id:
                    vals["ship_to_company"] = partner.parent_id.name[:30]
                vals["ship_to_address1"] = partner.street and partner.street[:30]
                vals["ship_to_address2"] = partner.street2 and partner.street2[:30]
                vals["ship_to_city"] = partner.city and partner.city[:30]
                vals["ship_to_state"] = partner.state_id and partner.state_id.code
                vals["ship_to_country"] = partner.country_id and partner.country_id.code
                vals["ship_to_zip"] = partner.zip
                vals["ship_to_phone"] = partner.phone
            vals["order_notes"] = (
                product.product_tmpl_id.delivery_report_desc or product.name[:40]
            )
            self.env["stock.outgoing.shipment.report"].create(vals)
        return self.env.ref(
            "stock_outgoing_shipment_report.action_stock_outgoing_shipment_report"
        ).read()[0]
