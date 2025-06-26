frappe.ui.form.on('Samosa', {
    refresh: function(frm) {
        frappe.msgprint("Hi");

        // Add button only if document is not submitted (optional)
        if (!frm.is_new() && frm.doc.docstatus === 0) {
            frm.add_custom_button('Accept', function() {
                frm.set_value('status', 'Completed');
                frm.save();
            });
        }
    }
});
