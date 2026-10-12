# Copyright (c) 2026, dev and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class BookIssue(Document):
	def validate(self):
		self.total_books = len(self.books)

		# Dynamically fetch limit from Library Settings
		max_books = frappe.db.get_single_value("Library Settings", "max_books_per_member") or 3
		
		if self.total_books > max_books:
			frappe.throw(f"Members cannot issue more than {max_books} books at once (configured in Library Settings)!")