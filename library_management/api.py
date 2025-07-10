import frappe
import random

@frappe.whitelist()
def publish_disease_data():
    # You can replace this with real query if needed
    fever_count = random.randint(0, 10)
    cold_count = random.randint(0, 10)

    data = {
        'label': frappe.utils.nowtime(),  # x-axis label
        'points': [fever_count, cold_count]  # order matches chart datasets
    }

    frappe.publish_realtime('disease_realtime_event', data)

import frappe
from frappe import _

@frappe.whitelist()
def get_children(parent=None):
    if not parent or parent == "All Tree_test2":
        parent = ""
    return frappe.get_list('Tree_test2', 
        fields=["name as value", "is_group as expandable"],
        filters={"parent_tree_test2": parent}
    )

@frappe.whitelist()
def add_node(name1, parent=None, is_group=0):
    doc = frappe.get_doc({
        "doctype": "Tree_test2",
        "name1": name1,
        "parent_tree_test2": parent,
        "is_group": is_group
    })
    doc.insert()
    return doc
