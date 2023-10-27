# Copyright 2023 Quartile Limited
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class ResConfigSetting(models.TransientModel):
    _inherit = "res.config.settings"

    product_standard_price_warning_msg = fields.Text(
        related="company_id.product_standard_price_warning_msg",
        readonly=False
    )
