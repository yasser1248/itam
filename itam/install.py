
from frappe.core.doctype.data_import.data_import import import_doc
import frappe
import click
import os


@frappe.whitelist()
def install_doctypes_data_before_install() :
    """ When app install will add any json files in folder files to database """
    all_files_in_folders = os.listdir( frappe.get_app_path("itam" ,"files"))
    click.secho("Install Doctypes From Files  => {}".format( " , ".join(all_files_in_folders)), fg="green")
    for file in all_files_in_folders:
        import_doc(frappe.get_app_path("itam" ,"files/" + f"{file}"))
        frappe.db.commit()