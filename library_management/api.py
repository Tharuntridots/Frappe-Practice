# import frappe
# import google_auth_oauthlib.flow

# # Dummy values – won't work for real auth, but enough for UI testing
# CLIENT_ID = "dummy-client-id.apps.googleusercontent.com"
# CLIENT_SECRET = "dummy-client-secret"
# REDIRECT_URI = "http://localhost:8001/api/method/library_management.api.google_auth_callback"


# @frappe.whitelist()
# def get_google_auth_url():
#     flow = google_auth_oauthlib.flow.Flow.from_client_config({
#         "web": {
#             "client_id": CLIENT_ID,
#             "client_secret": CLIENT_SECRET,
#             "redirect_uris": [REDIRECT_URI],
#             "auth_uri": "https://accounts.google.com/o/oauth2/auth",
#             "token_uri": "https://oauth2.googleapis.com/token"
#         }
#     }, scopes=["https://www.googleapis.com/auth/drive.file"])

#     flow.redirect_uri = REDIRECT_URI
#     auth_url, _ = flow.authorization_url(access_type='offline', include_granted_scopes='true')
#     return auth_url

# @frappe.whitelist(allow_guest=True)
# def google_auth_callback():
#     return "✅ Dummy callback reached. Integration simulated successfully."


# import frappe
# from frappe.utils import now_datetime

# @frappe.whitelist()
# def process_biometric(employee):
#     # Simulate match and insert a record
#     doc = frappe.get_doc({
#         "doctype": "Biometric Attendance",
#         "employee_name": employee,
#         "status": "Check In",
#         "timestamp": now_datetime()
#     })
#     doc.insert()
#     return "success"


import frappe
from frappe.utils.pdf import get_pdf
from frappe import _


@frappe.whitelist(allow_guest=True)
def generate_custom_pdf():
    # Pass any dynamic data here if needed
    context = {
        "title": "My Custom PDF Title"
    }

    # Render the template from your www folder
    html = frappe.render_template("library_management.templates.my_custom_page.html", context)

    # Generate PDF bytes from HTML
    pdf_bytes = get_pdf(html)

    # Prepare the HTTP response to download PDF
    frappe.local.response.filename = "custom_page.pdf"
    frappe.local.response.filecontent = pdf_bytes
    frappe.local.response.type = "pdf"


@frappe.whitelist()
def get_my_notebooks():
    user = frappe.session.user
    notebooks = frappe.db.get_list("Note Book", fields=["name", "owner"], debug=1)  # Removed 'created_by'
    return notebooks

import frappe

@frappe.whitelist()
def get_current_user_roles():
    return frappe.get_roles(frappe.session.user)


import frappe
from frappe import _

@frappe.whitelist()
def get_patient_data():
    data = frappe.db.get_list("Patient Visit", fields=["name", "patient_id"], limit_page_length=10)
    return data
