from . import __version__ as app_version
from frappe import _

app_name = "itam"
app_title = "Itam"
app_publisher = "IT Systematic"
app_description = "IT Assets Management"
app_email = "ahmeddesoky412@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/itam/css/itam.css"
# app_include_js = "/assets/itam/js/itam.js"

# include js, css files in header of web template
# web_include_css = "/assets/itam/css/itam.css"
# web_include_js = "/assets/itam/js/itam.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "itam/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
doctype_js = {
    "Purchase Receipt": "public/js/purchase_receipt.js",
    "Material Request": "public/js/material_request.js" ,
    "Asset Movement" : "public/js/asset_movement.js"

}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# "methods": "itam.utils.jinja_methods",
# "filters": "itam.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "itam.install.before_install"
# after_install = "itam.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "itam.uninstall.before_uninstall"
# after_uninstall = "itam.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "itam.utils.before_app_install"
# after_app_install = "itam.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "itam.utils.before_app_uninstall"
# after_app_uninstall = "itam.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "itam.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# "Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# "Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

override_doctype_class = {
    "Purchase Receipt": "itam.override.override_class.purchase_receipt.CustomPurchaseReceipt",
    "Asset Movement": "itam.override.override_class.asset_movement.CustomAssetMovement",
}

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
    "Asset": {
        "after_insert": ["itam.doc_events.asset.add_barcode_after_insert" ,"itam.doc_events.asset.add_differ_date" ],
    }
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# "all": [
# "itam.tasks.all"
# ],
# "daily": [
# "itam.tasks.daily"
# ],
# "hourly": [
# "itam.tasks.hourly"
# ],
# "weekly": [
# "itam.tasks.weekly"
# ],
# "monthly": [
# "itam.tasks.monthly"
# ],
# }

# Testing
# -------

# before_tests = "itam.install.before_tests"

# Overriding Methods
# ------------------------------
#
override_whitelisted_methods = {
    "erpnext.buying.doctype.purchase_order.purchase_order.make_purchase_receipt": "itam.override.whitelisted_methods.purchase_order.make_purchase_receipt"
# "frappe.desk.doctype.event.event.get_events": "itam.event.get_events"
}
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# "Task": "itam.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents

# -----------------------------------------------------------
# control website homepage
get_website_user_home_page = "itam.website.get_home_page"

# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["itam.utils.before_request"]
# after_request = ["itam.utils.after_request"]

# Job Events
# ----------
# before_job = ["itam.utils.before_job"]
# after_job = ["itam.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# {
# "doctype": "{doctype_1}",
# "filter_by": "{filter_by}",
# "redact_fields": ["{field_1}", "{field_2}"],
# "partial": 1,
# },
# {
# "doctype": "{doctype_2}",
# "filter_by": "{filter_by}",
# "partial": 1,
# },
# {
# "doctype": "{doctype_3}",
# "strict": False,
# },
# {
# "doctype": "{doctype_4}"
# }
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# "itam.auth.validate"
# ]

fixtures = [
    {
        "dt": ("Property Setter"),
        "filters": [
            ["doc_type", "in", ("Asset","Asset Movement","Delivery Note","Delivery Note Item",
                                "Department","Employee","Issue","Item","Item Barcode","Material Request",
                                "Material Request Item","Purchase Invoice","Purchase Invoice Item","Purchase Order",
                                "Purchase Order Item","Purchase Receipt","Purchase Receipt Item","Quotation","Request for Quotation",
                                "Salary Slip","Sales Invoice","Sales Invoice Item","Supplier Quotation","Stock Entry","Stock Entry Detail",
                                "Stock Reconciliation","Stock Reconciliation Item","Supplier","Support Policy")],
            ["field_name", "in", (
            # Asset
            
            "other_details",
            "other_details",
            "calculate_depreciation",
            "insured_value",
            "insured_value",
            "insured_value",
            "insurer",
            "insurer",
            "insurer",
            "comprehensive_insurance",
            "comprehensive_insurance",
            "comprehensive_insurance",
            "comprehensive_insurance",
            "insurance_end_date",
            "insurance_start_date",
            "insurance_details",
            "insurance_details",
            "section_break_23",
            "purchase_details_section",
            "accounting_dimensions_section",
            "accounting_dimensions_section",
            "company",
            "asset_owner",
            "company",
            "department",
            "policy_number",
            "policy_number",
            "asset_quantity",
            
            #Asset Movement
            "purpose",
            "purpose",
            
            #Delivery Note
            "scan_barcode",
            "in_words",
            "in_words",
            "disable_rounded_total"
            "rounded_total",
            "rounded_total",
            "base_rounded_total",
            "base_rounded_total",
            "tax_id",
            "tax_id",
            
            #Delivery Note Item
            "target_warehouse",
            "barcode",
            
            #Department
            "department_name",
            
            #Employee
            "salutation",
            "naming_series",
            "employee_number",
            "naming_series",
            "naming_series",
            "naming_series",
            "naming_series",
            "first_name",
            "employee_name",
            "employee_name",
            "date_of_joining",
            "date_of_birth",
            "column_break1",
            "column_break1",
            "date_of_joining",
            "date_of_birth",
            "first_name",
            "last_name",
            "middle_name",
            "company_details_section",
            "gender",
            "connections_tab",
            "exit",
            "profile_tab",
            "personal_details",
            "salary_information",
            "attendance_and_leave_details",
            "contact_details",
            "employment_details",
            
            #Issue
            "contact",
            "email_account",
            "contact",
            "via_customer_portal",
            "company",
            "project",
            "customer_name",
            "lead",
            "customer", 
            
            #Item
            "barcodes",
            "item_code",
            "item_code",
            "naming_series",
            "naming_series",
            "inspection_required_before_purchase",
            "naming_series",
            "auto_create_assets",
            "allow_alternative_item",
            "include_item_in_manufacturing",
            "has_variants",
            "is_stock_item",
            "is_fixed_asset",
            "standard_rate",
            "section_break_11",
            "manufacturing",
            "quality_tab",
            "item_tax_section_break",
            "sales_details",
            "purchasing_tab",
            "accounting",
            "variants_section",
            "inventory_section",
            "dashboard_tab",
            "is_zero_rated",
            "is_exempt",
            "brand",
            "section_break_11",
            "is_grouped_asset",
            
            #Item Barcode
            "barcode",
            
            #Material Request
            "scan_barcode",
            
            #Material Request Item
            "warehouse",
            "uom",
            "qty",
            
            #Purchase Invoice
            "scan_barcode", 
            "payment_schedule",
            "due_date",
            "in_words",
            "in_words",
            "disable_rounded_total",
            "rounded_total",
            "rounded_total",
            "base_rounded_total",
            "base_rounded_total",
            
            #Purchase Invoice Item
            "from_warehouse",
            
            #Purchase Order
            "additional_info_section",
            "subscription_section",
            "column_break5",
            "incoterm",
            "shipping_rule",
            "currency_and_price_list",
            "is_subcontracted",
            "apply_tds",
            "scan_barcode",
            "payment_schedule",
            "due_date",
            "in_words",
            "in_words",
            "disable_rounded_total",
            "rounded_total",
            "rounded_total",
            "base_rounded_total",
            "base_rounded_total",
            
            #Purchase Order Item
            "item_tax_template",
            
            #Purchase Receipt
            "is_subcontracted",
            "rejected_warehouse",
            "set_from_warehouse",
            "scan_barcode",
            "sec_warehouse",
            "provisional_expense_account",
            "terms_tab",
            "supplier_name_in_arabic",
            "supplier_name_in_arabic",
            "additional_info_section",
            "transporter_info",
            "printing_settings",
            "subscription_detail",
            "status_section",
            "company_trn",
            "billing_address_section",
            "section_break_98",
            "section_addresses",
            "raw_material_details",
            "pricing_rule_details",
            "sec_tax_breakup",
            "section_break_42",
            "section_break_46",
            "totals",
            "taxes_section",
            "taxes_charges_section",
            "section_break0",
            "project",
            "dimension_col_break",
            "cost_center",
            "accounting_dimensions_section",
            "accounting_dimensions_section",
            "currency_and_price_list",
            "currency_and_price_list",
            "return_against",
            "is_return",
            "apply_putaway_rule",
            "apply_putaway_rule",
            "company",
            "column_break_12",
            "column_break_12",
            "in_words",
            "disable_rounded_total",
            "rounded_total",
            "base_rounded_total",
            
            #Purchase Receipt Item
            "from_warehouse",
            "barcode",
            "qty",
            "item_code",
            "amount",
            "rejected_qty",
            "rate",
            "section_break_80",
            "accounting_dimensions_section",
            "manufacture_details",
            "item_weight_details",
            "allow_zero_valuation_rate",
            "section_break_45",
            "warehouse_and_reference",
            "discount_and_margin_section",
            "received_and_accepted",
            "billed_amt",
            "rate_difference_with_purchase_invoice",
            "landed_cost_voucher_amount",
            "base_net_amount",
            "base_net_rate",
            "column_break_32",
            "item_tax_template",
            "net_amount",
            "net_rate",
            "is_free_item",
            "stock_uom_rate",
            "base_amount",
            "col_break4",
            "uom",
            "uom",
            "uom",
            "rate_and_amount",
            "retain_sample",
            "is_exempt",
            "is_zero_rated",
            
            #Quotation
            "scan_barcode",
            "in_words",
            "in_words",
            "disable_rounded_total",
            "rounded_total",
            "rounded_total",
            "base_rounded_total",
            "base_rounded_total",
            
            #Request for Quotation
            "html_llwp",
            
            
            #Sales Invoice
            "scan_barcode",
            "payment_schedule",
            "due_date",
            "in_words",
            "in_words",
            "disable_rounded_total",
            "rounded_total",
            "rounded_total",
            "base_rounded_total",
            "base_rounded_total",
            "additional_discount_account",
            "additional_discount_account",
            "tax_id",
            "tax_id",
            
            #Sales Invoice Item
            "target_warehouse",
            "barcode",
            "discount_account",
            "discount_account",
            
            #Supplier Quotation
            "scan_barcode",
            "payment_schedule",
            "due_date",
            "in_words",
            "in_words",
            "disable_rounded_total",
            "rounded_total",
            "rounded_total",
            "base_rounded_total",
            "base_rounded_total",
            "tax_id",
            "tax_id",
            
            #Stock Entry
            "scan_barcode",
            
            #Stock Entry Detail
            "barcode",
            
            #Stock Reconciliation
            "scan_barcode",
            
            #Stock Reconciliation Item
            "barcode",
            
            #Supplier
            "naming_series",
            "naming_series",
            
            #Supplier Quotation
            "in_words",
            "in_words",
            "disable_rounded_total",
            "rounded_total",
            "rounded_total",
            "base_rounded_total",
            "base_rounded_total",
            
            #Support Policy
            "supporter",
            

            #     # Tab Breack in ITem Doctype
            #     "dashboard_tab",
            #     "inventory_section",
            #     "variants_section",
            #     "accounting",
            #     "purchasing_tab",
            #     "sales_details",
            #     "item_tax_section_break",
            #     "quality_tab",
            #     "manufacturing",
            #     # Fields in Item
            #     "standard_rate",
            #     "is_fixed_asset",
            #     "allow_alternative_item",
            #     "is_stock_item",
            #     "has_variants",
            #     "include_item_in_manufacturing",
            #     "auto_create_assets",
            #     "inspection_required_before_purchase",

            #     # Employee
            #     "connections_tab",
            #     "exit",
            #     "profile_tab",
            #     "personal_details",
            #     "salary_information",
            #     "attendance_and_leave_details",
            #     "contact_details",
            #     "employment_details",
            #     "gender",
            #     "last_name",
            #     "middle_name",
            #     "branch",
            #     "department",
            #     "first_name",
            #     "date_of_joining",
            #     "date_of_birth",
            #     "",
            #     "",

            #     # Purchase Receipt
            #     "supplier_name_in_arabic",
            #     "apply_putaway_rule",
            #     "is_return",
            #     "return_against",
            #     "column_break_12",
            #     "accounting_dimensions_section",
            #     "currency_and_price_list",
            #     "sec_warehouse",
            #     "section_break0",
            #     "taxes_charges_section",
            #     "taxes_section",
            #     "totals",
            #     "section_break_46",
            #     "section_break_42",
            #     "sec_tax_breakup",
            #     "pricing_rule_details",
            #     "raw_material_details",
            #     "section_addresses",
            #     "section_break_98",
            #     "billing_address_section",
            #     "status_section",
            #     "subscription_detail",
            #     "printing_settings",
            #     "transporter_info",
            #     "additional_info_section",
            #     "terms_tab",

            #     # Purchase Receipt Item
            #     "qty",
            #     "rejected_qty",
            #     "rate",
            #     "amount",

            )
            ]
        ]
    },
    {
        "dt": ("Custom Field"),
        "filters": [
            ["dt", "in", ("Asset", "Asset Movement Item","Material Request", "Purchase Receipt","Purchase Receipt Item","Item", "Employee","Issue","Support Policy")],
            ["fieldname", "in", (
                # Asset
                "custom_barcode",
                "custom_details",
                "custom_tab_break_ombaa",
                "custom_disposal",
                "custom_depreciation",
                "custom_insurance",
                "custom_vendor",
                "custom_model",
                "custom_po",
                "custom_sup",
                "custom_column_break_td0n2",
                "custom_from_date",
                "custom_column_break_z6yta",
                "custom_to_date",
                "custom_disposal1",
                "custom_disposal2",
                "custom_is_for_disposal",
                "custom_disposal_details",
                "custom_disposal_reason",
                "custom_beneficiary",
                "custom_resale_price",
                "custom_column_break_gqemc",
                "custom_scheduled_retirement",
                "custom_retired_date",
                "custom_is_loan",
                "custom_section_break_wiwav",
                "custom_section_break_eqnes",
                "custom_part_number",
                "custom_model_year",
                "warehouse",
                "branch",
                "mobile",
                "gender",
                "email",
                "serial_no",
                "life_cycle_status",
                "custom_description",
                "custom_mac_address",
                "custom_box_location",
                "custom_project",
                "custom_support_policy",
                "custom_section_break_glnrs",
                "custom_policy_details",
                "custom_days_",
                
                #Asset Movement Item
                "box_location",
                "custom_section_break_tjcwv",
                "custom_is_loan",
                "custom_from_date",
                "custom_column_break_qo54g",
                "custom_to_date",
                
                # Material Request
                "custudy",
                "location",
                "branch",
                "mobile",
                "gender",
                "column_break_lg2zo",
                "custodian",
                "department",
                "email",
                "section_break_cglzi",
                "is_loan",
                "section_break_oc6p1",
                "from_date",
                "column_break_4pjce",
                "to_date",
                # "workflow_state",
                "custom_request_type",
                
                # Purchase Receipt
                "custom_purchase_order_no",
                "custom_attached_document",
                "company_trn",
                "supplier_name_in_arabic",
                "custom_item_details",
                "custom_item_details_html",
                
                # Purchase Receipt Item
                "custom_asset_details",
                "custom_receipt_location",
                # "is_zero_rated",
                # "is_exempt",
                "custom_description",
                "custom_column_break_b1ogb",
                "custom_for_department",
                "custom_vendor",
                "custom_model",
                "custom_part_number",
                "custom_model_year",
                "custom_tax_rate",
                "custom_tax_amount",
                "insurance_start_date",
                "insurance_end_date",
                "custom_maintenance_required",
                "custom_vendor",
                "custom_support_policy",
                
                # Item
                "custom_asset_details",
                "custom_vendor",
                "custom_name2",
                "custom_model",
                "custom_part_number",
                "custom_model_year",
                "custom_column_break_jflhs",
                "custom_description",
                # "is_zero_rated",
                # "is_exempt",
                "custom_mac_address",

                # Employee
                "custom_contact",
                "custom_mobile",
                "custom_column_break_ujhbg",
                "custom_email",
                # "employment_type",
                # "job_applicant",
                # "grade",
                # "default_shift",
                # "health_insurance_section",
                # "health_insurance_provider",
                # "health_insurance_no",
                # "approvers_section",
                # "expense_approver",
                # "leave_approver",
                # "column_break_45",
                # "shift_request_approver",
                # "salary_cb",
                # "payroll_cost_center",
                
                #Issue
                "custom_employee",
                
                #Support Policy
                "custom_supporter",

                
                # Department
                # "section_break_4",
                # "payroll_cost_center",
                # "column_break_9",
                # "leave_block_list",
                # "approvers",
                # "shift_request_approver",
                # "leave_approvers",
                # "expense_approvers",
                
                # Address
                # "tax_category",
                # "is_your_company_address",
                # "address_in_arabic",
                
                # Contact
                # "is_billing_contact",
                
                # Customer
                # "customer_name_in_arabic",
                
                # Supplier
                # "supplier_name_in_arabic",
                
                # Purchase Invoice
                # "company_trn",
                # "supplier_name_in_arabic",
                
                # Purchase Invoice Item
                # "is_zero_rated",
                # "is_exempt",
                
                # Purchase Order
                # "company_trn",
                # "supplier_name_in_arabic",
                
                # Purchase Order Item
                # "is_zero_rated",
                # "is_exempt",
                
                # Sales Invoice
                # "company_trn",
                # "customer_name_in_arabic",
                # "ksa_einv_qr",
                
                # Sales Invoice Item
                # "is_exempt",
                # "is_zero_rated",
                
                # "custom_model",
                # "custom_part_number",
                # "custom_model_year",
                # "custom_tax_code",
                # "custom_tax_rate",
                # "custom_tax_amount",
                # "custom_total_amount",

            )
            ]
        ],
    },
    {
        "dt": ("Web Form"),
        "filters": [
            ["name", "in", ("issues-web","material-request-web","material-request","issues") ]
        ]
    },
    {
        "dt": ("Web Page"),
        "filters": [
            ["name", "in", ("home") ]
        ]
    },
    {
        "dt": ("Website Sidebar"),
        "filters": [
            ["name", "in", ("Home Page Sidebar") ]
        ]
    },
    {
        "dt": ("Portal Settings"),
    },
    {
        "dt": ("Website Settings"),
    },
]
