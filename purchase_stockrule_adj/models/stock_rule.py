# Copyright 2019 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models


class StockRule(models.Model):
    _inherit = "stock.rule"

    def _make_po_get_domain(self, values, partner):
        domain = super(StockRule, self)._make_po_get_domain(values, partner)
        if "group_id" in values and values["group_id"].sale_id:
            domain += (
                (
                    "sale_shipping_id",
                    "=",
                    values["group_id"].sale_id.partner_shipping_id.id,
                ),
            )
        return domain
