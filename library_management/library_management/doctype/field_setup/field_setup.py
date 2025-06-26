# Copyright (c) 2025, tharun and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class FieldSetup(Document):
    def before_save(self):
        frappe.msgprint("Original before_save in FieldSetup")

@frappe.whitelist()
def get_enabled_fieldsetups():
    frappe.msgprint("🔵 This is the ORIGINAL method.")
    return "Original Response"
