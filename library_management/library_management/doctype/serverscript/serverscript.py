# Copyright (c) 2025, tharun and contributors
# For license information, please see license.txt

import frappe
from frappe import _
from frappe.website.website_generator import WebsiteGenerator
# from frappe import msgprint


class ServerScript(WebsiteGenerator):

	# def validate(self):
	# 	self.get_list()
	@frappe.whitelist()
	def frm_call(self,msg):
		import time
		time.sleep(5)
		# frappe.msgprint(msg)

		self.last_name = "prasana"
		# return  "Hi this msg frm frm_call"

		# dbc_count = frappe.db.count('Client_Scripts', filters={"docstatus": 0})
		# frappe.msgprint(f"the count is {dbc_count}")

		# if frappe.db.exists('Client_Scripts', 'PM-0007'):
		# 	frappe.msgprint("present")
		# else:
		# 	frappe.msgprint("Not Present")

		# for row in self.get("family_members"):
		# 	frappe.msgprint(_("{0} the family member name is `{1}` and age is `{2}` ").format(row.idx, row.name1, row.relation))

		# self.get_value()
		# self.set_value()
		# self.sql()
		# self.sql_document()
		# self.get_document()


	# def get_document(self):
	# 	doc = frappe.get_doc('Client_Scripts', self.client_side)
	# 	frappe.msgprint(_("the first name is {0} and age is {1}").format(doc.first_name, doc.age))


	# 	for row in doc.get("family_members"):
	# 		frappe.msgprint(_("{0} the family member name is `{1}` and age is `{2}` ").format(row.idx, row.name1, row.relation))


	# def new_document(self):
	# 	doc = frappe.new_doc('Client_Scripts')
	# 	doc.first_name = "AArun"
	# 	doc.last_name = "kumar"
	# 	doc.age = 34
	# 	doc.append('family_members', {"name1": "prabhu",
	# 									"age":12,
	# 									"relation" : "chithapa"
	# 									})

	# 	doc.insert()

	# # def get_list(self):
	# 	doc = frappe.db.get_list('Client_Scripts',
	# 			filetrs={
	# 				'docstatus' : 0
	# 			},
	# 			fields=['first_name', 'age']
	# 	for d in doc:
	# 		frapppe.msgprint(_(The parent name is {0} and age is {1}).format(d.first_name, d.age))

	# 	)


	# def sql_document(self):
	# 	data = frappe.db.sql("""
	# 				SELECT 
	# 					first_name,
	# 					age
	# 				FROM
	# 					`tabClient_Scripts`
	# 				WHERE
	# 					enable =1
			
	# 		""", as_dict = 1)
	# 	frappe.msgprint(f"The name is {data[0]} and age is {data[1]}")
		# if data:
		# 	for row in data:
		# 		name = row.get("first_name")
		# 		age = row.get("age")
		# 		frappe.msgprint(f"The name is {name} and age is {age}")
		# else:
		# 	frappe.msgprint("No records found with enable = 1.")
	
	# def get_value(self):
	# 	result = frappe.db.get_value('Client_Scripts', 'PM-0003', ['first_name', 'age'])
		
	# 	if result:
	# 		first_name, age = result
	# 		frappe.msgprint(_("The first parent is {0} and age is {1}").format(first_name, age))
	# 	else:
	# 		frappe.msgprint("No record found for Client_Script with name PM-0003")


	# def set_value(self):

	# 	frappe.db.set_value('Client_Scripts', 'PM-0003', 'age', 25)

	# 	result = frappe.db.get_value('Client_Scripts', 'PM-0003', ['first_name', 'age'])
		
	# 	if result:
	# 		first_name, age = result
	# 		frappe.msgprint(_("The first parent is {0} and age is {1}").format(first_name, age))
	# 	else:
	# 		frappe.msgprint("No record found for Client_Script with name PM-0003")

		
	
