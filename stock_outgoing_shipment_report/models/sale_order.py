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
    shipping_use_carrier_acct = fields.Char(
        string='Delivery Carrier Account Number',
    )

    @api.onchange('carrier_id')
    def _onchange_carrier_id(self):
        if self.carrier_id and self.partner_shipping_id.delivery_carrier_account_ids.filtered(
                lambda l: l.carrier_id == self.carrier_id):
            self.shipping_use_carrier_acct = self.partner_shipping_id.delivery_carrier_account_ids.filtered(
                lambda l: l.carrier_id == self.carrier_id).delivery_carrier_account_num
        else:
            self.shipping_use_carrier_acct = False
