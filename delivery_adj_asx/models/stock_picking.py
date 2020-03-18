# Copyright 2019 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, models


class StockPicking(models.Model):
    _inherit = "stock.picking"

    @api.multi
    def _add_delivery_cost_to_so(self):
        """ Override standard method so that sales order line is not created when
            carrier_price is zero.
        """
        self.ensure_one()
        sale_order = self.sale_id
        if sale_order.invoice_shipping_on_delivery:
            # sale_order._create_delivery_line(self.carrier_id, self.carrier_price)
            if self.carrier_price:
                sale_order._create_delivery_line(self.carrier_id, self.carrier_price)
