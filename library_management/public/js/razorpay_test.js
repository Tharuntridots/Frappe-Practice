frappe.ui.form.on('Razorpay Test', {
    refresh: function (frm) {
        frm.add_custom_button('Open Razorpay', () => {
            let amount_in_paise = frm.doc.amount * 100 ;

            let options = {
                key: "rzp_test_1DP5mmOlF5G5ag",
                amount: amount_in_paise,
                currency: "INR",
                name: frm.doc.customer_name || "Demo User",
                description: "UI Demo - No real payment",
                handler: function (response) {
                    frappe.msgprint("Payment ID: " + response.razorpay_payment_id);
                },
                prefill: {
                    name: frm.doc.customer_name || "Test User",
                    email: frm.doc.email || "test@example.com",
                    contact: frm.doc.mobile || "9999999999"
                },
                theme: {
                    color: "#3399cc"
                },
                modal: {
                    ondismiss: function () {
                        frappe.msgprint("You closed the Razorpay popup.");
                    }
                }
            };

            let rzp = new Razorpay(options);
            rzp.open();
        });
    }
});
