frappe.ui.form.on('Biometric Attendance', {
    refresh: function(frm) {
        frm.add_custom_button("Scan Fingerprint", () => {
            frappe.msgprint("Fingerprint Scan Triggered");

            // Simulated API or hardware call
            navigator.vibrate(100); // simulate action in browser
            frappe.call({
                method: "library_management.api.process_biometric",
                args: {
                    employee: frm.doc.employee_name
                },
                callback: function(r) {
                    if (r.message === "success") {
                        frappe.msgprint("Biometric record saved successfully.");
                    }
                }
            });
        });
    }
});
