# Copyright 2019 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Sales Order's Customer Reference Adjustments",
    "summary": "",
    "version": "12.0.1.0.0",
    "category": "Sales",
    "website": "https://www.quartile.co/",
    "author": "Quartile Limited",
    "license": "AGPL-3",
    "installable": True,
    "depends": [
        "sale_stock",
    ],
    "data": [
        "views/sale_order_views.xml",
        "views/stock_picking_views.xml",
    ],
}
