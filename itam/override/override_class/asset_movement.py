

from erpnext.assets.doctype.asset_movement.asset_movement import AssetMovement
import frappe

class CustomAssetMovement(AssetMovement):
    
    def set_latest_location_and_custodian_in_asset(self):
        current_location, current_employee = "", ""
        cond = "1=1"

        for d in self.assets:
            args = {"asset": d.asset, "company": self.company}

            latest_movement_entry = frappe.db.sql(
                """
                SELECT asm_item.target_location, asm_item.to_employee
                FROM `tabAsset Movement Item` asm_item, `tabAsset Movement` asm
                WHERE
                    asm_item.parent=asm.name and
                    asm_item.asset=%(asset)s and
                    asm.company=%(company)s and
                    asm.docstatus=1 and {0}
                ORDER BY
                    asm.transaction_date desc limit 1
                """.format(
                    cond
                ),
                args,
            )
            if latest_movement_entry:
                current_location = latest_movement_entry[0][0]
                current_employee = latest_movement_entry[0][1]
                
            current_employee_details = frappe.get_doc("Employee" ,current_employee ) if current_employee else None
            
            asset_details = {
                "location" : current_location ,
                "custodian" : current_employee ,
                "branch" : current_employee_details.branch if current_employee_details else None,
                "mobile" : current_employee_details.custom_mobile if current_employee_details else None,
                "gender" : current_employee_details.gender if current_employee_details else None,
                "email" : current_employee_details.custom_email if current_employee_details else None,
                "department" : current_employee_details.department if current_employee_details else None,
                # "box_location" : d.box_location if self.purpose =="Issue" else None ,
            }
            
            if self.purpose =="Issue"  and self.docstatus == 1 :
                asset_details["custom_box_location"] = d.box_location
                if d.custom_is_loan == 1 :
                    asset_details['custom_is_loan'] = d.custom_is_loan
                    asset_details['custom_from_date'] = d.custom_from_date
                    asset_details['custom_to_date'] = d.custom_to_date
            
            
            frappe.db.set_value("Asset" , d.asset , asset_details)
            frappe.db.commit()

        
