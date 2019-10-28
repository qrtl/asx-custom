# Copyright 2019 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    shipping_insurance_amt = fields.Float(
        string='Shipping Insurance Amount',
    )
    delivery_carrier_service_id = fields.Many2one(
        'delivery.carrier.service',
        string='Delivery Service',
    )
    delivery_consignee_code_id = fields.Many2one(
        'delivery.consignee.code',
        string='Consignee Code',
    )
