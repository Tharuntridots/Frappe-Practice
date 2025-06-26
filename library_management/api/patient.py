import frappe
from frappe import _

@frappe.whitelist()
def get_patient_data():
    # Example: Fetch name, patient_id from Patient Visit DocType
    data = frappe.db.get_list("Patient Visit", fields=["name", "patient_id"], limit_page_length=10)
    return data