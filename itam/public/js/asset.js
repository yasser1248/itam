frappe.ui.form.on("Asset", {

    refresh(frm) {
        let now_date = frappe.datetime.nowdate();
        let end_dat = frm.selected_doc.insurance_end_date;
        let remaining_days = frappe.datetime.get_diff(end_dat, now_date);
        frm.set_value('remaining_days', remaining_days);
    },


    // validate(frm) {
    //     frm.set_value('sku', frm.doc.name);
    // },


    before_save(frm, cdt, cdn) {
        var doc = locals[cdt][cdn];
        if (doc.requested_by) {
            frm.add_fetch("requested_by", "user_id", "user_id");
            frappe.call({
                method: "frappe.share.add",
                args: {
                    doctype: "Asset",
                    name: doc.name,
                    user: doc.user_id,
                    read: 1,
                    write: 0,
                    share: 0,
                    everyone: 0,
                },
            });
        }
    },


    insurance_end_date(frm) {
        let now_date = frappe.datetime.nowdate();
        let end_dat = frm.selected_doc.insurance_end_date;
        let remaining_days = frappe.datetime.get_diff(end_dat, now_date);
        frm.set_value('remaining_days', remaining_days);
    },

});

