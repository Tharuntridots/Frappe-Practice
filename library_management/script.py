import frappe

def get_web_pages_with_dynamic_routes():
    brand_list = frappe.get_all("Brand List", fields=["name", "brand_item", "value", "value2"])

    routes = []
    for brand in brand_list:
        route_path = f"brand_item/{brand.brand_item.lower().replace(' ', '-')}"
        routes.append(frappe._dict({
            "name": f"{brand.brand_item}-page",
            "route": route_path,
            "template": "templates/pages/brand_item.html",
            "context": {
                "brand_name": brand.brand_item,
                "value": brand.value,
                "value2": brand.value2
            }
        }))

    return routes
