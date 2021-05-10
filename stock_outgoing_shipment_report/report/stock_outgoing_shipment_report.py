# Copyright 2019 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import _, api, fields, models
from odoo.exceptions import ValidationError


class StockOutgoingShipmentReport(models.TransientModel):
    _name = "stock.outgoing.shipment.report"

    move_id = fields.Many2one("stock.move", string="Stock Move", readonly=True,)
    carrier_id = fields.Many2one("delivery.carrier", string="Carrier",)
    customer_order_no = fields.Char(
        related="move_id.picking_id.name", string="ReferenceNumber", store=True,
    )
    po_date = fields.Char(string="PODate", compute="_compute_date_fields", store=True,)
    po_date_edit = fields.Date(string="PODate (Not For Export)",)
    ship_date = fields.Char(
        string="ShipDate", compute="_compute_date_fields", store=True,
    )
    ship_date_edit = fields.Date(string="ShipDate (Not For Export)",)
    ship_no_later = fields.Char(
        string="ShipNoLater", compute="_compute_date_fields", store=True,
    )
    ship_no_later_edit = fields.Date(string="ShipNoLater (Not For Export)",)
    shipping_carrier = fields.Char(
        related="carrier_id.name", string="ShipCarrier", store=True,
    )
    shipping_service_id = fields.Many2one(
        "delivery.carrier.service", string="ShipService",
    )
    shipping_service = fields.Char(
        related="shipping_service_id.name", string="ShipService", store=True,
    )
    shipping_signature_requred = fields.Selection(
        [("Y", "Y"), ("N", "N")], string="ShippingSignatureRequred", default="Y",
    )
    shipping_saturday_delivery = fields.Selection(
        [("Y", "Y")], string="ShippingSaturdayDelivery", default=False,
    )
    ship_account = fields.Char("ShipAccount")
    ship_billing = fields.Char("ShipBilling")
    shipping_carrier_acct_type = fields.Char(string="ShippingCarrierAcctType",)
    shipping_insure_shipment = fields.Selection(
        [("Y", "Y")], string="ShippingInsureShipment", default=False,
    )
    shipping_insurance_amount = fields.Char(
        string="ShippingInsuranceAmount", readonly=True,
    )
    ship_from_dc = fields.Selection(
        [("TUAL", "TUAL"), ("ATLA", "ATLA")], string="ShipFromDC", default=False,
    )
    ship_to_residential_indicator = fields.Selection(
        [("Y", "Y")],
        string="ShipToResidentialIndicator",
        compute="_compute_ship_to_residential_indicator",
        store=True,
        readonly=False,
    )
    shipping_charge = fields.Char(string="ShippingCharge",)
    shipping_reference1 = fields.Char(string="PurchaseOrderNumber",)
    shipping_reference2 = fields.Char(string="ShippingReference2",)
    ship_to_first_name = fields.Char(string="ShipToFirstName",)
    ship_to_last_name = fields.Char(string="ShipToLastName",)
    ship_to_company = fields.Char(string="ShipToCompany",)
    ship_to_address1 = fields.Char(string="ShipToAddress1",)
    ship_to_address2 = fields.Char(string="ShipToAddress2",)
    ship_to_city = fields.Char(string="ShipToCity",)
    ship_to_state = fields.Char(string="ShipToState",)
    ship_to_country_code = fields.Char(string="ShipToCountryCode",)
    ship_to_zip = fields.Char(string="ShipToZip",)
    ship_to_phone = fields.Char(string="ShipToPhone",)
    ship_to_customer_no = fields.Char(string="ShipToCustomerNo",)
    shipping_con_code = fields.Char(string="ShippingConCode",)
    includes_kit_items = fields.Selection(
        [("Y", "Y")], string="IncludesKitItems", default=False,
    )
    sku = fields.Char(
        related="move_id.product_id.default_code", string="Sku", store=True,
    )
    quantity = fields.Float(related="move_id.product_qty", string="Quantity", store=True,)
    description = fields.Char(string="OrderNotes",)
    po_line_no = fields.Char(string="PoLineNo",)
    item_no_ref = fields.Char(string="ItemNoRef",)
    original_price = fields.Char(string="OriginalPrice",)
    price = fields.Char(string="Price",)
    discounted_price = fields.Char(string="DiscountedPrice",)
    sold_to_first_name = fields.Char(string="SoldToFirstName",)
    sold_to_last_name = fields.Char(string="SoldToLastName",)
    sold_to_company = fields.Char(string="SoldToCompany",)
    sold_to_address1 = fields.Char(string="SoldToAddress1",)
    sold_to_address2 = fields.Char(string="SoldToAddress2",)
    sold_to_city = fields.Char(string="SoldToCity",)
    sold_to_state = fields.Char(string="SoldToState",)
    sold_to_country_code = fields.Char(string="SoldToCountryCode",)
    sold_to_zip = fields.Char(string="SoldToZip",)
    sold_to_phone = fields.Char(string="SoldToPhone",)
    sold_to_customer_no = fields.Char(string="SoldToCustomerNo",)
    order_note = fields.Text(string="OrderNote",)
    gift_message = fields.Text(string="Gift Message",)
    lot = fields.Char(string="Lot",)

    @api.constrains(
        "ship_to_first_name",
        "ship_to_last_name",
        "ship_to_company",
        "ship_to_address1",
        "ship_to_address2",
        "ship_to_city",
        "ship_to_customer_no",
        "description",
        "po_line_no",
        "item_no_ref",
        "sold_to_first_name",
        "sold_to_last_name",
        "sold_to_company",
        "sold_to_address1",
        "sold_to_address2",
        "sold_to_city",
        "sold_to_customer_no",
        "order_note",
        "gift_message",
    )
    def _validate_field_length(self):
        for rec in self:
            msg = _("%s should be at most %s digit(s).")
            fields_list = {
                "ship_to_first_name": ["ShipToFirstName", 30],
                "ship_to_last_name": ["ShipToLastName", 30],
                "ship_to_company": ["ShipToCompany", 30],
                "ship_to_address1": ["ShipToAddress1", 30],
                "ship_to_address2": ["ShipToAddress2", 30],
                "ship_to_city": ["ShipToCity", 30],
                "ship_to_customer_no": ["ShipToCustomerNo", 20],
                "description": ["Description", 40],
                "po_line_no": ["PoLineNo", 3],
                "item_no_ref": ["ItemNoRef", 20],
                "sold_to_first_name": ["SoldToFirstName", 30],
                "sold_to_last_name": ["SoldToLastName", 30],
                "sold_to_company": ["SoldToCompany", 30],
                "sold_to_address1": ["SoldToAddress1", 30],
                "sold_to_address2": ["SoldToAddress2", 30],
                "sold_to_city": ["SoldToCity", 30],
                "sold_to_customer_no": ["SoldToCustomerNo", 20],
                "order_note": ["OrderNote", 320],
                "gift_message": ["Gift Message", 250],
            }
            for field in fields_list:
                if rec[field] and len(rec[field]) > fields_list[field][1]:
                    raise ValidationError(
                        msg % (_(fields_list[field][0]), fields_list[field][1])
                    )

    @api.constrains(
        "ship_to_state", "ship_to_country_code", "sold_to_state", "sold_to_country_code"
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
            if rec.sold_to_country_code:
                country = self.env["res.country"].search(
                    [("code", "=", rec.sold_to_country_code)]
                )
                if not country:
                    raise ValidationError(msg % (_("SoldToCountryCode")))
            if rec.ship_to_country_code:
                country = self.env["res.country"].search(
                    [("code", "=", rec.ship_to_country_code)]
                )
                if not country:
                    raise ValidationError(msg % (_("ShipToCountryCode")))

    @api.constrains("shipping_charge")
    def _validate_number_fields(self):
        for rec in self:
            msg = _("Only numbers are allowed for %s field.")
            try:
                int(rec.shipping_charge)
            except Exception:
                try:
                    float(rec.shipping_charge)
                except Exception:
                    raise ValidationError(msg % _("ShippingCharge"))

    @api.multi
    @api.depends("po_date_edit", "ship_date_edit", "ship_no_later_edit")
    def _compute_date_fields(self):
        for line in self:
            date_format = "%m/%d/%Y"
            if line.po_date_edit:
                line.po_date = line.po_date_edit.strftime(date_format)
            if line.ship_date_edit:
                line.ship_date = line.ship_date_edit.strftime(date_format)
            if line.ship_no_later_edit:
                line.ship_no_later = line.ship_no_later_edit.strftime(date_format)

    @api.multi
    @api.depends("shipping_service_id")
    def _compute_ship_to_residential_indicator(self):
        for line in self:
            if (
                line.shipping_service_id
                and line.shipping_service_id.ship_to_residential_indicator
            ):
                line.ship_to_residential_indicator = "Y"
