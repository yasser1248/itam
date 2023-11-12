// Copyright (c) 2023, IT Systematic and contributors
// For license information, please see license.txt

frappe.ui.form.on('Next Year Plaining', {
	onload: function(frm) {
		if (frm.is_new() ) {
			add_items_in_tables(frm)
		}

	},
	items_total_amount(frm) {
		frm.trigger("calculate_grand_total")
	},
	
	calculate_grand_total(frm) {
		let grand_total = (frm.doc.total_amount || 0) + (frm.doc.asset_total_amount || 0) + (frm.doc.items_total_amount || 0)
		frm.set_value("grand_total" , grand_total)
	}

});


frappe.ui.form.on('Items Details', {
	price(frm, cdt, cdn) {
		calculate_total_amount(frm)
	},
	items_details_remove(frm , cdt , cdn) {
		calculate_total_amount(frm)
	}
});


function add_items_in_tables(frm){
	frm.call({
		method: "add_items_in_tables",
		doc: frm.doc

	})
}



function calculate_total_amount(frm) {
	let total_amount = 0 ;
	frm.doc.items_details.forEach(element => {
		total_amount += element.price
	});
	frm.set_value("items_total_amount" , total_amount);
	frm.refresh_field("items_total_amount")
}

