frappe.pages['mypage'].on_page_load = function(wrapper) {
    var page = frappe.ui.make_app_page({
        parent: wrapper,
        title: 'My Practice Page',
        single_column: true
    });

    page.add_inner_button('Click Me', () => {
        frappe.msgprint("Hello from Practice Page!");
    });

    $(wrapper).append("<div><h3>This is a custom Frappe page!</h3></div>");
};
