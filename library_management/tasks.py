import frappe
import time
def process_overdue_fines_heavy():
    """Simulate a heavy long-running fine calculation batch."""
    time.sleep(5)
    # Simulate 5-second computation
    frappe.logger().info("Overdue fine batch calculations complete!")
    
@frappe.whitelist(allow_guest=True)
def enqueue_overdue_calculation():
    """Whitelisted method to trigger background processing."""
    frappe.enqueue( method="library_management.tasks.process_overdue_fines_heavy", queue="short", timeout=300 )
    return {"status": "Queued", "message": "Fine calculation job offloaded to Redis worker!"}