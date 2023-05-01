import csv
from tabulate import tabulate
from helper import print_color, validate_input

# List of room objects read from file
room_list = []

class Room:
    number: int = 0
    rent: float = 0

    def __init__(self, number, rent):
        self.number = number
        self.rent = rent

    def __iter__(self):
        for attribute in [self.number, self.rent]:
            yield attribute

    def display(self):
        """Display this room's information"""
        print(f'Room number: {self.number}\n'
              f'Rent: ${self.rent}')

    @staticmethod
    def read_from_database(room_filename):
        """Read all tenant information from the database into memory"""
        with open(room_filename, 'r') as fp:
            reader = csv.reader(fp, delimiter=',')
            for row in reader:
                room_list.append(Room(row[0], row[1]))
    @staticmethod
    def write_to_database(room_filename):
        """Write all tenant information from memory into the database"""
        with open(room_filename, 'w') as fp:
            writer = csv.writer(fp, delimiter=',')
            for room in room_list:
                writer.writerow([room.number, room.rent])

    @staticmethod
    def room_menu() -> int:
        """Display all available menu options for managing rooms and rent"""
        print_color("ROOM MANAGEMENT", "second")
        print_color("MENU", "third")

        choice = input("1. Add a new room\n"
                       "2. Remove a room\n"
                       "3. Adjust rent for a room\n"
                       "4. Return to main menu\n\n"
                       "Your choice: ")

        # Check if choice is a good input
        if validate_input(choice, 5):
            return int(choice)

    @staticmethod
    def display_all():
        """Display room information from memory to the console"""
        pass

    def adjust_rent(self):
        try:
            for i in room_list:
                print(i, room_list[i])
            roomNum = input("For what room do you want to change the rent amount?:")
            newRent = input("Enter the rent amount that you want to adjust to: $")
            room_list[roomNum] = newRent
        except:
            print("An unexpected error has occured. Try again.")

    @staticmethod
    def add_room():
        """Add a new room dictionary in memory"""
        print_color("ADDING A NEW ROOM", "third")
        print_color("Enter 0 to quit", "info")

        room_num = input("Room Number: ")
        rent_amount = input("Rent Amount: ")
        if room_num == "0":
            return

        room_list.append(Room(room_num, rent_amount))

    @staticmethod
    def remove_room():
        """Remove a room from the tenant dictionary in memory."""
        print_color("REMOVING A ROOM", "third")
        print_color("Enter 0 to quit", "info")

        name_to_delete = input("Room Number: ")
        if name_to_delete == "0":
            return

        for i in room_list:
            if i.name == name_to_delete:
                room_list.remove(i)
                print_color("Room removed\n", "success")
                return

        print_color("Room Number not found\n", "error")
