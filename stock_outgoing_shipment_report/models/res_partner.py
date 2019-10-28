# Copyright 2019 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields, api


class ResPartner(models.Model):
    _inherit = 'res.partner'

    delivery_carrier_id = fields.Many2one(
        'delivery.carrier',
        string='Delivery Carrier',
    )
    delivery_carrier_account_num = fields.Char(
        string='Delivery Carrier Account Number',
    )
