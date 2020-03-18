# Copyright 2019 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class DeliveryCarrierAccount(models.Model):
    _name = "delivery.carrier.account"

    partner_id = fields.Many2one(
        "res.partner", string="Related Partner", required=True,
    )
    carrier_id = fields.Many2one(
        "delivery.carrier", string="Delivery Carrier", required=True,
    )
    delivery_carrier_account_num = fields.Char(
        string="Delivery Carrier Account Number", required=True,
    )
