// Copyright (c) 2023, IT Systematic and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Asset Count By Lifecycle State"] = {
	"filters": [

	],
	"formatter": function(value, row, column, data, default_formatter) {
		value = default_formatter(value, row, column, data);
		column.align = "left"
		return value;
	},
};

