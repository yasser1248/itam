# Copyright (c) 2023, IT Systematic and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
import datetime
from frappe.utils import get_year_ending , get_year_start


class NextYearPlaining(Document):
    
    @frappe.whitelist()
    def add_items_in_tables(self) :
        self.add_material_request_items()
        self.add_asset_warrentely_date_next_year()
        self.calculate_grand_total()


    def add_material_request_items(self):
        material_request_items = frappe.db.sql("""
                SELECT mri.item_code , mri.item_group , mri.qty as quantity  , mri.rate , mri.amount  as amount , mri.parent as material_request
                FROM `tabMaterial Request Item` mri
                LEFT JOIN `tabMaterial Request` mr
                    ON mr.name = mri.parent
                WHERE mr.workflow_state = "Pending"
                    AND mr.docstatus = 0
        """, as_dict=1)
        if material_request_items :
            self.append_data("material_request_items" , material_request_items)
            self.calculate_total_amount_of_items("material_request_items" , "total_amount")
        

    def add_asset_warrentely_date_next_year(self):
        year = datetime.date.today().year + 1
        first_day , last_day = get_year_start(f"{year}-01-25") , get_year_ending(f"{year}-01-25")
        filters = [
            ['insurance_end_date', 'between', [first_day , last_day]] ,
            {"docstatus" :1}
        ]
        
        asset_details = frappe.db.get_list("Asset",filters=filters , fields=["name as asset_name" , "asset_name as item_code ","asset_category", "custom_model as model" , "gross_purchase_amount as amount"])
        if asset_details :
            self.append_data("asset_items_details" , asset_details)
            self.calculate_total_amount_of_items("asset_items_details" , "asset_total_amount")
            
            
    def append_data(self , child_table , items):
        self.set(child_table , [])
        for item in items :
            self.append(child_table ,item )
            
    def calculate_total_amount_of_items(self, child_table ,field) :
        
        self.set(field , sum(list(map(lambda x : x.get("amount" , 0) , self.get(child_table)))) )
        
        
    def calculate_grand_total(self):
        self.grand_total = (self.total_amount or 0) + (self.asset_total_amount or 0) + ( self.items_total_amount or 0 )

            