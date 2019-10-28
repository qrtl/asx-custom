# Copyright 2019 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields, api


class DeliveryConsigneeCode(models.Model):
    _name = 'delivery.consignee.code'

    name = fields.Char(
        string='Consignee Codes',
        required=True,
    )
    description = fields.Char(
        string='Description',
    )
