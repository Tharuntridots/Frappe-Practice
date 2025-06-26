// Copyright (c) 2025, tharun and contributors
// For license information, please see license.txt

frappe.ui.form.on("Field Setup", {
	// setup(frm){
    //     frm.set_value("status", "Draft")
    //     console.log("status value set")
    // },

    // before_load(frm){
    //     console.log("before_load: this is load first and clean up previous data ")
    // },

    // refresh(frm){
    //     console.log("Button using refresh")
    //     frm.clear_custom_buttons();

    //     if(frm.doc.status === "Draft")
    //         frm.add_custom_button("Submit Now", ()=>{
    //             // frm.save()
    //             console.log("submitted")

    //         })
    // },


    // onload_post_render(frm){
    //     console.log("this is onload_post_render")
    //     $(frm.fields_dict.status.wrapper).css("background-color", "#f0f8ff");
    //     $(frm.fields_dict.age.wrapper).css("background-color", "#f0f8ff")
    //     $(frm.fields_dict.name1.wrapper).css("background-color", "#f0f8ff")
    //     $(frm.fields_dict.work.wrapper).css("background-color", "#f0f8ff")

    // },

    validate: function(frm){
        if(frm.doc.age > 18){
            console.log("okay you are above 18")
        }
        else{
            frappe.msgprint("you are under 18")
        }

    },


    before_save(frm){
        frm.set_value("status", "In Progress")

    },

    age(frm){
        console.log("Namne:", frm.doc.name1)
    }

});
   

frappe.call({
    method: "library_management.library_management.doctype.field_setup.field_setup.get_enabled_fieldsetups",
    callback: function(r) {
        frappe.msgprint("Returned: " + r.message);
    }
});

