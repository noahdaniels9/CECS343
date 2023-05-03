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
        del room_list[:]
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
        print_color("ROOM LIST", "third underline")
        print(tabulate(room_list, headers="firstrow", tablefmt="fancy_grid"))

    @staticmethod
    def adjust_rent():
        print_color("ADJUSTING RENT", "third")
        print_color("Enter 0 to quit", "info")

        while True:
            room_number = input("Room Number: ")
            if room_number == "0":
                return
            for room in room_list:
                if room.number == room_number:
                    print(f"Old rent: ${room.rent}")
                    new_rent = input("New rent: $")
                    if float(new_rent) < 0:
                        print_color("Invalid rent", "error")
                        return
                    else:
                        room.rent = new_rent
                        print_color("Rent adjusted", "success")
                        return
            print_color("Room number not found", "error")

    @staticmethod
    def add_room():
        """Add a new room dictionary in memory"""
        print_color("ADDING A NEW ROOM", "third")
        print_color("Enter 0 to quit", "info")

        try:
            new_room_number = int(input("Room Number: "))
        except ValueError:
            print_color("Please enter a number", "error")
            return
        else:
            for room in room_list:
                if room.number == str(new_room_number):
                    print_color("Room already exist", "error")
                    return

        if new_room_number == "0":
            return
        rent_amount = input("Rent Amount: ")

        room_list.append(Room(new_room_number, rent_amount))

    @staticmethod
    def remove_room(tenant_list):
        """Remove a room from the room list in memory."""
        print_color("REMOVING A ROOM", "third")
        print_color("Enter 0 to quit", "info")

        room_to_delete = input("Room Number: ")
        if room_to_delete == "0":
            return

        for room in room_list:
            if room.number == room_to_delete:
                for tenant in tenant_list:
                    if tenant.room == room_to_delete:
                        print_color(f"Evicting tenant {tenant.name}", "success")
                        tenant_list.remove(tenant)
                room_list.remove(room)
                print_color("Room removed\n", "success")
                return

        print_color("Room Number not found\n", "error")
