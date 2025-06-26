# Copyright (c) 2025, tharun and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Project(Document):
	def get_context(context):
		project_name = frappe.form_dict.name
		try:
			project = frappe.get_doc("Project", project_name)
			context.project = project
		except frappe.DoesNotExistError:
			context.project = None
