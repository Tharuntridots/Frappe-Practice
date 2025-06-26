from datetime import datetime

def field_setup_timeline(doctype, docname):
    return [
        {
            "creation": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            "template": "custom_fieldsetup_timeline",
            "template_data": {
                "msg": f"Timeline triggered for FieldSetup: {docname}"
            }
        }
    ]

