frappe.pages['mypage'].on_page_load = function(wrapper) {
    var page = frappe.ui.make_app_page({
        parent: wrapper,
        title: 'My PAge3',  // initial title
        single_column: true
    });

    // Set the title dynamically
    page.set_title('My Page');
};
