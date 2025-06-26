frappe.ui.form.on('Sales Tracker', {
    // refresh: function(frm) {
    //     let is_allowed = frappe.user_roles.includes('System Manager');
    //     frm.toggle_enable(['total_amount', 'total_items'], is_allowed);
    // },

    // total_items: function(frm) {
    //     frappe.msgprint("Total Items changed!");
    //     frm.toggle_reqd('customer_name', frm.doc.total_items === 7);
    // },
    
    // total_amount : function(frm){
    //     frm.toggle_display('data', frm.doc.total_amount > 500);
    // }
    
});


// frappe.call({
//     method: "library_management.library_management.doctype.sales_tracker.sales_tracker.get_total_items",
//     args : {docname : cur_frm.doc.name},
//     callback : function(r){
//         frappe.msgprint("Total Items: " + r.message);
//     }
// });

// frappe.call({
//     method : "library_management.library_management.doctype.sales_tracker.sales_tracker.create_sales_tracker",
//     args : {
//         customer_name : "Rakesh",
//         amount: 4000
//     },
//     callback : function(r){
//         frappe.msgprint("Created Doc: "+ r.message);
//     }
// })

// frappe.call({
//     method: "library_management.library_management.doctype.sales_tracker.sales_tracker.get_filed_link_details",
//     args : { link_name : cur_frm.doc.filed_link},
//     callback : function(r){
//         if(r.message){
//             frappe.msgprint("Name: "+ r.message.name + "  Age: "+ r.message.age)
//         }
//     }
// })

// frappe.call({
//     method: "library_management.library_management.doctype.sales_tracker.sales_tracker.get_sales_items",
//     args: {
//         docname : cur_frm.doc.name
//     },
//     callback: function(r){
//         if(r.message && r.message.length > 0){
//             let message = "Sales Items: \n\n";
//             r.message.forEach(function(item, index){
//                 message += `${index + 1}. ${item.item_name} - Qty: ${item.quantity}, Rate: ${item.rate}, Status: ${item.status}\n`;
//             });
//             frappe.msgprint(message);
//         } else {
//             frappe.msgprint("No items found.");
//         }
//     }
// });

// frappe.call({
//     method : "library_management.library_management.doctype.sales_tracker.sales_tracker.get_filtered_docs",
//     callback : function(r){
//         frappe.msgprint(r.message)
//     }
// })

frappe.ui.form.on('Sales Tracker', {
    after_save: function(frm) {
        frappe.msgprint("Saved!");
        frappe.utils.play_sound("ping");
    }
});
