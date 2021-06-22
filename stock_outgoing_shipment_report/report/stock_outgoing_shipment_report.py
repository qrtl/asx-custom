# Copyright 2019-2021 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import _, api, fields, models
from odoo.exceptions import ValidationError


class StockOutgoingShipmentReport(models.TransientModel):
    _name = "stock.outgoing.shipment.report"

    move_id = fields.Many2one("stock.move", string="Stock Move", readonly=True,)
    carrier_id = fields.Many2one("delivery.carrier", string="Carrier")
    # Following fields are for export.
    reference_number = fields.Char(
        related="move_id.picking_id.name", string="ReferenceNumber", store=True,
    )
    purchase_order_number = fields.Char("PurchaseOrderNumber")
    ship_date = fields.Char(
        string="ShipDate", compute="_compute_date_fields", store=True,
    )
    ship_date_edit = fields.Date(
        "ShipDate (Not For Export)",
        help="Defaulted from Scheduled Date of the picking.",
    )
    cancel_date = fields.Char(
        string="CancelDate", compute="_compute_date_fields", store=True,
    )
    cancel_date_edit = fields.Date("CancelDate (Not For Export)")
    ship_carrier = fields.Char(
        related="carrier_id.name", string="ShipCarrier", store=True,
    )
    ship_service_id = fields.Many2one(
        "delivery.carrier.service", string="ShipService (Not for Export)",
    )
    ship_service = fields.Char(
        related="ship_service_id.name", string="ShipService", store=True,
    )
    ship_account = fields.Char(
        "ShipAccount" , related="ship_carrier.name"
        )
    ship_billing = fields.Char("ShipBilling")
    ship_to_name = fields.Char("ShipToName")
    ship_to_company = fields.Char("ShipToCompany")
    ship_to_address1 = fields.Char("ShipToAddress1")
    ship_to_address2 = fields.Char("ShipToAddress2")
    ship_to_city = fields.Char("ShipToCity")
    ship_to_state = fields.Char("ShipToState")
    ship_to_zip = fields.Char("ShipToZip")
    ship_to_country = fields.Char("ShipToCountry")
    ship_to_phone = fields.Char("ShipToPhone")
    retailerid = fields.Char("RetailerID")
    sku = fields.Char(
        related="move_id.product_id.default_code", string="Sku", store=True,
    )
    lot_number = fields.Char("LotNumber")
    quantity = fields.Float(
        related="move_id.product_qty", string="Quantity", store=True
    )
    line_item_fulfillment_sale_price = fields.Char("LineItemFulfillmentSalePrice")
    sold_to_address1 = fields.Char("SoldToAddress1")
    sold_to_address2 = fields.Char("SoldToAddress2")
    sold_to_city = fields.Char("SoldToCity")
    sold_to_state = fields.Char("SoldToState")
    sold_to_zip = fields.Char("SoldToZip")
    sold_to_country = fields.Char("SoldToCountry")
    sold_to_phone = fields.Char("SoldToPhone")
    sold_to_code = fields.Char("SoldToCode")
    order_notes = fields.Char("OrderNotes")
    fulfillment_gift_message = fields.Char("FulfillmentGiftMessage")
    incomplete_status = fields.Char("IncompleteStatus")

    @api.constrains(
        "ship_to_name",
        "ship_to_company",
        "ship_to_address1",
        "ship_to_address2",
        "ship_to_city",
        "order_notes",
        "sold_to_address1",
        "sold_to_address2",
        "sold_to_city",
    )
    def _validate_field_length(self):
        for rec in self:
            msg = _("%s should be at most %s digit(s).")
            fields_list = {
                "ship_to_name": ["ShipToName", 30],
                "ship_to_company": ["ShipToCompany", 30],
                "ship_to_address1": ["ShipToAddress1", 30],
                "ship_to_address2": ["ShipToAddress2", 30],
                "ship_to_city": ["ShipToCity", 30],
                "order_notes": ["OrderNotes", 40],
                "sold_to_address1": ["SoldToAddress1", 30],
                "sold_to_address2": ["SoldToAddress2", 30],
                "sold_to_city": ["SoldToCity", 30],
            }
            for field in fields_list:
                if rec[field] and len(rec[field]) > fields_list[field][1]:
                    raise ValidationError(
                        msg % (_(fields_list[field][0]), fields_list[field][1])
                    )

    @api.constrains(
        "ship_to_state", "ship_to_country", "sold_to_state", "sold_to_country"
    )
    def _validate_country_state(self):
        for rec in self:
            msg = _("Invalid %s.")
            if rec.sold_to_state:
                state = self.env["res.country.state"].search(
                    [("code", "=", rec.sold_to_state)]
                )
                if not state:
                    raise ValidationError(msg % (_("SoldToState")))
            if rec.ship_to_state:
                state = self.env["res.country.state"].search(
                    [("code", "=", rec.ship_to_state)]
                )
                if not state:
                    raise ValidationError(msg % (_("ShipToState")))
            if rec.sold_to_country:
                country = self.env["res.country"].search(
                    [("code", "=", rec.sold_to_country)]
                )
                if not country:
                    raise ValidationError(msg % (_("SoldToCountryCode")))
            if rec.ship_to_country:
                country = self.env["res.country"].search(
                    [("code", "=", rec.ship_to_country)]
                )
                if not country:
                    raise ValidationError(msg % (_("ShipToCountryCode")))

    @api.multi
    @api.depends("ship_date_edit", "cancel_date_edit")
    def _compute_date_fields(self):
        for line in self:
            date_format = "%m/%d/%Y"
            if line.ship_date_edit:
                line.ship_date = line.ship_date_edit.strftime(date_format)
            if line.cancel_date_edit:
                line.cancel_date = line.cancel_date_edit.strftime(date_format)
