# Copyright (c) 2025, tharun and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class CompanyDetails(Document):
	pass

@frappe.whitelist()
def calculate_total_amount_form(amount, quantity):
    try:
        amount = float(amount)
        quantity = int(quantity)
        total = amount * quantity
        return total
    except Exception as e:
        frappe.throw(f"Error calculating total: {str(e)}")


import frappe
from frappe.model.document import Document

class CompanyDetails(Document):
    def on_submit(self):
        # This is called when the document is submitted
        frappe.publish_realtime('company_details', {
            'docname': self.name,
            'company_name': self.company_name,
            'status': self.status
        })


@frappe.whitelist()
def has_price_changed(docname):
    doc = frappe.get_doc("Company Details", docname)
    old_amount = doc.total_amount

    if old_amount != 2400:
        doc.db_set('total_amount', 2400)
        return f"Total Amount changed from {old_amount} to 2400"
    else:
        return "Total Amount was already 2400"



