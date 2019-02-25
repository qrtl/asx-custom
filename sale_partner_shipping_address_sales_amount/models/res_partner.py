# Copyright 2019 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields, api


class ResPartner(models.Model):
    _inherit = 'res.partner'

    delivery_sales_amount = fields.Float(
        compute='_compute_delivery_sales_amount',
        string='Sale (Delivery)'
    )

    @api.multi
    def _compute_delivery_sales_amount(self):
        for partner in self:
            delivery_amount = 0
            orders = self.env['sale.order'].search([
                ('partner_shipping_id', 'child_of',
                 partner.commercial_partner_id.id),
                ('state', 'in', ['sale', 'done'])
            ])
            for order in orders:
                delivery_amount += order.amount_total
            partner.delivery_sales_amount = delivery_amount

    @api.multi
    def action_view_delivery_sale_order(self):
        self.ensure_one()
        action = self.env.ref('sale.action_orders').read()[0]
        action['domain'] = [
            ('partner_shipping_id', 'child_of',
             self.commercial_partner_id.id),
            ('state', 'in', ['sale', 'done'])
        ]
        return action
