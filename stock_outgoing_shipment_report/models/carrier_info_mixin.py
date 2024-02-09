# Copyright 2024 Quartile Limited
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class CarrierInfoMixin(models.AbstractModel):
    """This model should only be inherited by a model with `carrier_id` field."""
    _name = "carrier.info.mixin"
    _description = "Carrier Information Mixin"

    shipping_insurance_amt = fields.Float(
        "Shipping Insurance Amount", help="For information only."
    )
    delivery_carrier_service_id = fields.Many2one(
        "delivery.carrier.service",
        string="Delivery Service",
        domain="[('carrier_id', '=', carrier_id)]",
    )
    shipping_use_carrier_acct = fields.Char("Delivery Carrier Account Number")

    @api.multi
    def _get_partner_shipping(self):
        raise NotImplementedError

    @api.onchange("carrier_id")
    def _onchange_carrier_id(self):
        self.delivery_carrier_service_id = False
        partner = self._get_partner_shipping()
        account_ids = partner.delivery_carrier_account_ids
        carrier_acct = account_ids.filtered(
            lambda l: l.carrier_id == self.carrier_id
        )[:1]
        if carrier_acct:
            self.shipping_use_carrier_acct = carrier_acct.delivery_carrier_account_num
        else:
            self.shipping_use_carrier_acct = False
