# Copyright 2021 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Sales Order Amount History",
    "version": "12.0.1.1.0",
    "category": "Sales",
    "website": "https://www.quartile.co",
    "author": "Quartile Limited",
    "license": "AGPL-3",
    "installable": True,
    "depends": ["sale"],
    "post_init_hook": "post_init_hook",
    "data": [
        "security/ir.model.access.csv",
        "views/account_fiscal_position_views.xml",
        "views/sale_order_amount_history_views.xml",
        "views/sale_order_views.xml",
    ],
}
