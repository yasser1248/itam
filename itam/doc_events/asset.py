import frappe

from frappe.utils import date_diff

def add_barcode_after_insert(doc:dict= {} , event:str=""):
    frappe.db.set_value("Asset" , doc.name , "custom_barcode" , doc.name)
    frappe.db.commit()
    doc.reload()
    
    
def add_differ_date(doc:dict= {} , event:str=""):
    
    if doc.get("insurance_end_date") and doc.get("insurance_start_date") :
    
        differ_date = date_diff(doc.insurance_end_date , doc.insurance_start_date) 
        
        # doc.custom_days_ = differ_date
        
        frappe.db.set_value("Asset" , doc.name , "custom_days_" , differ_date )
        
        frappe.db.commit()
    
    