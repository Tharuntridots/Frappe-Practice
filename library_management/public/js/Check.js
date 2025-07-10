frappe.ready(function() {
    const container = document.getElementById("custom-container");

    if (container) {
        const message = document.createElement("p");
        message.innerText = "Hello from JavaScript! ✅";
        container.appendChild(message);
    } else {
        console.warn("custom-container not found!");
    }
});

frappe.ui.form.on("Company Details", )