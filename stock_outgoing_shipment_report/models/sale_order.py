# Copyright 2019 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    shipping_insurance_amt = fields.Float(
        "Shipping Insurance Amount", help="For information only."
    )
    delivery_carrier_service_id = fields.Many2one(
        "delivery.carrier.service", string="Delivery Service",
    )
    shipping_use_carrier_acct = fields.Char(string="Delivery Carrier Account Number",)

    @api.onchange("carrier_id")
    def _onchange_carrier_id(self):
        account_ids = self.partner_shipping_id.delivery_carrier_account_ids
        if self.carrier_id and account_ids.filtered(
            lambda l: l.carrier_id == self.carrier_id
        ):
            self.shipping_use_carrier_acct = account_ids.filtered(
                lambda l: l.carrier_id == self.carrier_id
            ).delivery_carrier_account_num
        else:
            self.shipping_use_carrier_acct = False

    @api.multi
    def write(self, vals):
        res = super(SaleOrder, self).write(vals)
        if "carrier_id" in vals:
            for order in self:
                pickings = order.mapped("picking_ids").filtered(
                    lambda p: p.state not in ("done", "cancel")
                )
                pickings.update({"carrier_id": vals["carrier_id"]})
        return res
