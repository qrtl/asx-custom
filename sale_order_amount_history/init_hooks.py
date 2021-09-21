# Copyright 2021 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import SUPERUSER_ID, fields
from odoo.api import Environment


def post_init_hook(cr, registry):
    env = Environment(cr, SUPERUSER_ID, {})
    for order in env["sale.order"].search(
        [("state", "in", ("sale", "done")), ("amount_untaxed", "!=", 0.0)]
    ):
        date_conf = fields.Date.to_date(
            fields.Datetime.context_timestamp(order, order.confirmation_date)
        )
        history_vals = {
            "order_id": order.id,
            "currency_id": order.currency_id.id,
            "history_type": "add",
            "order_count": 1,
            "amount": order.amount_untaxed,
            "amount_diff": order.amount_untaxed,
            "date": date_conf,
        }
        env["sale.order.amount.history"].create(history_vals)
