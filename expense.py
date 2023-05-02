import csv
from datetime import datetime, date
from tabulate import tabulate
from helper import print_color, validate_input
from category import category_list

# List of expense objects read from file
expense_list = []


class Expense:
    date: datetime.date
    payee: str
    amount: int
    category: str

    def __init__(self, date: datetime.date, payee, amount, category):
        self.date = date
        self.payee = payee
        self.amount = amount
        self.category = category

    def __iter__(self):
        for attribute in [self.date, self.payee, self.amount, self.category]:
            yield attribute

    @staticmethod
    def expense_menu() -> int:
        """Display all available menu options for managing expenses"""
        print_color("EXPENSE MANAGEMENT", "second")
        print_color("MENU", "third")

        choice = input("1. Add an expense\n"
                       "2. Remove an expense\n"
                       "3. Return to main menu\n\n"
                       "Your choice: ")

        # Check if choice is a number
        if validate_input(choice, 4):
            return int(choice)

    @staticmethod
    def display_all():
        """Display all expenses"""
        print_color("EXPENSE LIST", "third underline")
        print(tabulate(expense_list, headers="firstrow", tablefmt="fancy_grid", showindex=range(1, len(expense_list))))

    @staticmethod
    def add_expense():
        print_color("ADDING AN EXPENSE", "third")
        print_color("Enter 0 to quit", "info")

        choice = input("EXPENSE DATE\n"
                       "1. Today\n"
                       "2. Custom date\n"
                       "Your choice: ")

        if validate_input(choice, 3) is False or choice == "0":
            return

        if choice == "1":
            date = datetime.today().strftime('%Y-%m-%d')
        elif choice == "2":
            while True:
                try:
                    date = datetime.strptime(input("Input date (YYYY-MM-DD): "), '%Y-%m-%d').date()
                except ValueError:
                    print_color("Invalid date format.", "error")
                else:
                    break

        payee = input("\nPayee: ")
        amount = input("\nAmount: ")

        print("\nCATEGORIES")
        print("Press 0 to add a new category")
        for i in range(len(category_list)):
            print(f"{i+1}. {category_list[i]}")

        while True:
            choice = input("Choose category: ")

            if choice == "0":
                category = input("Enter new category: ")
                category_list.append(category)
                break

            if validate_input(choice, len(category_list)+1):
                category = category_list[int(choice)-1]
                break
            else:
                print_color("Invalid choice", "error")

        expense_list.append(Expense(date, payee, amount, category))

    @staticmethod
    def remove_expense():
        print_color("REMOVING AN EXPENSE", "third")
        print_color("Enter 0 to quit\n", "info")

        choice = input("Enter expense index number: ")
        if choice == "0":
            return

        if validate_input(choice, len(expense_list)):
            choice = int(choice)
            expense_list.pop(choice)
            print_color("Expense removed", "success")
        else:
            print_color("Expense not found", "error")

    @staticmethod
    def read_from_database(filename):
        """Read all expense information from the database into memory"""
        with open(filename, 'r') as fp:
            reader = csv.reader(fp, delimiter=',')
            for row in reader:
                try:
                    date = datetime.strptime(row[0], '%Y-%m-%d').date()
                except ValueError:
                    expense_list.append(Expense(row[0], row[1], row[2], row[3]))
                else:
                    expense_list.append(Expense(date, row[1], row[2], row[3]))

    @staticmethod
    def write_to_database(filename):
        """Write all expense information from memory into the database"""
        with open(filename, 'w') as fp:
            writer = csv.writer(fp, delimiter=',')
            for expense in expense_list:
                writer.writerow([expense.date, expense.payee, expense.amount, expense.category])
