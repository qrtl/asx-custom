# Copyright 2020 Quartile Limited
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import api, fields, models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    enduser_id = fields.Many2one("res.partner", "Enduser")

    @api.multi
    def _prepare_invoice(self):
        self.ensure_one()
        invoice_vals = super(SaleOrder, self)._prepare_invoice()
        if self.enduser_id:
            invoice_vals["enduser_id"] = self.enduser_id.id
        return invoice_vals
