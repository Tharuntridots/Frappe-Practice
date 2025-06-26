# Copyright (c) 2025, tharun and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Tree_test2(Document):

    def child_document(self):
       children = frappe.get_all(
        'Tree_test2', filters = {'parent_tree_test2' : self.old_parent or self.name},
        fields = ['name', 'name1', 'role']
       )

       for child in children:
        frappe.msgprint(f"Child Name: {child.name}, Role:{child.role}")
    
    def parent_document(self):
        if self.parent_tree_test2:
            parent = frappe.get_doc('Tree_test2', self.parent_tree_test2)
            frappe.msgprint(f"Parent Name: {parent.name}, Role: {parent.role}")
        else:
            frappe.msgprint("No Parent found for this role")


    def on_update_after_submit(self):
        # self.child_document()
        self.parent_document()
        