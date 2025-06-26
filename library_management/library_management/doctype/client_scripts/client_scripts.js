// Copyright (c) 2025, tharun and contributors
// For license information, please see license.txt

frappe.ui.form.on("Client_Scripts", {

    // validate:function(frm){
    //     frm.set_value('full_name', frm.doc.first_name + " "+ frm.doc.middle_name + " "+ frm.doc.last_name)
        
    //     let row = frm.add_child('family_members', {
    //         name1: 'John',
    //         age:56,
    //         relation:'Uncle',
    //     })
    // },

    // enable:function(frm){
    //     // frm.set_df_property('first_name', 'reqd', 1)
    //     // frm.set_df_property('middle_name', 'read_only', 1)

    //     frm.toggle_reqd('age',true)
    // }
 
    // refresh:function(frm){
        // frm.add_custom_button('Click Me', ()=>{
        //     frappe.msgprint("You click me!")
        // })

        // frm.add_custom_button('click me 1', ()=>{
        //     frappe.msgprint("You Click 1")
        // }, 'Click Me')

        // frm.add_custom_button('click me 2', ()=>{
        //     frappe.msgprint("You Click 2")
        // }, 'Click Me')
    // }

    // frm.doc.first_name 

    // after_save: function(frm) {
    //     // frappe.msgprint(`The full name is ${frm.doc.first_name} ${frm.doc.middle_name} ${frm.doc.last_name}`);

    //     for (let row of frm.doc.family_members){
    //         frappe.msgprint(__("{0}. the family membrs name is '{1}' and relation is '{2}'",  [row.idx, row.name1, row.relation]));
               
    //     }
    // }


    // refresh : function(frm){
    //     if(frm.is_new()) {
    //         frm.set_intro('Now this show first ')
    //     }
    // }

// ---------------------------------------------------------------------------
	// refresh : function(frm){
    //     frappe.msgprint("Hello refresh")
    // }

    // onload : function(frm){
    //     frappe.msgprint("Hello onload")
    // }

    // validate : function(frm){
    //     frappe.msgprint("Hello validate")
    // }

    // before_save : function(frm){
    //     frappe.msgprint("Hello bef save")
    // }

    // after_save: function(frm){
    //     frappe.msgprint("Hello aft save")
    // }

    // enable : function(frm){
    //     frappe.msgprint("Hello enable")
    // }

    // age : function(frm){
    //     frappe.msgprint(f"Hello {age}")
    // }

    // family_members_on_form_rendered : function(frm){
    //     frappe.msgprint("Hello family")
    // }

    // before_submit : function(frm){
    //     frappe.msgprint("Hello refresh")
    // },

    // on_submit : function(frm){
    //     frappe.msgprint("Hello refresh")
    // },

    // before_cancel : function(frm){
    //     frappe.msgprint("Hello refresh")
    // },

    // on_cancel : function(frm){
    //     frappe.msgprint("Hello refresh")
    // },

});


// frappe.ui.form.on('Family Members', {
//     name1: function(frm){
//         frappe.msgprint("Hello name1")
//     },

//     // age: function(frm) {
//     //     frappe.msgprint("Hello age");
//     // }
// });