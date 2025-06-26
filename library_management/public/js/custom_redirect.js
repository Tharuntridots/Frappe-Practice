frappe.ready(() => {
  frappe.after_ajax(() => {
    if (frappe.session && frappe.session.user === "gokul@example.com") {
      if (window.location.pathname === "/app") {
        window.location.href = "/app/library-member";
      }
    }
  });
});
