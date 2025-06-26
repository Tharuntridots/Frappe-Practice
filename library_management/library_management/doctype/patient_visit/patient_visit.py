# Copyright (c) 2025, tharun and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class PatientVisit(Document):
	pass

@frappe.whitelist()
def get_patient_data():
    # Example: Fetch name, patient_id from Patient Visit DocType
    query = """
        SELECT * FROM `tabPatient Visit` ORDER BY visit_date DESC LIMIT 10
    """
    data = frappe.db.sql(query, as_dict=True)
    return data

@frappe.whitelist()
def get_patient_data2():
    query = """
        SELECT * FROM `tabPatient Visit` WHERE department = 'Heart';
    """
    data = frappe.db.sql(query, as_dict=True)
    return data

@frappe.whitelist()
def get_patient_data3():
    query = """
        SELECT department, COUNT(*) AS total_visits
        FROM `tabPatient Visit`
        GROUP BY department;
    """
    data = frappe.db.sql(query, as_dict=True)
    return data

@frappe.whitelist()
def get_patient_data4():
    query = """
        SELECT department, COUNT(*) AS total_visits
        FROM `tabPatient Visit`
        GROUP BY department
        HAVING total_visits > 2;
    """
    data = frappe.db.sql(query, as_dict=True)
    return data


@frappe.whitelist()
def get_patient_data5():
    query = """
        SELECT name, bill_amount FROM `tabPatient Visit`
        ORDER BY bill_amount DESC;
    """
    data = frappe.db.sql(query, as_dict=True)
    return data

@frappe.whitelist()
def get_patient_data6():
    query = """
        SELECT pv.name AS visit_id, p.name AS patient_name, p.age, pv.visit_date
        FROM `tabPatient Visit` pv
        JOIN `tabPatient` p ON pv.patient_id = p.name;
    """
    data = frappe.db.sql(query, as_dict=True)
    return data

@frappe.whitelist()
def get_patient_data7():
    query = """
        SELECT pv.name AS visit_id, d.name AS doctor_name, d.specification
        FROM `tabPatient Visit` pv
        JOIN `tabDoctor` d ON pv.doctor_id = d.name;
    """
    data = frappe.db.sql(query, as_dict=True)
    return data