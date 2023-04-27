import csv
from datetime import datetime
from tabulate import tabulate
from helper import print_color, validate_input

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
        print(tabulate(expense_list, headers="firstrow", tablefmt="fancy_grid"))

    @staticmethod
    def add_expense():
        pass

    @staticmethod
    def remove_expense():
        pass

    @staticmethod
    def read_from_database(filename):
        """Read all expense information from the database into memory"""
        with open(filename, 'r') as fp:
            reader = csv.reader(fp, delimiter=',')
            for row in reader:
                try:
                    date = datetime.strptime(row[0], '%Y/%m/%d').date()
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