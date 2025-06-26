app_name = "library_management"
app_title = "Library Management"
app_publisher = "tharun"
app_description = "library data stored"
app_email = "kishore@example"
app_license = "mit"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "library_management",
# 		"logo": "/assets/library_management/logo.png",
# 		"title": "Library Management",
# 		"route": "/library_management",
# 		"has_permission": "library_management.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/library_management/css/library_management.css"
# app_include_js = "/assets/library_management/js/library_management.js"

# include js, css files in header of web template
# web_include_css = "/assets/library_management/css/library_management.css"
# web_include_js = "/assets/library_management/js/library_management.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "library_management/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "library_management/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "library_management.utils.jinja_methods",
# 	"filters": "library_management.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "library_management.install.before_install"
# after_install = "library_management.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "library_management.uninstall.before_uninstall"
# after_uninstall = "library_management.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "library_management.utils.before_app_install"
# after_app_install = "library_management.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "library_management.utils.before_app_uninstall"
# after_app_uninstall = "library_management.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "library_management.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"library_management.tasks.all"
# 	],
# 	"daily": [
# 		"library_management.tasks.daily"
# 	],
# 	"hourly": [
# 		"library_management.tasks.hourly"
# 	],
# 	"weekly": [
# 		"library_management.tasks.weekly"
# 	],
# 	"monthly": [
# 		"library_management.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "library_management.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "library_management.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "library_management.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["library_management.utils.before_request"]
# after_request = ["library_management.utils.after_request"]

# Job Events
# ----------
# before_job = ["library_management.utils.before_job"]
# after_job = ["library_management.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"library_management.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }


# razarpay

# doctype_js = {
#     "Razorpay Test": "public/js/razorpay_test.js"
# }

# app_include_js = [
#     "https://checkout.razorpay.com/v1/checkout.js"
# ]


# google drive

# app_include_js = [
#     "/assets/library_management/js/drive.js"
# ]

# biometric
# doctype_js = {
#     "Biometric Attendance": "public/js/biometric_attendance.js"
# }


# app_include_js = "/assets/library_management/js/samosa.js"

# web_include_js = ["assets/library_management/js/portal_script.js"]
# web_include_css = ["assets/library_management/css/portal_style.css"]


# webform_include_js = {"Article": "public/js/article.js"}

# website_context = {
#     "favicon": "/assets/library_management/images/favicon.png"
# }


# extend_website_page_controller_context = {
#     "frappe.www.404": "library_management.pages.context_404"
# }

# website_catch_all = "not_found"


# home_page = "Homepage"


# brand_html = '<div><img src="/assets/library_management/images/favicon.png" style="height:20px; margin-right: 8px;"/> TennisMart</div>'

# base_template = "library_management/templates/my_custom_base.html"


# fixtures = [
#     "Article"
# ]

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#Desk it can access globally in the frappe 
app_include_js = ["assets/library_management/js/desk_custom.js"]

#Portal it can used in www web pages
web_include_js = ["assets/library_management/js/portal_custom.js"]

#web form it can used in webform 
webform_include_js = {"Sales Tracker": "public/js/webform_sales_tracker.js"}

#page js 
page_js = {"article-page" : "public/js/sales_page.js"}

#doctype js it only loa dthe particular doctype
doctype_js = {
    "Sales Tracker": "public/js/hookdoc.js"
}

#sounds can hear by submit the doctype = frappe.utils.play_sound("ping")
sounds = [
    {"name": "ping", "src": "/assets/library_management/images/ping.mp3", "volume": 0.4}
]

# migrate
before_migrate = "library_management.migrate.before_migrate"
after_migrate = "library_management.migrate.after_migrate"

#test = Run the command for test purpose   bench --site library.localhost run-tests --app library_management
before_tests = "library_management.migrate.before_tests"  


#file hook
# before_write_file = "library_management.overrides.file.before_write"
# write_file = "library_management.overrides.file.write_file"
# delete_file_data_content = "library_management.overrides.file.delete_file"

# boot info console = frappe.boot.my_global_key
extend_bootinfo = "library_management.boot.boot_session"

# get_web_pages_with_dynamic_routes = "library_management.script.get_web_pages_with_dynamic_routes"

website_redirects = [
    {"source": "/hello", "target": "/Homepage"}
]

# if we give /hello it redirect to /homepage helps to path problem solve
# website_path_resolver = "library_management.custom.website_routing.my_resolver"

website_route_rules = [
    {"from_route": "/mobile", "to_route": "/mobile_page"}
]

# website_catch_all = "not_found"

portal_menu_items = [
    {"title": "Dashboard", "route": "/dashboard", "role": "Teacher"},
    {"title": "Orders", "route": "/orders", "role": "Teacher"},
]

brand_html = '<div><img src="/assets/library_management/images/favicon.png" height="25" style="margin-right: 5px;"/> <b>TennisMart</b></div>'

# work
# base_template = "library_management/templates/my_custom_base.html"

# redirect without clicking any button
# braintree_success_page = "app.integrations.braintree_success_page"

calendars = ["Fields"] 

default_mail_footer = """
 <div>
 Sent via <a href="https://tennismart.com" target="_blank">TennisMart</a>
</div>
"""

# Work
# extend_website_page_controller_context = {
#     "frappe.www.404": "library_management.pages.context_404"
# }
 
# on_login = "library_management.overrides.successful_login"
# on_session_creation = "library_management.overrides.allocate_free_credits"
# on_logout = "library_management.overrides.clear_user_cache"


auth_hooks = ["library_management.overrides.validate_custom_jwt"]

fixtures = [
    "Field Setup"
]


# logged user entries only display
permission_query_conditions = {
    "Note Book": "library_management.permissions.notebook_query"
}

# Permission only give for a single record to gokul
has_permission = {
    "Field Setup": "library_management.permissions.notebook_has_permission"   
}

override_doctype_class = {
    "Field Setup": "library_management.overrides.CustomFieldSetup"
}

override_whitelisted_methods = {
    "library_management.library_management.doctype.field_setup.field_setup.get_enabled_fieldsetups":
    "library_management.overrides.custom_get_enabled_fieldsetups"
}


# doc_events = {
#     "*": {
#         "after_insert": "library_management.crud_events.after_insert_all"
#     },
#     "Field Setup": {
#         "after_insert": "library_management.crud_events.after_insert_fieldsetup",
#         "before_save": "library_management.crud_events.before_save_fieldsetup"
#     }
# }

# scheduler_events = {
#     "hourly": [
#         "library_management.scheduler_tasks.hourly_notification",
#         "library_management.scheduler_tasks.hourly_notification_email",
#     ]
# }

# additional_timeline_content = {
#     "Field Setup": ["library_management.timeline.field_setup_timeline"]
# }


jinja = {
    "methods": [
        "library_management.jinja.method",
        "library_management.utils.get_fullname"
    ],
    "filters": [
        "library_management.utils.format_currency"
    ]
}

auto_cancel_exempted_doctypes = ["Library Membership"]

# depend before install your app
# required_apps = ["erpnext"]

user_data_fields = [
    {"doctype": "Library Member", "filter_by": "email"},
]


# notification_config = "library_management.notification.get_notification_config"


page_js = {"article-page" : "public/js/list-page.js"}

app_include_js = [
    "/assets/library_management/js/list_page.js"
]
