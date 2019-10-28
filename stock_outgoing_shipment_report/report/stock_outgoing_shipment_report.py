# Copyright 2019 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class stockOutgoingShipmentReport(models.TransientModel):
    _name = 'stock.outgoing.shipment.report'

    move_id = fields.Many2one(
        'stock.move',
        string='Stock Move',
        readonly=True,
    )
    carrier_id = fields.Many2one(
        related='move_id.sale_line_id.order_id.carrier_id',
        string='Carrier',
        store=True,
    )
    customer_order_no = fields.Char(
        related='move_id.picking_id.name',
        string='CustomerOrderNo',
        store=True,
    )
    po_number = fields.Char(
        related='move_id.sale_line_id.order_id.name',
        string='PONumber',
        store=True,
    )
    po_date = fields.Datetime(
        related='move_id.sale_line_id.order_id.date_order',
        string='PODate',
        store=True,
    )
    ship_date = fields.Date(
        string='ShipDate',
    )
    ship_no_later = fields.Date(
        string='ShipNoLater',
    )
    shipping_carrier = fields.Char(
        related='carrier_id.name',
        string='ShippingCarrier',
        store=True,
    )
    shipping_service = fields.Char(
        related='move_id.sale_line_id.order_id.delivery_carrier_service_id.name',
        string='ShippingService',
        store=True,
    )
    shipping_signature_requred = fields.Selection(
        [('Y', 'Y'),
         ('N', 'N')],
        string='ShippingSignatureRequred',
        default='Y',
    )
    shipping_saturday_delivery = fields.Selection(
        [('Y', 'Y'),
         ('N', 'N')],
        string='ShippingSaturdayDelivery',
        default='N',
    )
    shipping_use_carrier_acct = fields.Char(
        compute='_get_shipping_use_carrier_acct',
        string='ShippingUseCarrierAcct',
        store=True,
        readonly=False,
    )
    shipping_carrier_acct_type = fields.Char(
        string='ShippingCarrierAcctType',
    )
    shipping_insure_shipment = fields.Selection(
        [('Y', 'Y'),
         ('N', 'N')],
        string='ShippingInsureShipment',
        default='N',
    )
    shipping_insurance_amount = fields.Float(
        related='move_id.sale_line_id.order_id.shipping_insurance_amt',
        string='ShippingInsuranceAmount',
        store=True,
    )
    ship_from_dc = fields.Selection(
        [('TUAL', 'TUAL'),
         ('ATLA', 'ATLA')],
        string='ShipFromDC',
        default='TUAL',
    )
    ship_to_residential_indicator = fields.Selection(
        [('Y', 'Y'),
         ('N', 'N')],
        string='ShipToResidentialIndicator',
        default='N',
    )
    shipping_charge = fields.Integer(
        string='ShippingCharge',
    )
    shipping_reference1 = fields.Char(
        string='ShippingReference1',
    )
    shipping_reference2 = fields.Char(
        string='ShippingReference2',
    )
    ship_to_first_name = fields.Char(
        related='move_id.picking_partner_id.name',
        string='ShipToFirstName',
        store=True,
        readonly=False,
    )
    ship_to_last_name = fields.Char(
        string='ShipToLastName',
    )
    ship_to_company = fields.Char(
        string='ShipToCompany',
    )
    ship_to_address1 = fields.Char(
        related='move_id.picking_partner_id.street',
        string='ShipToAddress1',
        store=True,
        readonly=False,
    )
    ship_to_address2 = fields.Char(
        related='move_id.picking_partner_id.street2',
        string='ShipToAddress2',
        store=True,
        readonly=False,
    )
    ship_to_city = fields.Char(
        related='move_id.picking_partner_id.city',
        string='ShipToCity',
        store=True,
        readonly=False,
    )
    ship_to_state = fields.Char(
        related='move_id.picking_partner_id.state_id.code',
        string='ShipToState',
        store=True,
        readonly=False,
    )
    ship_to_country_code = fields.Char(
        related='move_id.picking_partner_id.country_id.code',
        string='ShipToCountryCode',
        store=True,
        readonly=False,
    )
    ship_to_zip = fields.Char(
        related='move_id.picking_partner_id.zip',
        string='ShipToZip',
        store=True,
        readonly=False,
    )
    ship_to_phone = fields.Char(
        related='move_id.picking_partner_id.phone',
        string='ShipToPhone',
        store=True,
        readonly=False,
    )
    ship_to_customer_no = fields.Char(
        string='ShipToCustomerNo',
    )
    shipping_con_code = fields.Many2one(
        related='move_id.sale_line_id.order_id.delivery_consignee_code_id',
        string='ShippingConCode',
        store=True,
    )
    includes_kit_items = fields.Selection(
        [('Y', 'Y'),
         ('N', 'N')],
        string='IncludesKitItems',
        default='N',
    )
    sku = fields.Char(
        related='move_id.product_id.default_code',
        string='Sku',
        store=True,
    )
    quantity = fields.Float(
        related='move_id.product_qty',
        string='Qty',
        store=True,
    )
    description = fields.Char(
        related='move_id.product_id.product_tmpl_id.delivery_report_desc',
        string='Description',
        store=True,
        readonly=False,
    )
    po_line_no = fields.Char(
        string='PoLineNo',
    )
    item_no_ref = fields.Char(
        string='ItemNoRef',
    )
    original_price = fields.Integer(
        string='OriginalPrice',
    )
    price = fields.Integer(
        string='Price',
    )
    discounted_price = fields.Integer(
        string='DiscountedPrice',
    )
    sold_to_first_name = fields.Char(
        string='SoldToFirstName',
    )
    sold_to_last_name = fields.Char(
        string='SoldToLastName',
    )
    sold_to_company = fields.Char(
        string='SoldToCompany',
    )
    sold_to_address1 = fields.Char(
        string='SoldToAddress1',
    )
    sold_to_address2 = fields.Char(
        string='SoldToAddress2',
    )
    sold_to_city = fields.Char(
        string='SoldToCity',
    )
    sold_to_state = fields.Char(
        string='SoldToState',
    )
    sold_to_country_code = fields.Char(
        string='SoldToCountryCode',
    )
    sold_to_zip = fields.Char(
        string='SoldToZip',
    )
    sold_to_phone = fields.Char(
        string='SoldToPhone',
    )
    sold_to_customer_no = fields.Char(
        string='SoldToCustomerNo',
    )
    order_note = fields.Text(
        string='OrderNote',
    )
    gift_message = fields.Text(
        string='Gift Message',
    )
    lot = fields.Char(
        string='Lot',
    )

    @api.constrains('ship_to_last_name', 'ship_to_company',
                    'ship_to_address1', 'ship_to_address2', 'ship_to_city',
                    'ship_to_customer_no', 'description', 'po_line_no',
                    'item_no_ref', 'sold_to_first_name', 'sold_to_last_name',
                    'sold_to_company', 'sold_to_address1',
                    'sold_to_address2', 'sold_to_city', 'sold_to_customer_no',
                    'order_note', 'gift_message')
    def _validate_field_length(self):
        for rec in self:
            msg = _("%s should be at most %s digit(s).")

            if rec.ship_to_last_name and len(rec.ship_to_last_name) > 30:
                raise ValidationError(msg % (_("ShipToLastName"), "30"))
            if rec.ship_to_company and len(rec.ship_to_company) > 30:
                raise ValidationError(msg % (_("ShipToCompany"), "30"))
            if rec.ship_to_address1 and len(rec.ship_to_address1) > 30:
                raise ValidationError(msg % (_("ShipToAddress1"), "30"))
            if rec.ship_to_address2 and len(rec.ship_to_address2) > 30:
                raise ValidationError(msg % (_("ShipToAddress2"), "30"))
            if rec.ship_to_city and len(rec.ship_to_city) > 30:
                raise ValidationError(msg % (_("ShipToCity"), "30"))
            if rec.ship_to_customer_no and len(rec.ship_to_customer_no) > 20:
                raise ValidationError(msg % (_("ShipToCustomerNo"), "20"))

            if rec.description and len(rec.description) > 40:
                raise ValidationError(msg % (_("Description"), "40"))
            if rec.po_line_no and len(rec.po_line_no) > 3:
                raise ValidationError(msg % (_("PoLineNo"), "3"))
            if rec.item_no_ref and len(rec.item_no_ref) > 20:
                raise ValidationError(msg % (_("ItemNoRef"), "20"))

            if rec.sold_to_first_name and len(rec.sold_to_first_name) > 30:
                raise ValidationError(msg % (_("SoldToFirstName"), "30"))
            if rec.sold_to_last_name and len(rec.sold_to_last_name) > 30:
                raise ValidationError(msg % (_("SoldToLastName"), "30"))
            if rec.sold_to_company and len(rec.sold_to_company) > 30:
                raise ValidationError(msg % (_("SoldToCompany"), "30"))
            if rec.sold_to_address1 and len(rec.sold_to_address1) > 30:
                raise ValidationError(msg % (_("SoldToAddress1"), "30"))
            if rec.sold_to_address2 and len(rec.sold_to_address2) > 30:
                raise ValidationError(msg % (_("SoldToAddress2"), "30"))
            if rec.sold_to_city and len(rec.sold_to_city) > 30:
                raise ValidationError(msg % (_("SoldToCity"), "30"))
            if rec.sold_to_customer_no and len(rec.sold_to_customer_no) > 20:
                raise ValidationError(msg % (_("SoldToCustomerNo"), "20"))

            if rec.order_note and len(rec.order_note) > 320:
                raise ValidationError(msg % (_("OrderNote"), "320"))
            if rec.gift_message and len(rec.gift_message) > 250:
                raise ValidationError(msg % (_("Gift Message"), "250"))

    @api.constrains('ship_to_state', 'ship_to_country_code',
                    'sold_to_state', 'sold_to_country_code')
    def _validate_country_state(self):
        for rec in self:
            msg = _("Invalid %s.")
            if rec.sold_to_state:
                state = self.env['res.country.state'].search([
                    ('code', '=', rec.sold_to_state)
                ])
                if not state:
                    raise ValidationError(msg % (_("SoldToState")))
            if rec.ship_to_state:
                state = self.env['res.country.state'].search([
                    ('code', '=', rec.ship_to_state)
                ])
                if not state:
                    raise ValidationError(msg % (_("ShipToState")))
            if rec.sold_to_country_code:
                country = self.env['res.country'].search([
                    ('code', '=', rec.sold_to_country_code)
                ])
                if not country:
                    raise ValidationError(msg % (_("SoldToCountryCode")))
            if rec.ship_to_country_code:
                country = self.env['res.country'].search([
                    ('code', '=', rec.ship_to_country_code)
                ])
                if not country:
                    raise ValidationError(msg % (_("ShipToCountryCode")))

    @api.multi
    @api.depends('carrier_id')
    def _get_shipping_use_carrier_acct(self):
        for line in self:
            if line.carrier_id and line.move_id.picking_partner_id.delivery_carrier_id and \
                    line.carrier_id == line.move_id.picking_partner_id.delivery_carrier_id:
                line.shipping_use_carrier_acct = \
                    line.move_id.picking_partner_id.delivery_carrier_account_num
            else:
                line.shipping_use_carrier_acct = False

    @api.multi
    def write(self, vals):
        res = super(stockOutgoingShipmentReport, self).write(vals)
        if 'ship_to_first_name' in vals:
            for rec in self:
                if rec.ship_to_first_name and len(rec.ship_to_first_name) > 30:
                    raise ValidationError(
                        _("%s should be at most %s digit(s).") % (_("ShipToFirstName"), "30"))
        return res
