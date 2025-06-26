// Copyright (c) 2025, tharun and contributors
// For license information, please see license.txt

// frappe.ui.form.on('Medical Practice', {
//     before_save: function(frm) {
//         frm.add_custom_button("Get Patients Above 30", function() {
//             frappe.call({
//                 method: "library_management.library_management.doctype.medical_practice.get_patients_above_30",
//                 callback: function(r) {
//                     console.log(r.message);
//                     frappe.msgprint(JSON.stringify(r.message));
//                 }
//             });
//         });
//     }
// });



frappe.ui.form.on('Medical Practice', {
    refresh: function(frm) {
        frm.add_custom_button('Click me', function() {
            frappe.call({
                method: "library_management.library_management.doctype.medical_practice.medical_practice.test_fun",
                callback: function(r) {
                    console.log(r.message);
                    frappe.msgprint(__('Result: ') + JSON.stringify(r.message));
                }
            });
        });
    }
});
