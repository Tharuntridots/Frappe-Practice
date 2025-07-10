import socket

def get_local_ip_address():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip_address = s.getsockname()[0]
        s.close()
        return ip_address
    except socket.error:
        return "Local IP address edukka mudiyala."

def boot_session(bootinfo):
    local_ip = get_local_ip_address()
    bootinfo.my_global_key = f"Local IP Detected: {local_ip}"
    print(f"Boot Session Status: {bootinfo.my_global_key}")


# apps/library_management/library_management/boot.py

import frappe

def get_new_value():
    doc = frappe.new_doc('Company Data')
    doc.company_name = "qwert"
    doc.description = "new insert"
    doc.insert()
    frappe.db.commit()  # Just to be sure in scheduled jobs
    frappe.logger().info("New Company Data inserted by scheduler.")
