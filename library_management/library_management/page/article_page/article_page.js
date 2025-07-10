// frappe.pages['article-page'].on_page_load = function(wrapper) {
//     let page = frappe.ui.make_app_page({
//         parent: wrapper,
//         title: 'Article Dashboard',
//         single_column: true
//     });

//     $(wrapper).find('.layout-main-section').append(`
//         <div class="row">
//             <div class="col-sm-4">
//                 <div class="widget-box dashboard-box">
//                     <h3>Total Patients</h3>
//                     <div id="total-patients">Loading...</div>
//                 </div>
//             </div>
//             <div class="col-sm-4">
//                 <div class="widget-box dashboard-box">
//                     <h3>Total Medicines</h3>
//                     <div id="total-medicines">Loading...</div>
//                 </div>
//             </div>
//         </div>
//     `);

//     // Custom style
//     const style = `
//         <style>
//             .dashboard-box {
//                 background-color: #f7f7f7;
//                 border: 1px solid #ddd;
//                 padding: 20px;
//                 border-radius: 8px;
//                 box-shadow: 2px 2px 8px rgba(0,0,0,0.1);
//                 margin-bottom: 20px;
//             }
//             .dashboard-box h3 {
//                 margin-top: 0;
//                 font-weight: 600;
//             }
//             .dashboard-box div {
//                 font-size: 1.5rem;
//                 color: #007bff;
//             }
//         </style>
//     `;
//     $(wrapper).append(style);

//     // Fetch counts
//     frappe.call({
//         method: "frappe.client.get_count",
//         args: {
//             doctype: "Medical Practice"
//         },
//         callback: function(r) {
//             $('#total-patients').text(r.message || 0);
//         }
//     });

//     frappe.call({
//         method: "frappe.client.get_count",
//         args: {
//             doctype: "Prescription Medicine"
//         },
//         callback: function(r) {
//             $('#total-medicines').text(r.message || 0);
//         }
//     });
// };


page.set_title('My Page');