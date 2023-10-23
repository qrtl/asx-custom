This module restricts the updating of standard price for products to only those users
in the group_system group.

Background
~~~~~~~~~~

For products that use either the FIFO or Average Cost costing method, users might misunderstand
that the "standard_price" field represents the unit cost calculated by Odoo based on the current
stock valuation, rather than the product cost/price that will be applied when creating a purchase order.
There is a possibility that users may update the "standard_price" with the product price obtained from
the vendor's pricelist. If this occurs, the stock valuation of the product will be unexpectedly updated,
and the value will not accurately reflect the actual valuation.
