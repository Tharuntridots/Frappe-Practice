# Copyright (c) 2025, tharun and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class CustomerFeedback(Document):
	pass

# @frappe.whitelist()
# def get_feedback_list():
#     query = frappe.qb.get_query("Customer Feedback", fields=["name1", "email", "feedback"])
#     feedbacks = query.run(as_dict=True)
#     return feedbacks

# @frappe.whitelist()
# def get_feedback_list():
#     query = frappe.qb.get_query("Customer Feedback", fields=["*"])
#     feedbacks = query.run(as_dict=True)
#     return feedbacks

@frappe.whitelist()
def get_feedback_list():
    query = frappe.qb.get_query("Customer Feedback", fields=["name1", "email", "feedback", "status"], 
		filters = {"docstatus": 0}
	)
    feedbacks = query.run(as_dict=True)
    return feedbacks

@frappe.whitelist()
def get_feedback_list2():
	query = frappe.qb.get_query('Customer Feedback', fields=["status", "name"], group_by = "status")
	data = query.run(as_dict= True)
	return data

@frappe.whitelist()
def get_feedback_list3():
	query = frappe.qb.get_query('Customer Feedback', fields=["status", "COUNT(name)"], group_by = "status")
	data = query.run(as_dict= True)
	return data

@frappe.whitelist()
def get_data():
    data = frappe.db.get_all("Customer Feedback", fields=["name", "status"])
    return data


