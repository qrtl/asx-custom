# Copyright 2019 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import json

from odoo.addons.web.controllers.main import CSVExport, ExcelExport


class CSVExportInherit(CSVExport):

    # Override the base() method which is used to gather fields' values in the
    # export CSV.
    def base(self, data, token):
        params = json.loads(data)
        # When the stock.outgoing.shipment.report model is selected, remove
        # the first element in the fields list which is the External ID by
        # default.
        if params["model"] == "stock.outgoing.shipment.report":
            params["fields"].pop(0)
            data = json.dumps(params)
        return super(CSVExportInherit, self).base(data, token)


class ExcelExportInherit(ExcelExport):

    # Override the base() method which is used to gather fields' values in the
    # export Excel.
    def base(self, data, token):
        params = json.loads(data)
        # When the stock.outgoing.shipment.report model is selected, remove
        # the first element in the fields list which is the External ID by
        # default.
        if params["model"] == "stock.outgoing.shipment.report":
            params["fields"].pop(0)
            data = json.dumps(params)
        return super(ExcelExportInherit, self).base(data, token)
