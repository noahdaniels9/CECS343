import csv
from termcolor import colored
from tabulate import tabulate
from display import *

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
    def read_from_database(tenant_filename):
        """Read all tenant information from the database into memory"""
        with open(tenant_filename, 'r') as fp:
            reader = csv.reader(fp, delimiter=',')
            for row in reader:
                tenant_list.append(Tenant(row[0], row[1]))

    @staticmethod
    def write_to_database(tenant_filename):
        """Write all tenant information from memory into the database"""
        with open(tenant_filename, 'w') as fp:
            writer = csv.writer(fp, delimiter=',')
            for tenant in tenant_list:
                writer.writerow([tenant.name, tenant.room])

    @staticmethod
    def tenant_menu() -> int:
        """Display all available menu options for managing tenants"""
        print(colored("TENANT MANAGEMENT".center(Width.full), Color.primary, attrs=["bold", "underline"]))
        print(colored("MENU\n".center(Width.full), Color.secondary))

        choice = input("1. Add a new tenant\n"
                       "2. Remove a tenant\n"
                       "3. Return to main menu\n\n"
                       "Your choice: ")

        # Check if choice is a number
        try:
            choice = int(choice)
        except ValueError:
            print(colored("Please enter a number".center(Width.full), Color.error))
        else:
            # Check if choice is in range
            if choice in range(4):
                return choice
            else:
                print(colored("Invalid choice".center(Width.full), Color.error))

    @staticmethod
    def display_all():
        """Display tenant information from memory to the console"""
        print(colored("TENANT LIST".center(Width.full), attrs=["underline"]))
        print(tabulate(tenant_list, headers="firstrow", tablefmt="rounded_grid"))

    @staticmethod
    def add_tenant():
        """Add a tenant to tenant dictionary in memory
        It will overwrite room number if the name already exist, so it also acts as an update function"""
        print("ADDING A NEW TENANT")
        tenant_name = input("Name: ")
        room_number = input("Room number: ")

        tenant_list.append(Tenant(tenant_name, room_number))

    @staticmethod
    def remove_tenant():
        """Remove a tenant from the tenant dictionary in memory."""
        print("\nREMOVING A TENANT")
        name_to_delete = input("Name: ")

        for tenant in tenant_list:
            if tenant.name == name_to_delete:
                tenant_list.remove(tenant)
