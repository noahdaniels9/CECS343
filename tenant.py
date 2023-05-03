import csv
from tabulate import tabulate
from helper import print_color, validate_input

# List of tenant objects read from file
tenant_list = []


class Tenant:
    name: str
    room: int

    def __init__(self, name, room):
        self.name = name
        self.room = room

    def __iter__(self):
        for attribute in [self.name, self.room]:
            yield attribute

    def display(self):
        """Display this tenant's information"""
        print(f"Name : {self.name}\n"
              f"Room number: {self.room}")

    @staticmethod
    def read_from_database(filename):
        """Read all tenant information from the database into memory"""
        del tenant_list[:]
        with open(filename, 'r') as fp:
            reader = csv.reader(fp, delimiter=',')
            for row in reader:
                tenant_list.append(Tenant(row[0], row[1]))

    @staticmethod
    def write_to_database(filename):
        """Write all tenant information from memory into the database"""
        with open(filename, 'w', newline='') as fp:
            writer = csv.writer(fp, delimiter=',')
            for tenant in tenant_list:
                writer.writerow([tenant.name, tenant.room])

    @staticmethod
    def tenant_menu() -> int:
        """Display all available menu options for managing tenants"""
        print_color("TENANT MANAGEMENT", "second")
        print_color("MENU", "third")

        choice = input("1. Add a new tenant\n"
                       "2. Remove a tenant\n"
                       "3. Return to main menu\n\n"
                       "Your choice: ")

        # Check if choice is a good input
        if validate_input(choice, 4):
            return int(choice)

    @staticmethod
    def display_all():
        """Display tenant information from memory to the console"""
        print_color("TENANT LIST", "third underline")
        print(tabulate(tenant_list, headers="firstrow", tablefmt="fancy_grid"))

    @staticmethod
    def add_tenant(room_list):
        """Add a tenant to tenant dictionary in memory
        It will overwrite room number if the name already exist, so it also acts as an update function"""
        print_color("ADDING A NEW TENANT", "third")
        print_color("Enter 0 to quit", "info")

        tenant_name = input("Tenant Name: ")
        if tenant_name == "0":
            return

        try:
            room_number = int(input("Room Number: "))
        except ValueError:
            print_color("Please enter a number", "error")
            return
        else:
            for room in room_list:
                if room.number == str(room_number):
                    tenant_list.append(Tenant(tenant_name, room_number))
                    print_color("Tenant added", "success")
                    return

            print_color("Room not exist", "error")


    @staticmethod
    def remove_tenant():
        """Remove a tenant from the tenant dictionary in memory."""
        print_color("REMOVING A TENANT", "third")
        print_color("Enter 0 to quit", "info")

        name_to_delete = input("Name: ")
        if name_to_delete == "0":
            return

        for tenant in tenant_list:
            if tenant.name == name_to_delete:
                tenant_list.remove(tenant)
                print_color("Tenant removed\n", "success")
                return

        print_color("Name not found\n", "error")
