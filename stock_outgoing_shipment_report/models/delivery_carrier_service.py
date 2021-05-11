# Copyright 2019 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class DeliveryCarrierService(models.Model):
    _name = "delivery.carrier.service"

    carrier_id = fields.Many2one(
        "delivery.carrier", string="Ship Carrier", required=True,
    )
    name = fields.Char(string="Service", required=True,)
    description = fields.Char(string="Description",)
    mos = fields.Selection(
        [
            ("ground", "Ground"),
            ("air", "Air"),
            ("international", "International"),
            ("ltl", "LTL"),
            ("express", "Express"),
            ("domestic", "Domestic"),
            ("will_call", "WILL CALL"),
        ],
        string="MOS",
        required=True,
    )
    ship_to_residential_indicator = fields.Boolean(
        "ShipToResidentialIndicator", help="For information only."
    )

    def name_get(self):
        res = []
        for record in self:
            name = "{}: {}".format(record.carrier_id.name, record.name)
            res.append((record.id, name))
        return res
