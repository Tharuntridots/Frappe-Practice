import frappe

def successful_login(login_manager):
    user = frappe.session.user
    frappe.msgprint(f"🎉 Welcome back {user}!")

    # If the logged-in user is gokul@example.com
    if user == "gokul@example.com":
        # Redirect to Library Member Doctype
        frappe.local.response["type"] = "redirect"
        frappe.local.response["location"] = "/app/library-member"

def allocate_free_credits(login_manager):
    user = frappe.session.user
    frappe.logger().info(f"✅ Session created for {user}, giving free credits.")

def clear_user_cache(login_manager):
    user = frappe.session.user
    frappe.logger().info(f"🚪 User {user} logged out. Clearing cache.")

def validate_custom_jwt():
    token = frappe.request.headers.get("Authorization")
    if token and token.startswith("Bearer "):
        jwt_token = token[7:]

        if jwt_token == "my-secret-token":
            frappe.set_user("sam@gmail.com")  # Replace with actual user email
            frappe.logger().info("✅ Authenticated as sam@gmail.com")
        else:
            frappe.logger().warning("❌ Invalid token. Continuing as Guest.")
    else:
        frappe.logger().info("ℹ️ No Authorization header. Treated as Guest.")

# your_app/overrides/field_setup_override.py

import frappe
from library_management.library_management.doctype.field_setup.field_setup import FieldSetup

class CustomFieldSetup(FieldSetup):
    def before_save(self):
        frappe.msgprint("Custom before_save in CustomFieldSetup")
        # super().before_save()


@frappe.whitelist()
def custom_get_enabled_fieldsetups():
    frappe.msgprint("🟢 This is the OVERRIDDEN method.")
    return "Overridden Response"
