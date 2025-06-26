# Copyright (c) 2025, tharun and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.model.naming import make_autoname


class Members(Document):

	def autoname(self):
		self.name = make_autoname(f"{'ME'}.####")

	# def before_save(self):
	# 	doc= frappe.get_doc('Members', 'ME0001')
	# 	self.age = doc.age
	
	def add_document(self):
		doc = frappe.get_doc({
			'doctype': 'Members',
			'title':'rome',
			'name1':'rome'
		})
		doc.insert()
		frappe.msgprint("document added successfully")


	def add_document2(self):
		doc = frappe.new_doc('Members')
		doc.name1='prassana'
		doc.insert()
		frappe.msgprint("document2 added successfully")

	
	def last_document(self):
		doc = frappe.get_last_doc('Members', filters={"docstatus": 2})
		frappe.msgprint(f"last document {doc.name}")


	def delete_document(self):
		doc = frappe.delete_doc('Members', 'ME0008')   ##delete
		frappe.msgprint("delete successfully")


	def rename_document(self):
		doc = frappe.rename_doc('Members', 'ME0005', "hiii")  #rename
		frappe.msgprint("rename successfully")


	def meta_data(self):
		meta = frappe.get_meta('Members')
		if meta.has_field('name1'):
			frappe.msgprint("status is present")
		else:
			frappe.msgprint("status is not present")
		
		field_details = []
		for field in meta.fields:
			field_details.append(f"{field.fieldname} ({field.fieldtype})")
		frappe.msgprint("Fields in Members doctype:" + "\n".join(field_details))
		

	def new_insert(self):
		doc = frappe.new_doc('Members')
		# doc.name1 = 'sam curren4'
		doc.age = 22

		doc.insert(
			ignore_permissions = True,
			ignore_links = True,
			ignore_if_duplicate = True,
			ignore_mandatory = True
		)

	def new_save(self):
		doc = frappe.new_doc("Members")
		doc.name1='chandrru'
		doc.age=47

		doc.save(
			ignore_permissions = True,
			ignore_version = True
		)


	def new_delete(self):
		doc = frappe.get_doc("Members", "ME0013")
		doc.delete()


	def validate(self):
		old_doc = self.get_doc_before_save()
		if old_doc:
			if old_doc.age != self.age:  ##self.has_value_changed("age"):
				frappe.msgprint(f"age {old_doc.age} is change to {self.age}")
			else:
				frappe.msgprint("age is same ")
		else:
			frappe.msgprint("this is new document")

	def reload_document(self):
		doc = frappe.get_meta("Members")
		doc.reload()

	def check_permissions(self, permtype='write'):
		doc = frappe.get_doc('Members', self.name)
		if doc.check_permissions('write'):
			frappe.msgprint("write permission assible for the user")
		else:
			frappe.msgprint("not assible")
	
	def title_document(self):
		doc = frappe.get_doc('Members', self.name)
		title = doc.get_title()
		frappe.msgprint(f"{title} is the title of the document field")

	def data_modify(self):
		doc= frappe.get_doc('Members', self.name)
		doc.db_set('age', 888, notify=True)
		frappe.msgprint("data modified")

	def url_document(self):
		doc = frappe.get_doc('Members', self.name)
		url = doc.get_url()
		frappe.msgprint(f"{url} off the document")

	def comment_document(self):
		doc = frappe.get_doc('Members', self.name)
		doc.add_comment('Edit', 'This is my dummy comment')

	def seen_document(self):
		doc = frappe.get_doc('Members', self.name)
		doc.add_seen('kishore@example.com')
		frappe.msgprint("seen the document")
	
	def view_document(self):
		doc = frappe.get_doc('Members', self.name)
		doc.add_viewed()
		frappe.msgprint("view added")

	def tag_document(self):
		doc= frappe.get_doc('Members', self.name)
		doc.add_tag('come_back_indian')
		frappe.msgprint("tag added")
	
	def tag_document_get(self):
		doc = frappe.get_doc('Members', self.name)
		tags = doc.get_tags()
		frappe.msgprint(f"Tags: {', '.join(tags)}")

	def db_insert_document(self):
		doc = frappe.new_doc('Members')
		doc.name1 = "zzz"
		doc.age= 86
		doc.db_insert()
		frappe.message("insert on db")

	def db_update_document(self):
		doc = frappe.get_doc('Members', self.name)
		doc.age=46
		doc.db_update()
		frappe.msgprint("updated on db")

	def on_submit(self):
		# self.add_document()
		self.add_document2()

	def on_update_after_submit(self):
		# self.last_document()
		# self.delete_document()
		# self.rename_document()
		# self.meta_data()
		# self.new_insert()
		# self.new_save()
		# self.new_delete()
		# self.reload_document()
		# self.check_permissions()
		# self.title_document()
		# self.data_modify()
		# self.url_document()
		# self.comment_document()
		# self.seen_document()
		# self.view_document()
		# self.tag_document()
		# self.tag_document_get()
		# self.run_method('tag_document')
		# self.db_insert_document()
		self.db_update_document()

	
		



