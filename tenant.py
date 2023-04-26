import csv
tenant_dict = {}


class Tenant:
    name: str
    room: int

    def __init__(self, name, room):
        self.name = name
        self.room = room

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
                tenant_dict[row[0]] = int(row[1])

    @staticmethod
    def write_to_database(tenant_filename):
        """Write all tenant information from memory into the database"""
        with open(tenant_filename, 'w') as fp:
            writer = csv.writer(fp, delimiter=',')
            for k, v in tenant_dict.items():
                writer.writerow([k, v])

    @staticmethod
    def tenant_menu() -> int:
        """Display all available menu options for managing tenants"""
        choice = input("\nTENANT MANAGEMENT\n"
                       "1. Add a new tenant\n"
                       "2. Remove a tenant\n"
                       "3. Return to main menu\n\n"
                       "Your choice: ")

        # Check if choice is a number
        try:
            choice = int(choice)
        except ValueError:
            print("Please enter a number.")

        # Check if choice is in range
        if choice in range(4):
            return choice
        else:
            print("Invalid choice.\n")

    @staticmethod
    def display_all():
        """Display tenant information from memory to the console"""
        print("TENANT LIST")
        for k, v in tenant_dict.items():
            print(f"{k}: {v}")

    @staticmethod
    def add_tenant():
        """Add a tenant to tenant dictionary in memory
        It will overwrite room number if the name already exist, so it also acts as an update function"""
        print("ADDING A NEW TENANT")
        tenant_name = input("Name: ")
        room_number = input("Room number: ")

        tenant_dict[tenant_name] = room_number

    @staticmethod
    def remove_tenant():
        """Remove a tenant from the tenant dictionary in memory."""
        Tenant.display_all()
        print("\nREMOVING A TENANT")
        tenant_name = input("Name: ")

        try:
            tenant_dict.pop(tenant_name)
        except KeyError:
            print("Tenant not found! Try entering a full name.")





