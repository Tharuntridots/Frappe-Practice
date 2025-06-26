# File: apps/library_management/library_management/utils.py

import frappe

def get_fullname(user):
    first_name, last_name = frappe.db.get_value("User", user, ["first_name", "last_name"])
    return f"{first_name} {last_name}"

def format_currency(value, currency):
    return f"{currency} {value:,.2f}"

