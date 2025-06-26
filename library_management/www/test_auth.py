import frappe
from frappe import _

def get_context(context):
    return {
        "user": frappe.session.user,
        "message": f"Hello {frappe.session.user}!"
    }
