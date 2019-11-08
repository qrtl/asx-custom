# Copyright 2019 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Sales Order Additional Information",
    "summary": "",
    "version": "12.0.1.0.1",
    "category": "Sales",
    "website": "https://www.quartile.co/",
    "author": "Quartile Limited",
    "license": "AGPL-3",
    "installable": True,
    "depends": [
        "delivery",
        "sale",
    ],
    "data": [
        "reports/sale_order_report_templates.xml",
        "views/res_partner_views.xml",
        "views/sale_order_views.xml",
        "views/sale_portal_templates.xml",
    ],
}
