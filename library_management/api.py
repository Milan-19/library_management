import frappe

@frappe.whitelist(allow_guest=True)
def check_book_status(isbn):
    """Check availability of a book by ISBN."""
    book = frappe.db.get_value("Book", {"isbn": isbn}, ["name", "title", "author", "is_available"], as_dict=True)
    if not book:
        return {"status": "Not Found", "message": f"No book found with ISBN {isbn}"}
    return {"status": "Success", "book": book}