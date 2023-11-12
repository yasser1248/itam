# Copyright (c) 2023, IT Systematic and contributors
# For license information, please see license.txt

import frappe
from frappe import _
from itertools import zip_longest


def execute(filters=None):
    columns = get_columns(filters)
    data = get_data(filters)
    chart = get_chart_data(columns , data)
    report_summary = get_report_summary(data)
    
    return columns, data, None, chart, report_summary



def get_columns(filters = None):
    columns = [
        {
            "label": _("Type"),
            "fieldname": "doctype",
            "fieldtype": "Link",
            "options" : "DocType",
            "width": 150, 
        },
        {
            "label": _("Name"),
            "fieldname": "name",
            "options" : "doctype",
            "fieldtype": "Dynamic Link",
            "width": 180,
        },
        {
            "label": _("Item Code"),
            "fieldname": "item_code",
            "fieldtype": "Link",
            "options" : "Item" ,
            "width": 350,
        },

        {
            "label": _("Status"),
            "fieldname": "status",
            "fieldtype": "Data",
            "width": 180,
        },
        {
            "label": _("Qty"),
            "fieldname": "qty",
            "fieldtype": "Int",
            "width": 120,
        },
    ]
    
    return columns
    


def get_data(filters=None) :
    
    all_data = []
    
    if filters.get("from_date") and  filters.get("to_date"):
        if filters.get("from_date") >  filters.get("to_date") :
            frappe.throw(_("To Date Must Be Greater Than To Date"))
            
    all_assets =  frappe.db.get_all("Asset" ,filters= { "docstatus" : 1} , fields= ["name","item_code" , "status" ,"asset_category" , "custom_model" , "custodian" , "location"])
    
    all_po = frappe.db.sql("""
                                SELECT poi.parenttype  as doctype , po.name , poi.item_code , po.status , (poi.qty - poi.received_qty ) as qty
                                FROM `tabPurchase Order Item` poi
                                LEFT JOIN `tabPurchase Order` po
                                    ON po.name = poi.parent
                                WHERE po.docstatus = 1
                                    AND po.status IN ('To Receive and Bill' , 'To Receive')

                        """, as_dict=1)
    
    
    for item_one , item_two  in zip_longest(all_assets , all_po) :        
        if item_two :
            # item_two.status = "In transit" if item_two.status == "To Receive and Bill" else item_two.status
            item_two.status = "In transit"
            all_data.append(item_two)
            
        if item_one :
            if item_one.status == "Submitted" and item_one.custodian == None :
                item_one.status = "In stock" 
            elif item_one.status == "Submitted"  and item_one.custodian :
                item_one.status = "In use" 
            

            all_data.append(item_one.update({"doctype" : "Asset" , "qty" : 1}))
            
    return all_data


def get_chart_data(columns , data):
    
    summary = get_report_summary_details()
    
    summary.append(sum(list(map(lambda x : x.get("qty") if x.get("doctype") == "Purchase Order" else 0 , data))))

    chart = {
        "data" : {
            # "labels" : ["In use" , "In stock" , "Consumed" , "In maintenance" , "In transit" , "Retired" ],
            "labels" : [ "In use" , "In stock" , "In maintenance" ,"Consumed"  , "Retired" , "In transit" ],
            "datasets" : [
                { "name": "Summary","values" : summary} ,
                # { "name": "Dataset 2", "values": [30, 50, -10, 15, 18] } ,
            ]
        },

        "type" : "pie" ,
        "colors": [ "#0d3659" , "#80e5ff" ,"#525c69","#a6cff2","#6a6d7c" , "#2086df","#AD2959" ],
    }
    return chart



def get_report_summary_details():
    
    all_data = frappe.db.sql("""
                                SELECT 
                                    COUNT(CASE WHEN  custodian IS NOT NULL AND status NOT IN ("In Maintenance")  AND custom_is_for_disposal = 0 THEN 1 END) as in_use ,
                                    COUNT(CASE WHEN  location IS NOT NULL AND status NOT IN ("In Maintenance") AND custom_is_for_disposal = 0 THEN 1 END) as in_stock ,
                                    COUNT(CASE WHEN  status = "In Maintenance" THEN 1 END ) AND custom_is_for_disposal = 0  as in_maintain ,
                                    COUNT(CASE WHEN  status = "Fully Depreciated" THEN 1 END ) AND custom_is_for_disposal = 0  as as_consumed ,
                                    COUNT(CASE WHEN  custom_is_for_disposal = 1 THEN 0 END ) AND custom_is_for_disposal = 0  as retierd 
                                FROM `tabAsset`
                                WHERE  docstatus = 1
                            """,as_list=1)
    
    return all_data[0]
    
    
def get_report_summary(data):
    
    all_asset_quantity = sum(list(map(lambda x : x.get("qty") if x.get("doctype") == "Asset" else 0, data)))
    return [
        {
            "value": all_asset_quantity,
            "label": _("Total Asset"),
            "indicator": "Green" ,
            "datatype": "Int",
            # "currency": currency,
        },
    ]