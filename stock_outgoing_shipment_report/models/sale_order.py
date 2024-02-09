# Copyright 2019-2024 Quartile Limited
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, models


class SaleOrder(models.Model):
    _name = "sale.order"
    _inherit = ["sale.order", "carrier.info.mixin"]

    @api.multi
    def _get_partner_shipping(self):
        self.ensure_one()
        return self.partner_shipping_id

    @api.onchange("partner_shipping_id")
    def _onchange_partner_shipping_id(self):
        self._onchange_carrier_id()
        return super()._onchange_partner_shipping_id()

    @api.multi
    def action_confirm(self):
        res = super().action_confirm()
        for order in self:
            order.picking_ids.write(
                {
                    "carrier_id": order.carrier_id.id,
                    "delivery_carrier_service_id": order.delivery_carrier_service_id.id,
                    "shipping_use_carrier_acct": order.shipping_use_carrier_acct,
                }
            )
        return res

    @api.multi
    def write(self, vals):
        res = super().write(vals)
        if not any(
            key in vals for key in [
                "carrier_id", "delivery_carrier_service_id", "shipping_use_carrier_acct"
            ]
        ):
            return res
        for order in self:
            pickings = order.mapped("picking_ids").filtered(
                lambda p: p.state not in ("done", "cancel")
            )
            pickings.write(
                {
                    "carrier_id": order.carrier_id.id,
                    "delivery_carrier_service_id": order.delivery_carrier_service_id.id,
                    "shipping_use_carrier_acct": order.shipping_use_carrier_acct,
                }
            )
        return res
