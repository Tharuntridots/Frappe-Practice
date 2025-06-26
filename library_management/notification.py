def get_notification_config():
    return {
        "for_doctype": {
            "Library Member": {"enabled": 1},  # Show count of all enabled members
            "Library Transaction": {"status": "Issued"},  # Show count of books issued
        },
        "for_module_doctypes": {
            "Library": "Library Management"
        },
        "for_module": {
            "Library Management": "library_management.notifications.get_library_notifications"
        }
    }

# Optional: show a custom count for the whole module
def get_library_notifications():
    from frappe.utils import cint
    count = frappe.db.count("Library Transaction", {"status": "Overdue"})
    return count
