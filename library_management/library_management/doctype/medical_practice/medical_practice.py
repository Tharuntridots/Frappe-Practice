# Copyright (c) 2025, tharun and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.query_builder import DocType
from frappe.query_builder.functions import Count


class MedicalPractice(Document):
	pass


@frappe.whitelist()
def get_patients_above_30():
	MP = DocType("Medical Practice")

	result = (
		frappe.qb.from_(MP)
		.select(
			MP.patient_name,
			MP.age,
			MP.disease
		)
		.where(MP.age >30)
	).run(as_dict = True)

	return result

@frappe.whitelist()
def get_patients_record():
	MD=  DocType("Medical Practice")
	name_field = frappe.qb.Field("patient_name")
	query = (
		frappe.qb.from_(MD)
		.select(MD.patient_name, MD.age)
		.where(name_field.like("R%"))
	)
	
	result = frappe.db.sql(query, as_dict=True)

	return result


@frappe.whitelist()
def get_joined_patient_visits():
    PatientVisit = DocType("Patient Visit")
    MedicalPractice = DocType("Medical Practice")

    query = (
        frappe.qb
        .from_(PatientVisit)
        .inner_join(MedicalPractice)
        .on(PatientVisit.patient_id == MedicalPractice.name)
        .select(
            PatientVisit.date.as_("visit_date"),
            MedicalPractice.name.as_("patient_id"),
            MedicalPractice.patient_name,
            MedicalPractice.age,
            MedicalPractice.disease
        )
    )

    result = query.run(as_dict=True)
    return result


@frappe.whitelist()
def use_join():
	PV = DocType("Patient Visit")
	MP = DocType("Medical Practice")

	query = (
		frappe.qb.from_(PV)
		.inner_join(MP)
		.on(PV.patient_id == MP.name)
		.select(
			PV.date.as_("Visit Date"),
			MP.name.as_("patient_id"),
			MP.patient_name,
			MP.age
		)
	)

	result = query.run(as_dict = True)
	return result



@frappe.whitelist()
def test_fun():
    PV = DocType("Patient Visit")
    MP = DocType("Medical Practice")

    visit_count = Count(PV.name).as_("visit_count")

    query = (
        frappe.qb.from_(PV)
        .inner_join(MP).on(PV.patient_id == MP.name)
        .groupby(PV.patient_id)
        .select(MP.patient_name, visit_count)
    )

    result = query.run(as_dict=True)
    return result

	

