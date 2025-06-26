# Copyright (c) 2025, tharun and contributors
# For license information, please see license.txt

import frappe
from frappe.website.website_generator import WebsiteGenerator


class Client_Scripts(WebsiteGenerator):
	pass

@frappe.whitelist()
def frappe_call(msg):
	import time
	time.sleep(3)
	frappe.msgprint(msg)
	# return "Hi this msg from Frappe_call"