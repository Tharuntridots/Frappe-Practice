# Copyright (c) 2025, tharun and contributors
# For license information, please see license.txt

import frappe
from frappe.website.website_generator import WebsiteGenerator
from frappe.model.document import Document
from frappe import _

class SalesTracker(Document):
    pass
    # def before_save(self):
    #     # Create and insert a new Sales Tracker document
    #     doc = frappe.get_doc({
    #         'doctype': 'Sales Tracker',
    #         'customer_name': 'John Doe',
    #         'data': 'Test Data',
    #         'total_amount': 5000,
    #         'total_items': 3
    #     })
    #     frappe.msgprint(f"Inserted: {doc.name}")

	# def before_save(self):
	# 	doc= frappe.get_all('Sales Tracker', fields= ['name', 'customer_name'])

	# 	for d in doc:
	# 		frappe.msgprint(f"{d.name}= {d.customer_name}")


	# def validate(self):
	# 	if self.total_amount == 0:
	# 		self.db_set('total_amount', 5)
	# 		frappe.msgprint("Set in db")

    # def before_save(self):
    #     docs = frappe.db.get_list('Sales Tracker', fields=['name', 'customer_name'])
    #     for doc in docs:
    #         frappe.msgprint(f"Name: {doc['name']}, Customer: {doc['customer_name']}")

# @frappe.whitelist()
# def get_total_items(docname):
#     doc = frappe.get_doc("Sales Tracker", docname)
#     return len(doc.sales_items)

# @frappe.whitelist()
# def create_sales_tracker(customer_name, amount):
#     doc = frappe.new_doc("Sales Tracker")
#     doc.customer_name = customer_name
#     doc.total_amount = amount
#     doc.insert()
#     return doc.name 

# @frappe.whitelist()
# def get_filed_link_details(link_name):
#     doc = frappe.get_doc("Field Setup", link_name)
#     return {
#         "name": doc.name1,
#         "age": doc.age
#     }


# @frappe.whitelist()
# def get_sales_items(docname):
#     doc = frappe.get_doc("Sales Tracker", docname)
#     items = []
#     for row in doc.sales_items:
#         items.append({
#             "item_name": row.item_name,
#             "description": row.description,
#             "quantity": row.quantity,
#             "rate": row.rate,
#             "amount": row.amount,
#             "status": row.status
#         })
#     return items    

# @frappe.whitelist()
# def get_filtered_docs():
#     docs = frappe.db.get_list(
#         "Sales Tracker",
#         filters={"customer_name": "Internal Customer"},
#         fields = ["name", "total_amount"]
#     )

#     for d in docs:
#         frappe.msgprint(f"{d.name}- {d.total_amount} ")