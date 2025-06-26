# Copyright (c) 2025, tharun and contributors
# For license information, please see license.txt

# import frappe


# def execute(filters=None):
# 	columns, data = [], []
# 	return columns, data


# medical_practice_report.py

import frappe
from frappe import _

def execute(filters=None):
    columns = [
        {
            "label": _("Patient Name"),
            "fieldname": "patient_name",
            "fieldtype": "Data",
            "width": 150
        },
        {
            "label": _("Age"),
            "fieldname": "age",
            "fieldtype": "Int",
            "width": 80
        },
        {
            "label": _("Disease"),
            "fieldname": "disease",
            "fieldtype": "Data",
            "width": 100
        },
        {
            "label": _("Medicines"),
            "fieldname": "medicines",
            "fieldtype": "Data",
            "width": 200
        }
    ]

    data = frappe.db.get_all(
        'Medical Practice',
        fields=['patient_name', 'age', 'medicines'],
        order_by='modified desc'
    )

    return columns, data
