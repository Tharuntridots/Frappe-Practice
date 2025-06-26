// Copyright (c) 2025, tharun and contributors
// For license information, please see license.txt

frappe.ui.form.on('Medical Prescription', {
    // Triggered when the parent form is loaded
    onload(frm) {
        console.log("Prescription form loaded");
    }
});


// frappe.ui.form.on("Prescription Medicine", {
// 	medicine_name(frm,cdt, cdn){
//         let row = frappe.get_doc(cdt, cdn)
//         frappe.msgprint(`Medicine selected: ${row.medicine_name}`)
        
//         if(row.medicine_name === "Paracetamol") {
//             row.frequency = "twice in a day";
//             row.dosage = "200mg"
//             frm.refresh_field('medicines');
//         }
//     }
// });

// frappe.ui.form.on('Prescription Medicine', {
//     medicine_name(frm, cdt, cdn) {
//         let row = frappe.get_doc(cdt, cdn);

//         if (row.medicine_name) {
//             frappe.db.get_doc('Item', row.medicine_name).then(item => {
//                 row.dosage = item.default_dosage;
//                 row.frequency = item.default_frequency;
//                 frm.refresh_field('medicines');
//             });
//         }
//     }
// });

function update_total_medicines(frm){
    frm.set_value('total_medicines', frm.doc.medicines.length)
}
frappe.ui.form.on('Prescription Medicine', {
    medicine_name(frm){
        update_total_medicines(frm)
    },
    dosage(frm) {
        update_total_medicines(frm);
    },
    frequency(frm) {
        update_total_medicines(frm);
    },
    medicines_remove(frm) {
        update_total_medicines(frm);
    }
})

