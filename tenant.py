import csv
tenant_dict = {}


class Tenant:
    name: str = ""
    room: int = 0

    def __init__(self, name, room):
        self.name = name
        self.room = room

    def display(self):
        """Display this tenant's information"""
        print(f"Name : {self.name}\n"
              f"Room number: {self.room}")

    @staticmethod
    def read_from_database(tenant_filename):
        with open(tenant_filename, 'r') as fp:
            reader = csv.reader(fp, delimiter=',')
            for row in reader:
                tenant_dict[row[0]] = int(row[1])

    @staticmethod
    def write_to_database(tenant_filename):
        with open(tenant_filename, 'w') as fp:
            writer = csv.writer(fp, delimiter=',')
            for k, v in tenant_dict.items():
                writer.writerow([k, v])

    @staticmethod
    def tenant_menu() -> int:
        choice = input("TENANT MANAGEMENT\n"
                       "1. Display all tenants\n"
                       "2. Add a new tenant\n"
                       "3. Remove a tenant\n"
                       "4. Return to main menu\n\n"
                       "Your choice: ")

        # Check if choice is a number
        try:
            choice = int(choice)
        except ValueError:
            print("Please enter a number.")

        # Check if choice is in range
        if choice in range(5):
            return choice
        else:
            print("Invalid choice.\n")

    @staticmethod
    def display_all():
        print("TENANT LIST")
        for k, v in tenant_dict.items():
            print(f"{k}: {v}")

    @staticmethod
    def add_tenant():
        Tenant.display_all()
        tenant_name = input("Name: ")
        room_number = input("Room number: ")

        tenant_dict[tenant_name] = room_number

    @staticmethod
    def remove_tenant():
        Tenant.display_all()
        tenant_name = input("Name: ")





