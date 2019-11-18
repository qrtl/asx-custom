# Copyright 2019 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Delivery Functions Adjustments",
    "summary": "",
    "description": """
 - Avoid create the delivery charge line in sales order for free shipping.
 - Add Sale Order Salesperon as outgoing shipment's follower while confirmation.
    """,
    'version': '12.0.1.1.0',
    "category": "Stock",
    "website": "https://www.quartile.co/",
    "author": "Quartile Limited",
    "license": "AGPL-3",
    "installable": True,
    "depends": [
        "delivery",
    ],
}
