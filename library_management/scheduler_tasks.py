# your_app/scheduler_tasks.py

import frappe

def hourly_notification():
    # Send a notification to Administrator (or replace with any user)
    user = "Administrator"

    frappe.get_doc({
        "doctype": "Notification Log",
        "subject": "⏰ Hourly Reminder",
        "email_content": "This is your hourly notification from scheduler.",
        "for_user": user
    }).insert(ignore_permissions=True)

    frappe.logger().info("📢 Notification sent to " + user)


def hourly_notification_email():
    frappe.sendmail(
        recipients=["sam@gmail.com.com"],
        subject="⏰ Hourly Notification",
        message="This is your hourly email from the scheduler task."
    )
    frappe.logger().info("📧 Email sent to sam@gmail.com")