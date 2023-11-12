import frappe
from frappe.utils import nowdate

@frappe.whitelist()
def material_request(data,user):
    try:
        request_data = frappe.parse_json(data)
        material_request_doc =frappe.new_doc("Material Request")

        material_request_doc.set("material_request_type","Material Issue")
        material_request_doc.set("transaction_date",nowdate())
        material_request_doc.set("schedule_date",nowdate())
        material_request_doc.set("company",frappe.defaults.get_user_default("company"))
        material_request_doc.set("custom_request_type",request_data.get("request_type"))

        item = {
            "item_code": request_data.get("item_code"),
            "qty": request_data.get("qty"),
            "uom": frappe.defaults.get_user_default("stock_uom"),
        }

        material_request_doc.append("items",item)
        material_request_doc.set("custodian",frappe.get_doc(doctype="Employee",user_id=user).name)
        
        material_request_doc.save()
        return "Success"
    except Exception:
        return "Fail"
    

