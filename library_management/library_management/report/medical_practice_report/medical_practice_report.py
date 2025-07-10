# Copyright (c) 2025, tharun and contributors
# For license information, please see license.txt

# import frappe


# def execute(filters=None):
# 	columns, data = [], []
# 	return columns, data


# medical_practice_report.py

# import frappe
# from frappe import _

# def execute(filters=None):
#     columns = [
#         {
#             "label": _("Patient Name"),
#             "fieldname": "patient_name",
#             "fieldtype": "Data",
#             "width": 150
#         },
#         {
#             "label": _("Age"),
#             "fieldname": "age",
#             "fieldtype": "Int",
#             "width": 80
#         },
#         {
#             "label": _("Disease"),
#             "fieldname": "disease",
#             "fieldtype": "Data",
#             "width": 100
#         },
#         {
#             "label": _("Medicines"),
#             "fieldname": "medicines",
#             "fieldtype": "Data",
#             "width": 200
#         }
#     ]

#     data = frappe.db.get_all(
#         'Medical Practice',
#         fields=['patient_name', 'age','disease', 'medicines'],
#         order_by='modified desc'
#     )

#     return columns, data



import frappe
from frappe import _ 

def execute(filters = None):
    data = frappe.db.sql("""
        SELECT disease, COUNT(*) as count
        FROM `tabMedical Practice`
        GROUP BY disease
    """, as_dict= True)

    columns = [
        {
            "label": _("Disease"),
            "fieldname": "disease",
            "fieldtype": "Data",
            "width": 200
        },
        {
            "label": _("Count"),
            "fieldname": "count",
            "fieldtype": "Int",
            "width": 120
        }
    ]

    chart = {
        "data"  : {
            "labels": [row.disease for row in data],
            "datasets": [
                {
                    "name" : "Disease Count",
                    "values" : [row.count for row in data]
                }
                 
            ]
        }, 
        "type" : "pie",
        "height": 300
    }

    return columns, data, None, chart