// Copyright (c) 2025, tharun and contributors
// For license information, please see license.txt

frappe.ui.form.on("Calender Doctype", {
	refresh(frm) {
        frm.add_custom_button('Click me', ()=>{
            frappe.call({
                method: "library_management.api.google_calendar.authorize_user"
            })
        })
	},
});
