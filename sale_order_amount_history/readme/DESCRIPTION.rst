This module does the following:

* Adds the Sales Order Amount History model (sale.order.amount.history).
* Creates Sales Order Amount History records for certain changes in the sales order.

Changes that create history
---------------------------

Changes that create a Sales Order Amount History record:

* State change from 'Quotation' / 'Quotation Sent' to 'Sales Order' (History Type 'Add')
* State change from 'Sales Order' to 'Canceled' (History Type 'Delete')
* Amount change when sales order is in 'Sales Order' state ('History Type 'Change')

Exception: Sales orders for the group companies (which should be indicated by the
assigned fiscal position) should not create history records.

The design of Order Count
-------------------------

When a history record is created, Order Count is added (+1) when the order amount
changes from zero to something else, and deducted (-1) when the order amount changes
to zero.  Below are the patterns.

* Sales order with non-zero amount is confirmed.  -> 1
* Sales order with zero amount is confirmed.  -> 0
* Amount is changed from non-zero to non-zero for a confirmed sales order.  -> 0
* Amount is changed from zero to non-zero for a confirmed sales order.  -> 1
* Amount is changed from non-zero to zero for a confirmed sales order.  -> -1
* Conirmed sales order with non-zero amount is cancelled.  -> -1
* Conirmed sales order with zero amount is cancelled.  -> 0

The date to capture the exchange rate for
-----------------------------------------

The exchange rate for company currency amount conversion is based on the Confirmation
Date of the sales order (instead of the date of the history record).  This is to avoid
the confusion of having some unwanted balance when a confirmed foreign currency order
is cancelled in the next month, for example.
