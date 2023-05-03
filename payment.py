import csv
from tabulate import tabulate
from helper import print_color, validate_input

# List of room objects read from file
payment_list = []


class Payment:
    room: int
    jan: int
    feb: int
    march: int
    april: int
    may: int
    june: int
    july: int
    aug: int
    sept: int
    octo: int
    nov: int
    dec: int

    def __init__(self, room, jan, feb, march, april, may,
                 june, july, aug, sept, octo, nov, dec):
        self.room = room
        self.jan = jan
        self.feb = feb
        self.march = march
        self.april = april
        self.may = may
        self.june = june
        self.july = july
        self.aug = aug
        self.sept = sept
        self.octo = octo
        self.nov = nov
        self.dec = dec

    def __iter__(self):
        for attribute in [self.room, self.jan, self.feb, self.march,
                          self.april, self.may, self.june, self.july,
                          self.aug, self.sept, self.octo, self.nov, self.dec]:
            yield attribute

    def display(self):
        """Display this tenant's payment"""
        print(f"Room : {self.room}")
        months = ["jan", "feb", "march", "april", "may", "june",
                  "july", "aug", "sep", "octo", "nov", "dec"]
        pass


    @staticmethod
    def read_from_database(filename):
        """Read all tenant information from the database into memory"""
        del payment_list[:]
        with open(filename, 'r') as fp:
            reader = csv.reader(fp, delimiter=',')
            for row in reader:
                payment_list.append(Payment(row[0], row[1], row[2], row[3], row[4], row[5], row[6],
                                            row[7], row[8], row[9], row[10], row[11], row[12]))

    @staticmethod
    def write_to_database(payment_filename):
        """Write all tenant information from memory into the database"""
        with open(payment_filename, 'w', newline='') as fp:
            writer = csv.writer(fp, delimiter=',')
            for rooms in payment_list:
                writer.writerow([rooms.room, rooms.jan, rooms.feb, rooms.march, rooms.april,
                                 rooms.may, rooms.june, rooms.july, rooms.aug, rooms.sept,
                                 rooms.octo, rooms.nov, rooms.dec])

    @staticmethod
    def payment_menu() -> int:
        """Display all available menu options for managing tenants"""
        print_color("INCOME RECORD MANAGEMENT", "second")
        print_color("MENU", "third")

        choice = input("1. Add a new payment\n"
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
        print(tabulate(payment_list, headers="firstrow", tablefmt="fancy_grid"))

    @staticmethod
    def add_payment():      # may need fix
        """Add a new room dictionary in memory"""
        print_color("ADDING A NEW PAYMENT", "third")
        print_color("Enter 0 to quit", "info")

        room_number = input("Room number: ")
        if room_number == "0":
            return
        jan_pay = input("January Payment:")
        feb_pay = input("February Payment:")
        march_pay = input("March Payment:")
        april_pay = input("April Payment:")
        may_pay = input("May Payment:")
        june_pay = input("June Payment:")
        july_pay = input("July Payment:")
        aug_pay = input("August Payment:")
        sept_pay = input("September Payment:")
        octo_pay = input("October Payment:")
        nov_pay = input("November Payment:")
        dec_pay = input("December Payment")

        payment_list.append(Payment(room_number, jan_pay, feb_pay, march_pay, april_pay,
                                    may_pay, june_pay, july_pay, aug_pay, sept_pay,
                                    octo_pay, nov_pay, dec_pay))

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

    def new_text_file(self):
        pass

    @staticmethod
    def sum_all_payments() -> float:
        return 0