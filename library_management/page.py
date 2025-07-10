context.records = frappe.get_all(
    "Company Details",
    fields=["name", "company_name", "amount"]
)
context.greeting = "hii"