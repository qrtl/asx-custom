# Copyright 2019 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class DeliveryCarrier(models.Model):
    _inherit = "delivery.carrier"

    delivery_carrier_service_ids = fields.One2many(
        "delivery.carrier.service",
        inverse_name="carrier_id",
        string="Available Service(s)",
    )

    ship_billing = fields.Selection(
        [("third_party", "Third Party"), ("bill_third_party", "Bill Third Party")],
        string="Ship Billing"
    )
