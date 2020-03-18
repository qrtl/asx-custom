# Copyright 2019 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class StockIncomingShipmentReport(models.TransientModel):
    _name = "stock.incoming.shipment.report"

    move_id = fields.Many2one("stock.move", string="Stock Move", readonly=True,)
    client_code = fields.Char(string="Client Code",)
    tracking_pro_num = fields.Char(string="Tracking / PRO Number",)
    seal = fields.Char(string="Seal",)
    anticipated_arrival_date = fields.Char(
        string="Anticipated Arrival Date", compute="_compute_date_fields", store=True,
    )
    anticipated_arrival_date_edit = fields.Datetime(
        string="Anticipated Arrival Date (Not for Export)",
    )
    client_receipt_ref_num = fields.Char(
        related="move_id.picking_id.name",
        string="Client Receipt Reference Number",
        store=True,
    )
    client_vendor_po_num = fields.Char(
        related="move_id.purchase_line_id.order_id.name",
        string="Client/Vendor PO Number",
        store=True,
    )
    carrier_code = fields.Char(string="Carrier Code",)
    load_type = fields.Char(string="Load Type",)
    part_num = fields.Char(
        related="move_id.product_id.default_code", string="Part Number", store=True,
    )
    lot_num = fields.Char(string="Lot Number",)
    expiration_date = fields.Char(
        string="Expiration Date", compute="_compute_date_fields", store=True,
    )
    expiration_date_edit = fields.Date(string="Expiration Date (Not for Export)",)
    quantity_expected = fields.Float(
        related="move_id.product_uom_qty", string="Quantity Expected (EA)", store=True,
    )
    po_notes = fields.Char(string="PO Notes",)

    @api.multi
    @api.depends("expiration_date_edit", "anticipated_arrival_date_edit")
    def _compute_date_fields(self):
        for line in self:
            date_format = "%m/%d/%Y"
            if line.expiration_date_edit:
                line.expiration_date = line.expiration_date_edit.strftime(date_format)
            if line.anticipated_arrival_date_edit:
                line.anticipated_arrival_date = line.anticipated_arrival_date_edit.strftime(
                    date_format
                )
