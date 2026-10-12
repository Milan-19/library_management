// Copyright (c) 2026, dev and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Book Issue", {
// 	refresh(frm) {

// 	},
// });

frappe.ui.form.on("Book Issue", {
	refresh(frm) {
		// Add custom quick-action button
		if (frm.doc.docstatus === 0) {
			frm.add_custom_button(__("Check Member Eligibility"), function () {
				if (frm.doc.library_member) {
					frappe.msgprint(
						__("Member ") +
							frm.doc.library_member +
							__(" is eligible to issue books."),
					);
				} else {
					frappe.throw(__("Please select a Library Member first."));
				}
			});
		}
	},
});
// Update book count dynamically when rows are added or removed
frappe.ui.form.on("Issue Book Item", {
	books_add(frm) {
		update_total_books(frm);
	},
	books_remove(frm) {
		update_total_books(frm);
	},
});
function update_total_books(frm) {
	let count = (frm.doc.books || []).length;
	frm.set_value("total_books", count);

	// DYNAMIC LOOKUP: Fetch max limit directly from Library Settings
	frappe.db.get_single_value("Library Settings", "max_books_per_member").then((max_books) => {
		let limit = max_books || 3; // Fallback to 3 if not configured

		if (count > limit) {
			frappe.show_alert({
				message:
					__("Warning: Maximum ") +
					limit +
					__(" books allowed per transaction (configured in Library Settings)!"),
				indicator: "red",
			});
		}
	});
}
