# Copyright (c) 2025, tharun and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class NoteBook(Document):
	def validate(self):
		if self.brand == "Dairy":
			self.pencil = ""
			self.sketch = ""
		