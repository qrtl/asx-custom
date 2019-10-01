# Copyright 2019 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Account Invoice Sent Date",
    "summary": "",
    'description': """
This module adds the functionality to record the date invoice was sent by 
email.
    """,
    "version": "12.0.1.1.0",
    "category": "Accounting",
    "website": "https://www.quartile.co/",
    "author": "Quartile Limited",
    "license": "AGPL-3",
    "installable": True,
    "depends": [
        "account",
    ],
    "data": [
        "views/account_invoice_views.xml",
    ],
}
