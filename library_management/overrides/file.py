# app/overrides/file.py

import frappe

def before_write(file_doc=None):
    print("🟡 before_write hook triggered")
    frappe.msgprint("Hook: before_write called")

def write_file(file_doc=None):
    print("🟢 write_file hook triggered (override default save)")
    frappe.msgprint("Hook: write_file called")
    
    # Optional: Example custom logic (still saving locally)
    if file_doc:
        file_doc.save_to_files()

def delete_file(file_doc=None):
    print("🔴 delete_file hook triggered")
    frappe.msgprint("Hook: delete_file called")

    # Optional: custom deletion logic
    if file_doc and file_doc.file_url:
        frappe.delete_file(file_doc.file_url)
