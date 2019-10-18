# -*- coding: utf-8 -*-
# Copyright 2019 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging
from odoo import models, fields, api

_logger = logging.getLogger(__name__)

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    sale_invoice_policy = fields.Selection(
        [('order', 'Ordered quantities'),
         ('delivery', 'Delivered quantities')],
        string='Invoicing Policy',
    )