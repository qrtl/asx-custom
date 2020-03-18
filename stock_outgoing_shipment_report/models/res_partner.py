# Copyright 2019 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    delivery_carrier_account_ids = fields.One2many(
        "delivery.carrier.account",
        inverse_name="partner_id",
        string="Delivery Carrier Account(s)",
    )
