# Task 1: Customer Service Ticket Tracker Demonstrate your ability to use nested collections and loops by creating a system to 
# track customer service tickets.

# Problem Statement: Develop a program that:

# Tracks customer service tickets, each with a unique ID, customer name, issue description, and status (open/closed).
# Implement functions to:
# Open a new service ticket.
# Update the status of an existing ticket.
# Display all tickets or filter by status.
# Initialize with some sample tickets and include functionality for additional ticket entry.
# Example ticket structure:

# service_tickets = {
#     "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
#     "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
# }

service_tickets = {
    "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}

def open_ticket(ticket_id, customer, issue):
    """Open a new service ticket."""
    service_tickets[ticket_id] = {
        "Customer": customer,
        "Issue": issue,
        "Status": "open"
    }
    print(f"New ticket opened: {ticket_id}")

def update_ticket_status(ticket_id, status):
    """Update the status of an existing ticket."""
    if ticket_id in service_tickets:
        service_tickets[ticket_id]["Status"] = status
        print(f"Ticket {ticket_id} status updated to '{status}'.")
    else:
        print(f"Ticket {ticket_id} not found.")

def display_tickets():
    """Display all tickets."""
    print("Displaying all tickets:")
    for ticket_id, ticket in service_tickets.items():
        print(f"{ticket_id}: Customer: {ticket['Customer']}, Issue: {ticket['Issue']}, Status: {ticket['Status']}")

def main():
    display_tickets() 
    open_ticket("Ticket003", "Charlie", "Cannot access account") 
    update_ticket_status("Ticket001", "closed") 
    display_tickets()  

if __name__ == "__main__":
    main()