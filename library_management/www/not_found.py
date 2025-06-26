import frappe

def get_context(context):
    context.no_cache = 1
    context.title = "404 - Page Not Found"
    return context
