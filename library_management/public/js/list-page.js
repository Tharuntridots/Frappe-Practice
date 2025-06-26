frappe.pages['list-page'].on_page_load = function(wrapper) {
    let page = frappe.ui.make_app_page({
        parent: wrapper,
        title: 'Combined Dashboard',
        single_column: true
    });

    $(wrapper).find('.layout-main-section').html(`
        <div id="article-section"></div>
        <div id="medicine-section"></div>
    `);

    // Load templates
    $(wrapper).find('#article-section').html(
        frappe.render_template("article_dashboard", {})
    );

    $(wrapper).find('#medicine-section').html(
        frappe.render_template("medicine_dashboard", {})
    );

    // JS logic for article section
    frappe.call({
        method: "frappe.client.get_count",
        args: { doctype: "Medical Practice" },
        callback: function(r) {
            $('#article-section #total-patients').text(r.message || 0);
        }
    });

    // JS logic for medicine section
    frappe.call({
        method: "frappe.client.get_count",
        args: { doctype: "Prescription Medicine" },
        callback: function(r) {
            $('#medicine-section #total-medicines').text(r.message || 0);
        }
    });
};
