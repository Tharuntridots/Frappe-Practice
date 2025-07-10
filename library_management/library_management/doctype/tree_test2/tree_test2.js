// Copyright (c) 2025, tharun and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Tree_test2", {
// 	refresh(frm) {

// 	},
// });


// frappe.treeview_settings['Tree_test2'] = {
//     breadcrumb: 'Library Management',
//     title: 'Tree View for Test2',
//     get_tree_nodes: 'library_management.library_management.doctype.tree_test2.get_children',
//     add_tree_node: 'library_management.library_management.doctype.tree_test2.add_node',
//     fields: [
//         {
//             fieldtype: 'Data',
//             fieldname: 'name1',
//             label: 'Name',
//             reqd: true
//         },
//         {
//             fieldtype: 'Check',
//             fieldname: 'is_group',
//             label: 'Is Group'
//         }
//     ],
//     extend_toolbar: true,
//     toolbar: [
//         {
//             label: 'Add Child',
//             condition: function(node) {
//                 return node.data.is_group;
//             },
//             click: function(node) {
//                 frappe.model.with_doctype('Tree_test2', function() {
//                     frappe.treeview_settings['Tree_test2'].add_node(node);
//                 });
//             },
//             btnClass: 'btn-primary'
//         }
//     ]
// };
