// frappe.ui.form.on('Note Book', {
//     brand: function(frm) {
//         if (frm.doc.brand) {
//             frappe.db.get_doc('Brand List', frm.doc.brand).then(brand_doc => {
//                 // Set pencil to brand's value
//                 frm.set_value('pencil', brand_doc.value);
//                 // Set pen and sketch to zero
//                 frm.set_value('pen', 0);
//                 frm.set_value('sketch', 0);
//             });
//         } else {
//             frm.set_value('pencil', '');
//             frm.set_value('pen', '');
//             frm.set_value('sketch', '');
//         }
//     },
//     onload: function(frm) {
//         frm.trigger('brand');
//     }
// });


frappe.ui.form.on('Note Book', {
    refresh: function(frm) {
        frm.add_custom_button('Go to Field Setup', function() {
            frappe.set_route('Form', 'Field Setup');
        });
    }
});


frappe.ui.form.on('Note Book', {
    refresh(frm) {
        frm.add_custom_button("Get My Notebooks", function () {
            frappe.call({
                method: 'library_management.api.get_my_notebooks',
                callback: function(r) {
                    console.log(r.message);
                    frappe.msgprint("Check browser console for result.");
                }
            });
        });
    }
});


frappe.ui.form.on('Note Book', {
    onload: function (frm) {
        frappe.call({
            method: 'library_management.api.get_current_user_roles',
            callback: function(r) {
                if (r.message) {
                    if (r.message.includes("Teacher")) {
                        frappe.msgprint("You are accessing this as a Teacher.");
                    } else {
                        frappe.msgprint("Your roles: " + r.message.join(", "));
                    }
                }
            }
        });
    }
});

frappe.ui.form.on('Company Details', {
    amount : function(frm){
        if (frm.doc.amount >= 10000){
            frm.set_value('Status', 'No1')
        } else {
            frm.set_value()
        }
    }
})