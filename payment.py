import csv
from tabulate import tabulate
from helper import print_color, validate_input

# List of room objects read from file
payment_list = []

class Payment:
    def __init__(self, name):
        self.name = name
        self.payment_list = []



    def add_payment(self, pay_amount):
        self.payment_list.append(pay_amount)
    def print_paylist(self):
        print(self.name, "'s payment list:")
        table = [["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"], self.payment_list]
        print(tabulate(table))
        pass

    @classmethod
    def read_from_database(cls, payment_filename):
        """Read all tenant information from the database into memory"""
        with open(payment_filename, 'r') as fp:
            reader = csv.reader(fp, delimiter=',')
            for row in reader:
                payment_list.append(Payment(row[0], row[1]))

    @staticmethod
    def write_to_database(payment_filename):
        """Write all tenant information from memory into the database"""
        with open(payment_filename, 'w') as fp:
            writer = csv.writer(fp, delimiter=',')
            for room in payment_list:
                writer.writerow([room.number, room.rent])

    @staticmethod
    def payment_menu() -> int:
        """Display all available menu options for managing tenants"""
        print_color("INCOME RECORD MANAGEMENT", "second")
        print_color("MENU", "third")

        choice = input("1. Add a new payment\n"
                       "2. Edit a payment"
                       "3. Make a new list for different year\n"
                       "4. Return to main menu\n\n"
                       "Your choice: ")

        # Check if choice is a good input
        if validate_input(choice, 5):
            return int(choice)

    @staticmethod
    def display_all():
        """Display tenant information from memory to the console"""
        print_color("RENTAL INCOME RECORD", "third underline")
        print(tabulate(payment_list, headers="firstrow", tablefmt="fancy_grid"))