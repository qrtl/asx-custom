This module is a modified version of OCA's sale_tier_validation module.

The module is intended to be used to restrict the quotation print function while the quotation has yet to be approved by a designated person.

This module does the following:

#. Hides the buttons on sales order form which let users print the quotation, when the quotation is still not approved (view adjustments).
#. Blocks the status change from 'draft' to 'sent'/'sale' when the quotation is still not approved.

The Point 1 does not remove the drop-down options from the 'Print' button which is enabled through the ir.actions.report records.
To practically disable these print options to non-privileged users, we assign 'Administration / Settings' group to these records.
