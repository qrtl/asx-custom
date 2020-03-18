# Copyright 2019 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    'name': 'Special Instruction for Sales Order Line',
    'version': '12.0.1.0.0',
    'author': 'Quartile Limited',
    'website': 'https://www.quartile.co',
    'category': 'Sales',
    'license': "LGPL-3",
    'description': """
Add "Special Instruction" field to sales order line, the field will be passed
to stock move and purchase order order.
""",
    'depends': [
        'sale_order_line_view',
        'sale_stock',
        'purchase_stock',
    ],
    "data": [
        "views/purchase_order_views.xml",
        "views/sale_order_views.xml",
        "views/stock_move_views.xml",
        "views/stock_picking_views.xml",
    ],
    'installable': True,
}
