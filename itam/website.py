import frappe


def get_home_page(user):
    if frappe.session.user != "Guest":
        return "home"
    else:
        return "login"