


frappe.ui.form.on('Asset Movement', {
	set_required_fields: (frm, cdt, cdn) => {
		let fieldnames_to_be_altered;
		if (frm.doc.purpose === 'Transfer') {
			fieldnames_to_be_altered = {
				target_location: { read_only: 0, reqd: 1 },
				source_location: { read_only: 1, reqd: 1 },
				from_employee: { read_only: 1, reqd: 0 },
				to_employee: { read_only: 1, reqd: 0 },
                box_location : { read_only : 1 , reqd : 0},
				custom_is_loan : { hidden : 1 },
                // custom_to_date : { read_only : 1 , reqd : 0},
			};
		}
		else if (frm.doc.purpose === 'Receipt') {
			fieldnames_to_be_altered = {
				target_location: { read_only: 0, reqd: 1 },
				source_location: { read_only: 1, reqd: 0 },
				from_employee: { read_only: 0, reqd: 0 },
				to_employee: { read_only: 1, reqd: 0 } ,
                box_location : { read_only : 1 , reqd : 0} ,
				custom_is_loan : { hidden : 1 },
				// custom_is_loan : { hidden : 1 , reqd : 0},
                // custom_to_date : { read_only : 1 , reqd : 0},
			};
		}
		else if (frm.doc.purpose === 'Issue') {
			fieldnames_to_be_altered = {
				target_location: { read_only: 1, reqd: 0 },
				source_location: { read_only: 1, reqd: 0 },
				from_employee: { read_only: 1, reqd: 0 },
				to_employee: { read_only: 0, reqd: 1 } ,
                box_location : { read_only : 0 , reqd : 1},
                custom_is_loan : { hidden : 0  , reqd : 1}
                // custom_to_date : { read_only : 0 },
			};
		}
		if (fieldnames_to_be_altered) {
			Object.keys(fieldnames_to_be_altered).forEach(fieldname => {
				let property_to_be_altered = fieldnames_to_be_altered[fieldname];
				Object.keys(property_to_be_altered).forEach(property => {
					let value = property_to_be_altered[property];
					frm.fields_dict['assets'].grid.update_docfield_property(fieldname, property, value);
				});
			});
			frm.refresh_field('assets');
		}
	}





})