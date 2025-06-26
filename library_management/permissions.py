import frappe

def notebook_query(user):
    if not user:
        user = frappe.session.user
    return """(`tabNote Book`.owner = {user})""".format(user=frappe.db.escape(user))


import frappe

def notebook_has_permission(doc, user):
    # Only allow Library Member role
    if "Library Member" in frappe.get_roles(user):
        # Only allow this one specific document
        if doc.name == "1lm9sf2f9b":
            return True
    return False

