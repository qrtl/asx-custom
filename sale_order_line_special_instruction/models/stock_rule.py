# Copyright 2019 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields, api


class StockRule(models.Model):
    _inherit = 'stock.rule'

    @api.multi
    def _run_buy(self, product_id, product_qty, product_uom, location_id, name,
                 origin, values):
        res = super(StockRule, self)._run_buy(product_id, product_qty,
                                              product_uom, location_id,
                                              name, origin, values)
        suppliers = product_id.seller_ids.filtered(
            lambda r: (not r.company_id or r.company_id == values[
                'company_id']) and (not r.product_id or r.product_id ==
                                    product_id))
        supplier = self._make_po_select_supplier(values, suppliers)
        partner = supplier.name
        domain = self._make_po_get_domain(values, partner)
        if domain:
            po = self.env['purchase.order'].sudo().search(
                [dom for dom in domain])
            for line in po.order_line:
                if line.product_id == product_id and line.product_uom == \
                        product_id.uom_po_id:
                    print(values)
                    print(line)
                    print(line.special_instruction)
                    # print(values['special_instruction'])
                    # values = [line.special_instruction, values[
                    #     'special_instruction']]
                    # line.sudo().write({
                    #     'special_instruction': ','.join(values)
                    # })
        return res
