
import frappe
from frappe import _
from erpnext.stock.doctype.purchase_receipt.purchase_receipt import PurchaseReceipt
from frappe.utils import flt

class CustomPurchaseReceipt(PurchaseReceipt):
    
    def make_asset(self, row, is_grouped_asset=False):
        if not row.asset_location:
            frappe.throw(_("Row {0}: Enter location for the asset item {1}").format(row.idx, row.item_code))

        item_data = frappe.db.get_value(
            "Item", row.item_code, ["asset_naming_series", "asset_category"], as_dict=1
        )

        if is_grouped_asset:
            purchase_amount = flt(row.base_amount + row.item_tax_amount)
        else:
            purchase_amount = flt(row.base_rate + row.item_tax_amount)

        asset = frappe.get_doc(
            {
                "doctype": "Asset",
                "item_code": row.item_code,
                "asset_name": row.item_name,
                "naming_series": item_data.get("asset_naming_series") or "AST",
                "asset_category": item_data.get("asset_category"),
                "location": row.asset_location,
                "company": self.company,
                "supplier": self.supplier,
                "purchase_date": self.posting_date,
                "calculate_depreciation": 0,
                "purchase_receipt_amount": purchase_amount,
                "gross_purchase_amount": purchase_amount,
                "asset_quantity": row.qty if is_grouped_asset else 0,
                "purchase_receipt": self.name  ,
                "cost_center": row.cost_center,
                "warehouse" : self.set_warehouse ,
                # New
                "insurance_start_date" : row.insurance_start_date  ,
                "insurance_end_date" : row.insurance_end_date ,
                "custom_vendor" : row.custom_vendor ,
                "custom_part_number" : row.custom_part_number ,
                "custom_model_year" : row.custom_model_year ,
                "custom_model" : row.custom_model ,
                "custom_description": row.description,
                "maintenance_required": row.custom_maintenance_required,
                "available_for_use_date" : self.posting_date , 
                "custom_support_policy" : row.custom_support_policy 
                
            }
        )
        asset.flags.ignore_validate = True
        asset.flags.ignore_mandatory = True
        asset.set_missing_values()
        asset.insert()
        
        return asset.name


