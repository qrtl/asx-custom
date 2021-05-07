# Copyright 2019 Open Source Integrators
# Copyright 2021 Quartile Limited
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Sale Tier Validation Quotation Print",
    "summary": "Extends the functionality of Sale Orders to "
               "support a tier validation process.",
    "version": "12.0.1.0.0",
    "category": "Sale",
    "website": "https://quartile.co",
    "author": "Open Source Integrators, Odoo Community Association (OCA), Quartile Limited",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        "sale",
        "base_tier_validation",
    ],
    "data": [
        "report/sale_report.xml",
        "views/sale_order_view.xml",
    ],
}
