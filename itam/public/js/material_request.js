frappe.ui.form.on("Material Request", {
    refresh(frm){
        frm.set_df_property('material_request_type', 'options', ['Purchase', 'Material Transfer' , 'Material Issue'])
        frm.refresh_field('material_request_type');

    }

})