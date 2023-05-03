import os
import csv
from tabulate import tabulate
from helper import print_color, validate_input

# List of payment years read from file
payment_list = []
headers = ["room number", "january", "february", "march", "april", "may", "june",
           "july", "august", "september", "october", "november", "december"]


class Payment:

    def __init__(self, year, payments):
        self.year = year
        self.payments = payments

    def __iter__(self):
        for item in self.payments:
            yield item

    @staticmethod
    def read_from_database(directory):
        """Read all tenant information from the database into memory"""
        del payment_list[:]
        for filename in os.listdir(directory):
            full_filename = directory + filename

            with open(full_filename, 'r') as fp:
                reader = csv.reader(fp, delimiter=',')
                payment_year = Payment(year=os.path.splitext(filename)[0], payments=[])
                for row in reader:
                    payment_year.payments.append(row)

                payment_list.append(payment_year)

    @staticmethod
    def write_to_database(directory):
        """Write all tenant information from memory into the database"""
        for payment_year in payment_list:
            full_filename = directory + payment_year.year + ".txt"
            with open(full_filename, 'w') as fp:
                writer = csv.writer(fp, delimiter=',')
                for row in payment_year.payments:
                    writer.writerow(row)

    @staticmethod
    def payment_menu() -> int:
        """Display all available menu options for managing tenants"""
        print_color("INCOME RECORD MANAGEMENT", "second")
        print_color("MENU", "third")

        choice = input("1. Add a new room payment setup\n"
                       "2. Edit a payment\n"
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
        for payment_year in payment_list:
            print(payment_year.year)
            print(tabulate(payment_year.payments, headers=[headers[i].capitalize() for i in range(len(headers))], tablefmt="fancy_grid"))

    @staticmethod
    def add_payment(room_list):  # may need fix
        """Add a new payment """
        print_color("ADDING A NEW PAYMENT", "third")

        print_color("YEARS", "third")
        print_color("Return to previous menu to add another calendar year", "info")
        for payment_year in payment_list:
            print(payment_year.year)
        year = input("\nYour choice: ")

        # Check for correct year
        for payment_year in payment_list:
            if payment_year.year == year:

                # Input and check for correct room
                try:
                    room_number = int(input("\nROOM NUMBER: "))
                except ValueError:
                    print_color("Please enter a number", "error")
                    return
                else:
                    for room in room_list:
                        if room.number == str(room_number):
                            new_payment = room.rent
                            print(f"Payment for this room: ${new_payment}")

                            # Input and check month
                            print_color("MONTH (January to December)", "third")
                            month = input("Your choice: ")

                            if month.lower() in headers:
                                for item in payment_year.payments:
                                    if item[0] == str(room_number):
                                        item[headers.index(month.lower())] = new_payment
                                        return
                            else:
                                print_color("Invalid month", "error")
                                return

        print_color("Year not available. Try option 3 (add more years)", "error")

    @staticmethod
    def edit_payment():
        print_color("CHANGING PAYMENT", "third")
        print_color("Enter 0 to quit", "info")

        room_number = input("Room number: ")
        if room_number == "0":
            return
        room_row = int(room_number) % 100
        print("\n1-January"
              "\n2-February"
              "\n3-March"
              "\n4-April"
              "\n5-May"
              "\n6-June"
              "\n7-July"
              "\n8-August"
              "\n9-September"
              "\n10-October"
              "\n11-November"
              "\n12-December")
        month = (int(input("Which month?: "))) - 1
        payment = input("Payment: ")
        'room that will have its payment edited'
        edit_room = payment_list[room_row]
        'room payment for that month is changed to new payment'
        months_names = ['jan', 'feb', 'march', 'april', 'may', 'june', 'july', 'aug', 'sept', 'octo', 'nov', 'dec']
        month_name = months_names[month]
        setattr(edit_room, month_name, payment)
        'add updated room payment back to list'
        payment_list[room_row] = edit_room

    @staticmethod
    def new_text_file(directory, room_list):
        print_color("ADDING A NEW YEAR", "third")

        try:
            new_year = int(input("New year: "))
        except ValueError:
            print_color("Invalid input", "error")
        else:
            for payment_year in payment_list:
                if payment_year.year == str(new_year):
                    print_color("Year already exist", "error")
                    return

            full_filepath = directory + str(new_year) + ".txt"
            with open(full_filepath, 'w') as fp:
                writer = csv.writer(fp, delimiter=',')
                for room in room_list[1:]:
                    row = ["-"] * 12
                    row.insert(0, room.number)
                    writer.writerow(row)

    @staticmethod
    def sum_all_payments():
        all_payments = []

        for payment_year in payment_list:
            annual_payments = 0
            for room in payment_year.payments:
                for payment in room[1:]:
                    if payment != "-":
                        annual_payments += float(payment)
            all_payments.append([payment_year.year, annual_payments])

        return all_payments
