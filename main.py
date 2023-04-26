from tenant import *
from room import *
from payment import *
from expense import *

# The path to all database files
tenant_filename = "/Users/vinhhuynh/Documents/CSULB/CECS 343/343 Project/Tenants.txt"
room_filename = "/Users/vinhhuynh/Documents/CSULB/CECS 343/343 Project/Rooms.txt"
payment_filename = "/Users/vinhhuynh/Documents/CSULB/CECS 343/343 Project/Payments.txt"
expense_filename = "/Users/vinhhuynh/Documents/CSULB/CECS 343/343 Project/Expenses.txt"


def login():
    """Handles logging in"""
    print("APARTMENT MANAGEMENT SYSTEM\n"
          "LOG IN\n")

    print("Username: John")
    while True:
        password = input("Password: ")
        if password == "johnsnow":
            print("Login successful!\n")
            return
        print("Incorrect password\n")


def main_menu() -> int:
    """Handles displaying program's main menu"""
    choice = input("\nMENU\n"
                   "1. Tenant Management\n"
                   "2. Rental Income Management\n"
                   "3. Expense Management\n"
                   "4. Annual Summary\n"
                   "5. Log Out\n\n"
                   "Your choice: ")

    # Check if choice is a number
    try:
        choice = int(choice)
    except ValueError:
        print("Please enter a number.")

    # Check if choice is in range
    if choice in range(6):
        return choice
    else:
        print("Invalid choice.\n")


def tenant_management():  # DONE
    """
    Handles all operations regarding tenants, including display, add and remove tenant.
    """
    # Get user choice and call corresponding functions
    while True:
        Tenant.display_all()
        choice = Tenant.tenant_menu()

        if choice == 1:
            Tenant.add_tenant()
        elif choice == 2:
            Tenant.remove_tenant()
        elif choice == 3:
            break

    # Update changes to database
    if choice == 1 or choice == 2:
        Tenant.write_to_database(tenant_filename)


def payment_management():
    """
    Handles all operations regarding payments, including display all payments, record a payment and change rent.
    """
    pass


def expense_management():
    """
    Handles all operations regarding expense, including display all expenses and record an expense.
    """
    pass


def reports():
    """
    Handles all operations regarding reports, including all payment records, all expense records, expenses by
    categories, profits and losses
    """
    pass


if __name__ == '__main__':
    login()
    print("Welcome To Apartment Management System")

    # Load all data from database
    Tenant.read_from_database(tenant_filename)
    Room.read_from_database(room_filename)
    Payment.read_from_database(payment_filename)
    Expense.read_from_database(expense_filename)

    while True:
        choice = main_menu()

        if choice == 5:
            print("Logging out...")
            break

        if choice == 1:
            tenant_management()
        elif choice == 2:
            payment_management()
        elif choice == 3:
            expense_management()
        elif choice == 4:
            reports()
