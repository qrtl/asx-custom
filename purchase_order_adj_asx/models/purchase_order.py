# Copyright 2019 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields, api


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    evidence_status = fields.Selection([
       ('more', 'Need More'),
       ('done', 'Done'),
    ], string="Evidence Status", default='')
    
    evidence_text = fields.Char()
    memo = fields.Text(string="Memo")
