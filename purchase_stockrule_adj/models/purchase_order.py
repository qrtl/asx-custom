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
    @api.depends('order_line.move_dest_ids')
    def _compute_sale_shipping_id(self):
        for order in self:
            for order_line in order.order_line:
                for move in order_line.move_dest_ids:
                    if move.sale_line_id:
                        order.sale_shipping_id = move.sale_line_id.order_id.partner_shipping_id
                        return
