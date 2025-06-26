# Copyright (c) 2025, tharun and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.model.naming import make_autoname  

class Controller(Document):

    def before_insert(self):
        frappe.msgprint(
            msg="this is before_insert"
        )
              
    def before_naming(self):
        frappe.msgprint(
            msg="this is before_naming"
        )

    def autoname(self):
        self.name = make_autoname(f"{'TASK'}.###")
    
    def before_validate(self):
        if "@gmail.com" in self.email:
            frappe.msgprint(
                msg ="Valid email address"
            )
        else:
            frappe.throw("not a valid email")

    def validate(self):
        if self.age <= 18:
            frappe.throw("age is less then 18")

    def before_save(self):
        frappe.msgprint("text is changed")
        self.text = "this is dummy text"

    def before_submit(self):
        frappe.msgprint("the document is going to submit")

    def before_cancel(self):
        frappe.msgprint("this data is going to cancel")
    
    def before_update_after_submit(self):
        frappe.msgprint("running before_update_after_submit")
        self.text = "this doc is submitted"

    def on_update(self):
        self.text = "this is on update function"

    def on_submit(self):
        self.time = "00.00"

    def on_cancel(self):
        frappe.msgprint("bye bye")

    def on_update_after_submit(self):
        frappe.msgprint("update on submitted document")

    def on_change(self):
        self.time = "1.00"