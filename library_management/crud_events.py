# your_app/crud_events.py

import frappe

def after_insert_all(doc, method=None):
    frappe.msgprint(f"🌍 A new document was inserted in DocType: {doc.doctype}, Name: {doc.name}")

def after_insert_fieldsetup(doc, method=None):
    frappe.msgprint(f"✅ Field Setup '{doc.name}' was inserted!")

def before_save_fieldsetup(doc, method=None):
    frappe.msgprint("✍️ Saving Field Setup. Custom logic can go here.")
