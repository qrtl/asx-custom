# Copyright 2019 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    'name': 'Group 3PL',
    'summary': '',
    'description': """
Restricts access to records/menu items/view items for 3PL users.

Update '3PL Users' field in warehouse for 3PL users to be able to access
the picking records of the warehouse.
    """,
    'version': '12.0.1.0.0',
    'category': 'Security',
    'website': 'https://www.quartile.co/',
    'author': 'Quartile Limited',
    'license': 'AGPL-3',
    'installable': True,
    'depends': [
        'sale_stock',
        'purchase_stock',
        'contacts',
        'calendar',
    ],
    'data': [
        'security/stock_security.xml',
        'security/ir.model.access.csv',
        'views/stock_menu_views.xml',
        'views/stock_warehouse_views.xml',
        'views/stock_picking_views.xml',
        'views/product_views.xml',
        'views/res_partner_views.xml',
    ],
}
