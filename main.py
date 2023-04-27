from tenant import *
from room import *
from payment import *
from expense import *
from termcolor import colored
from display import *

# The path to all database files
tenant_filename = "#FIX- add your own path for text files"
room_filename = "#FIX- add your own path for text files"
payment_filename = "#FIX- add your own path for text files"
expense_filename = "#FIX- add your own path for text files"


def login():
    """Handles logging in"""
    print(colored("APARTMENT MANAGEMENT SYSTEM".center(Width.full), Color.primary, attrs=["bold", "underline"]))
    print(colored("LOGIN\n".center(Width.full), Color.secondary))

    print("Username: John")
    while True:
        password = input("Password: ")
        if password == "johnsnow":
            print(colored("Login successful!\n".center(Width.full), Color.success))
            return
        print(colored("Incorrect password\n".center(Width.full), Color.error))


def main_menu() -> int:
    """Handles displaying program's main menu"""
    print(colored("APARTMENT MANAGEMENT SYSTEM".center(Width.full), Color.primary, attrs=["bold", "underline"]))
    print(colored("MENU\n".center(Width.full), Color.secondary))

    choice = input("1. Tenant Management\n"
                   "2. Rental Income Management\n"
                   "3. Expense Management\n"
                   "4. Annual Summary\n"
                   "5. Log Out\n\n"
                   "Your choice: ")

    # Check if choice is a number
    try:
        choice = int(choice)
    except ValueError:
        print(colored("Please enter a number".center(Width.full), Color.error))
    else:
        # Check if choice is in range
        if choice in range(6):
            return choice
        else:
            print(colored("Invalid choice".center(Width.full), Color.error))


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
