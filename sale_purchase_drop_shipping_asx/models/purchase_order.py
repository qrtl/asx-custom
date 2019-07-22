# Copyright 2019 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields, api


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    sale_shipping_id = fields.Many2one(
        'res.partner',
        string='Sale Order\'s Delivery Address',
        compute='_compute_sale_shipping_id',
        store=True,
    )

    @api.multi
    @api.depends('origin')
    def _compute_sale_shipping_id(self):
        for order in self:
            sale_order_name_list = order.origin.split(',')
            sale_orders = self.env['sale.order'].search(
                [('name', 'in', sale_order_name_list)])
            if sale_orders:
                order.sale_shipping_id = sale_orders[0].partner_shipping_id
