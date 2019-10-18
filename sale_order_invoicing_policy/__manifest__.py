# -*- coding: utf-8 -*-
# Copyright 2019 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Sale Order Invoicing Policy",
    "summary": "",
    "description": """
This module allow user to change product's invoicing policy on sales order.
""",
    "version": "12.0.1.0.0",
    "category": "Sale",
    "website": "https://www.quartile.co/",
    "author": "Quartile Limited",
    "license": "AGPL-3",
    "installable": True,
    "depends": [
        "sale_stock",
    ],
    "data": [
        "views/sale_order_views.xml",
    ],
}
