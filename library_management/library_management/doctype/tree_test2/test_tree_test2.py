# Copyright (c) 2025, tharun and Contributors
# See license.txt

# import frappe
from frappe.tests.utils import FrappeTestCase


class TestTree_test2(FrappeTestCase):
    

	
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
