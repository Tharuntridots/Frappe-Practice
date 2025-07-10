// frappe.pages['mypage'].on_page_load = function(wrapper) {
//     const page = frappe.ui.make_app_page({
//         parent: wrapper,
//         title: 'Initial Title',
//         single_column: true
//     });

//     // Dynamically change the title
//     page.set_title('My Page');
//     page.set_indicator('Pending', 'orange')

// 9

//     page.add_menu_item('Send Email', () => open_email_dialog())



// };



// frappe.pages['mypage'].on_page_load = function(wrapper) {
//     let $wrapper = $(wrapper);
//     $wrapper.html(`<div id="chart" style="padding: 20px;"></div>`);

//     let data = {
//         labels: [],
//         datasets: [
//             {
//                 name: "Fever",
//                 values: []
//             },
//             {
//                 name: "Cold",
//                 values: []
//             }
//         ]
//     };

//     let chart = new frappe.Chart("#chart", {
//         title: "Disease Count Realtime",
//         data: data,
//         type: 'line',
//         height: 300,
//         colors: ['#ff6f69', '#247ba0']
//     });

//     frappe.realtime.on('disease_realtime_event', function(data_point) {
//         const label = data_point.label;
//         const values = data_point.points;

//         chart.data.labels.push(label);
//         chart.data.datasets[0].values.push(values[0]);  // Fever
//         chart.data.datasets[1].values.push(values[1]);  // Cold

//         // Keep only latest 10 entries
//         if (chart.data.labels.length > 10) {
//             chart.data.labels.shift();
//             chart.data.datasets.forEach(ds => ds.values.shift());
//         }

//         chart.update();
//     });
// };


// frappe.pages['mypage'].on_page_load = function(wrapper) {
//     console.log("Page loaded");

//     const $wrapper = $(wrapper);
//     $wrapper.html(`<div id="chart" style="padding: 20px;"></div>`);

//     // Initial empty chart data
//     const data = {
//         datasets: [
//             {
//                 name: "Fever",
//                 values: []
//             },
//             {
//                 name: "Cold",
//                 values: []
//             }
//         ]
//     };

//     // Create Realtime Chart instance
//     const chart = new frappe.ui.RealtimeChart("#chart", "disease_realtime_event", 10, {
//         title: "Disease Count Realtime",
//         data: data,
//         type: "bar",
//         height: 300,
//         colors: ["#ff6f69", "#247ba0"]
//     });

//     // Start listening to the socket event
//     chart.start_updating();

//     // (Optional) Log data received
//     frappe.realtime.on("disease_realtime_event", (data) => {
//         console.log("Realtime event data received:", data);
//     });
// };




