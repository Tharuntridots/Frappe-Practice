// Copyright (c) 2025, tharun and contributors
// For license information, please see license.txt

frappe.ui.form.on("ServerScript", {
    // enable : function(frm){
    //     frm.call({
    //         doc : frm.doc,
    //         method : 'frm_call',
    //         args : {
    //             msg : "Hello"
    //         }, 
    //         freeze: true,
    //         freeze_message: __('Calling frm_call Method'),
    //         callback: function(r){
    //             frappe.msgprint(r.message)
    //         }
    //     })
    // }

    enable: function(frm) {
        frappe.call({
            method: 'library_management.library_management.doctype.client_scripts.client_scripts.frappe_call',
            args: {
                msg: "Hello"
            }, 
            freeze: true,
            freeze_message: __('Calling frm_call Method'),
            callback: function(r) {
                frappe.msgprint(r.message);
            }
        });
    }
});
