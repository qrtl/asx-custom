# Copyright 2019 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Stock Incoming Shipment Report",
    "summary": "",
    "version": "12.0.1.0.0",
    "category": "Stock",
    "website": "https://www.quartile.co/",
    "author": "Quartile Limited",
    "license": "AGPL-3",
    "installable": True,
    "depends": ["delivery",],
    "data": [
        "data/stock_incoming_shipment_report_data.xml",
        "security/ir.model.access.csv",
        "views/stock_incoming_shipment_report_views.xml",
        "wizard/stock_incoming_shipment_report_wizard_views.xml",
    ],
}
