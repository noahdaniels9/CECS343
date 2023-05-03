from tenant import *
from room import *
from payment import *
from expense import *
from helper import *


# The path to all database files
tenant_filename = "C:/Users/alexa/PycharmProjects/343Project/Tenants.txt"
room_filename = "C:/Users/alexa/PycharmProjects/343Project/Rooms.txt"
payment_filename = "C:/Users/alexa/PycharmProjects/343Project/Payments.txt"
expense_filename = "C:/Users/alexa/PycharmProjects/343Project/Expenses.txt"
category_filename = "C:/Users/alexa/PycharmProjects/343Project/Categories.txt"

def login():
    """Handles logging in"""
    print_color("APARTMENT MANAGEMENT SYSTEM", "first")
    print_color("LOG IN", "third")

    print("Username: John")
    while True:
        password = input("Password: ")
        if password == "johnsnow":
            print_color("Login successful!\n", "success")
            return
        print_color("Incorrect password\n", "error")


def main_menu() -> int:
    """Handles displaying program's main menu"""
    print_color("APARTMENT MANAGEMENT SYSTEM", "first")
    print_color("MENU", "third")

    choice = input("1. Display Tenant List\n"
                   "2. Display Room List\n"
                   "3. Display Rental Income Record\n"
                   "4. Display Expense Record\n"
                   "5. Display Annual Summary\n"
                   "6. Log Out\n\n"
                   "Your choice: ")

    # Check if choice is a valid
    if validate_input(choice, 7):
        return int(choice)


def tenant_management():  # DONE
    """
    Handles all operations regarding tenants, including display, add and remove tenant.
    """
    # Get user choice and call corresponding functions
    while True:
        Tenant.display_all()
        choice = Tenant.tenant_menu()

        if choice == 1:
            Room.read_from_database(room_filename)
            Tenant.add_tenant(room_list)
        elif choice == 2:
            Tenant.remove_tenant()
        elif choice == 3:
            break

        # Update changes to database
        if choice == 1 or choice == 2:
            Tenant.write_to_database(tenant_filename)


def room_management():
    """
    Handles all operations regarding rooms, including display all rooms, add room, remove room, and adjust rent
    """
    while True:
        Room.display_all()
        choice = Room.room_menu()

        if choice == 1:
            Room.add_room()
        elif choice == 2:
            Tenant.read_from_database(tenant_filename)
            Room.remove_room(tenant_list)
        elif choice == 3:
            Room.adjust_rent()
        elif choice == 4:
            break

        Room.write_to_database(room_filename)
        Tenant.write_to_database(tenant_filename)


def payment_management():
    """
    Handles all operations regarding payments, including display all payments, record a payment and change rent.
    """
    # Get user choice and call corresponding functions
    while True:
        Payment.display_all()
        choice = Payment.payment_menu()

        if choice == 1:
            Payment.add_payment()
        elif choice == 2:
            Payment.edit_payment()
        elif choice == 3:
            Payment.new_text_file()
        elif choice == 4:
            break

        # Update changes to database
        if choice == 1 or choice == 2:
            Payment.write_to_database(payment_filename)


def expense_management(): # DONE
    """
    Handles all operations regarding expense, including display all expenses and record an expense.
    """
    # Get user choice and call corresponding functions
    while True:
        Expense.display_all()
        choice = Expense.expense_menu()

        if choice == 1:
            Expense.add_expense()
        elif choice == 2:
            Expense.remove_expense()
        elif choice == 3:
            break

        # Update changes to database
        if choice == 1 or choice == 2:
            Expense.write_to_database(expense_filename)
            Expense.save_categories(category_filename)


def reports():
    """
    Handles all operations regarding reports, including all payment records, all expense records, expenses by
    categories, profits and losses
    """
    print_color("ANNUAL REPORTS", "second")
    print_color("SUMMARY", "third")

    all_payments = Payment.sum_all_payments()
    all_expenses = Expense.sum_all_expenses()
    profit = all_payments - all_expenses

    print(tabulate([["TOTAL INCOME", f"${all_payments:,}"],
                    ["TOTAL EXPENSE", f"${all_expenses:,}"],
                    ["PROFIT" if profit > 0 else "LOSS", f"${profit:,}"]], tablefmt="rounded_grid"))

    print_color("EXPENSE BY CATEGORY", "third")
    print(tabulate([[key, f"${value:,}"] for key, value in Expense.sum_expenses_by_category().items()], tablefmt="rounded_grid", headers=["CATEGORY", "TOTAL"]))


if __name__ == '__main__':
    login()

    # Load all data from database
    Tenant.read_from_database(tenant_filename)
    Room.read_from_database(room_filename)
    Payment.read_from_database(payment_filename)
    Expense.read_from_database(expense_filename)
    Expense.load_categories(category_filename)

    while True:
        choice = main_menu()

        if choice == 6:
            print_color("LOGGED OUT", "success")
            break

        if choice == 1:
            tenant_management()
        elif choice == 2:
            room_management()
        elif choice == 3:
            payment_management()
        elif choice == 4:
            expense_management()
        elif choice == 5:
            reports()
