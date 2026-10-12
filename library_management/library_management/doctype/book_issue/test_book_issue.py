# Copyright (c) 2026, dev and Contributors
# See license.txt

import frappe
from frappe.tests.utils import FrappeTestCase
class TestBookIssue(FrappeTestCase):
	def test_max_books_limit_exception(self):
		# Verify that attempting to issue more than 3 books raises a ValidationError
		issue = frappe.get_doc({ "doctype": "Book Issue", "library_member": "MEM-00001", "books": [ {"book": "BOOK-00001"}, {"book": "BOOK-00002"}, {"book": "BOOK-00003"}, {"book": "BOOK-00004"} ] })
		# Assert that frappe.ValidationError is thrown
		self.assertRaises(frappe.ValidationError, issue.insert)

# # import frappe
# from frappe.tests import IntegrationTestCase


# # On IntegrationTestCase, the doctype test records and all
# # link-field test record dependencies are recursively loaded
# # Use these module variables to add/remove to/from that list
# EXTRA_TEST_RECORD_DEPENDENCIES = []  # eg. ["User"]
# IGNORE_TEST_RECORD_DEPENDENCIES = []  # eg. ["User"]



# class IntegrationTestBookIssue(IntegrationTestCase):
# 	"""
# 	Integration tests for BookIssue.
# 	Use this class for testing interactions between multiple components.
# 	"""

# 	pass
