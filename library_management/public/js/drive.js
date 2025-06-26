frappe.ui.form.on('Google Drive File', {
    refresh: function(frm) {
        frm.add_custom_button('Connect Google Drive', () => {
            frappe.call({
                method: 'library_management.api.get_google_auth_url',
                callback: function(r) {
                    if (r.message) {
                        window.open(r.message, "_blank");
                    }
                }
            });
        });
    }
});
