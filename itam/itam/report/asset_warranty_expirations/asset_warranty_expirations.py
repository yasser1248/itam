# Copyright (c) 2023, IT Systematic and contributors
# For license information, please see license.txt

import frappe
from frappe import _

def execute(filters=None):
    columns = get_columns(filters)
    data = get_data(filters)
    return columns, data


def get_columns(filters = None):
    columns = [
        {
            "label": _("Name"),
            "fieldname": "name",
            "fieldtype": "Link",
            "options": "Asset",
            "width": 180,
        },
        {
            "label": _("Item Code"),
            "fieldname": "item_code",
            "fieldtype": "Link",
            "options": "Item",
            "width": 300,
        },
        {
            "label": _("Asset Category"),
            "fieldname": "asset_category",
            "fieldtype": "Link",
            "options": "Asset Category",
            "width": 150,
        },
        {
            "label": _("Model"),
            "fieldname": "custom_model",
            "fieldtype": "Data",
            "width": 120,
        },
        {
            "label": _("State"),
            "fieldname": "state",
            "fieldtype": "Data",
            "width": 120,
        },
        {
            "label": _("Insurance Start Date"),
            "fieldname": "insurance_start_date",
            "fieldtype": "Date",
            "width": 150,
        },
        {
            "label": _("Insurance End Date"),
            "fieldname": "insurance_end_date",
            "fieldtype": "Date",
            "width": 150,
        },
    ]
    
    return columns


def get_data(filters=None) :
    
    
    if filters.get("from_date") and  filters.get("to_date"):
        if filters.get("from_date") >  filters.get("to_date") :
            frappe.throw(_("To Date Must Be Greater Than To Date"))
    
    conditions = ""
    
    if filters.get("from_date") and filters.get("to_date") :

        conditions += "AND insurance_start_date >= %(from_date)s  AND insurance_end_date <= %(to_date)s"

    
    asset_details = frappe.db.sql("""
                                        SELECT name , item_code , asset_category , custom_model , insurance_start_date , insurance_end_date , 
                                        CASE WHEN custodian IS NOT NULL  THEN 'In Use'
                                            ELSE 'OUT'
                                        END AS state
                                        FROM `tabAsset`
                                        WHERE docstatus = 1
                                            {conditions}
                """.format(conditions=conditions),{
                    "from_date": filters.get("from_date") ,
                    "to_date": filters.get("to_date") ,
                } , as_dict=1)
    
    
    return asset_details

