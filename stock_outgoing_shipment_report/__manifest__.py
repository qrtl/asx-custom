# Copyright 2019 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Stock Outgoing Shipment Report",
    "summary": "",
    "version": "12.0.1.0.0",
    "category": "Stock",
    "website": "https://www.quartile.co/",
    "author": "Quartile Limited",
    "license": "AGPL-3",
    "installable": True,
    "depends": [
        "delivery",
        "stock",
    ],
    "data": [
        "data/stock_outgoing_shipment_report_data.xml",
        "security/ir.model.access.csv",
        "views/delivery_carrier_views.xml",
        "views/delivery_carrier_service_views.xml",
        "views/product_template_views.xml",
        "views/res_partner_views.xml",
        "views/sale_order_views.xml",
        "views/stock_outgoing_shipment_report_views.xml",
    ],
}
