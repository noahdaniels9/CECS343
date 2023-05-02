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
        pass
        '''
        """Read all tenant information from the database into memory"""
        i = 0
        with open(filename, 'r') as fp:
            reader = csv.reader(fp, delimiter=',')
            for row in reader:
                if i == 1:
                    payment_list.append(Payment(row[0], row[1]))
                else:
                    payment_list.append(Payment(row[0], row[1]))
                    i += 1
    '''

    @staticmethod
    def write_to_database(payment_filename):
        """Write all tenant information from memory into the database"""
        with open(payment_filename, 'w', newline='') as fp:
            writer = csv.writer(fp, delimiter=',')
            for room in payment_list:
                writer.writerow([room.number, room.rent])

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

        pay_amount = input("Enter Amount: ")
        if pay_amount == "0":
            return

        payment_list.append(pay_amount)

    def edit_payment(self):
        pass

    def new_text_file(self):
        pass

    @staticmethod
    def sum_all_payments() -> float:
        return 0