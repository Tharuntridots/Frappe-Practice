import frappe

def get_context(context):
    context.projects = frappe.get_all("Projects", fields=["name", "title", "description"])
    return context
