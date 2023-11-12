frappe.ui.form.on("Purchase Receipt", {

    onload(frm){
      if (frm.is_new()){
        for (let i in frm.doc.items ){
          frm.doc.items[i].insurance_start_date = frm.doc.posting_date
        }
        frm.refresh_field("items")
      }

    },
    refresh(frm, cdt, cdn) {
      var d = locals[cdt][cdn];
       var html = [];
      for (let row in d.items) {
       html.push("<table  style='width:100%' >",
       "<thead >",
         "<tr>",
           "<th  height='25px' bgcolor='#687178' style='color:white; padding:10px'  colspan='2'>","<strong>","إسم الصنف","</strong>","</th>"
           ,
           "<th height='25px' bgcolor='#687178' style='color:white;'   colspan='2'>","<strong>",d.items[row].item_code,"</strong>","</th>"
           ,
         "</tr>",
       "</thead>",
     
       "<tbody>",
         "<tr  >",
           "<td style='color:#1f272e; padding:10px' height='20px'>","موقع الإستلام","</td>",
          //  "<td>","الموظف","</td>",
          //  "<td >","قسم","</td>",
          "<td >","مطلوب لقسم","</td>",
         "<td>","الشركة المنتجة","</td>",
           "<td>","موقع الصندوق","</td>",
         "</tr>",
         "<tr  bgcolor='#f9fafa' style='color:#1f272e'>",
           "<td style='color:#1f272e; padding:10px'>",d.items[row].custom_receipt_location,"</td>",
          //  "<td style='color:#1f272e; padding:10px'>",d.items[row].custom_employee,"</td>",
          //  "<td style='color:#1f272e; padding:10px'>",d.items[row].custom_department,"</td>",
          "<td style='color:#1f272e; padding:10px'>",d.items[row].custom_for_department,"</td>",
         "<td style='color:#1f272e; padding:10px'>",d.items[row].custom_vendor,"</td>",
           "<td style='color:#1f272e; padding:10px'>",d.items[row].custom_box_location,"</td>",
         "</tr>",
         "<tr  >",
         "<td style='color:#1f272e; padding:10px' height='20px'>","مطلوب لمشروع","</td>",
         "<td>","مطلوب بوسطة","</td>",
         "<td >","رقم القطعة","</td>",
         "<td>","سنة الصنع","</td>",
       "</tr>",
       "<tr  bgcolor='#f9fafa' style='color:#1f272e'>",
         "<td style='color:#1f272e; padding:10px'>",d.items[row].custom_requested_for_project,"</td>",
         "<td style='color:#1f272e; padding:10px'>",d.items[row].custom_requested_by,"</td>",
         
       "</tr>",
       "<tr  >",
       "<td style='color:#1f272e; padding:10px' height='20px'>","اسم","</td>",
       "<td>","الموديل","</td>",
       "<td colspan='2'>","وصف الصنف","</td>",

       "<td style='color:#1f272e; padding:10px'>",d.items[row].custom_part_number,"</td>",
       "<td style='color:#1f272e; padding:10px'>",d.items[row].custom_model_year,"</td>",
     "</tr>",
     "<tr  bgcolor='#f9fafa' style='color:#1f272e'>",
       "<td style='color:#1f272e; padding:10px'>",d.items[row].custom_name2,"</td>",
       "<td style='color:#1f272e; padding:10px'>",d.items[row].custom_model,"</td>",
      
     "</tr>",
     "<tr  >",
       "<td style='color:#1f272e; padding:10px' height='20px'>","تاريخ بدء الضمان او الدعم","</td>",
       "<td>","تاريخ نهاية الضمان او الدعم","</td>",
     "</tr>",
     "<tr  bgcolor='#f9fafa' style='color:#1f272e'>",
       "<td style='color:#1f272e; padding:10px'>",d.items[row].custom_insurance_start_date,"</td>",
       "<td style='color:#1f272e; padding:10px'>",d.items[row].custom_warranty_support_end_date,"</td>",
       "<td  colspan='2' style='color:#1f272e; padding:10px'>",d.items[row].custom_description,"</td>",
  
     "</tr>",
       "</tbody>",
         
     "</table>"
  );
      }
      let htmls = html.join(" ");
      console.log( htmls);
        frm.set_df_property(
          "custom_item_details_html",
          "options",
          `${htmls}`
        );
     
    },
  });
  
  // ********************************************************************************
  // frappe.ui.form.on('Purchase Receipt', {
  // onload(frm){
  //     frm.dashboard.hide();
  // 	}
  // });
  
  frappe.ui.form.on('Purchase Receipt Item', {
      validate(frm, cdt, cdn) {
         var d = locals[cdt][cdn];
          frm.set_value(d.rate, 1);
      },
      items_add(frm, cdt , cdn){
        let current_row = locals[cdt][cdn];
        current_row.insurance_start_date = frm.doc.posting_date ;
        refresh_field("items") ;
      }
      
  });
  // frappe.ui.form.on('Purchase Receipt Item', {
  // 	item_code(frm, cdt, cdn) {
  // 	   var d = locals[cdt][cdn];
  // 	   let location1= "الفرع الرئيسي";
  //     frappe.model.set_value(cdt, cdn, "location2", "");
  
  
  //     frappe.model.set_value(cdt, cdn, "location2", location1);
  //       frm.add_fetch('location2','employee','employee');
  //       frm.add_fetch('location2','department','department');
  //         frm.refresh_field(cdt, cdn, "location2");
  // 	   	}
  // });