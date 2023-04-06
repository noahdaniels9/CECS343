from tenant import *
def login():
    print("Log in required")
    print()
    print("Name: John")
    password = ""
    password = input("Password: ")
    while password != "JohnSnow":
        print("Incorrect Password")
        password = input("Password: ")

def menu(user_input):
    print("Please select what you would like to display:")
    print("1. Tenant List")
    print("2. Rental Income Record")
    print("3. Expense Record")
    print("4. Annual Summary")
    print("5. Log Out")
    user_input = int(input("Enter Input: "))
    return user_input


def main():
    login()
    print("Login Successful!")
    print()
    user_input = 0
    while user_input != 5:
        print("Welcome To Apartment Management System")
        print()
        user_input = menu(user_input)
        if (user_input == 1):
            print("Displaying Tenant List")
            Tenant.display_tenants()
            tOpt = input("Do you want to add or remove from tenant list? Press 1 for add, 2 for remove, and any other key for previous menu.")
            if (tOpt == 1):
                tname = str(input("Enter tenant name that you want to add:"))
                troomnum = int(input("Enter tenant room number that you want to add:"))
                Tenant.add_tenant(tname, troomnum)
            elif (tOpt == 2):
                remname = str(input("Enter the tenant name that you want to remove from the list"))
                Tenant.remove_tenant(remname)
            elif (tOpt != 1 and tOpt != 2):
                menu(0)
        elif(user_input == 2):
            print("Displaying Rental Income record")
        elif (user_input == 3):
            print("Displaying Expense Record")
        elif (user_input == 4):
            print("Displaying Annual Summary")

    print("Successfully Logged out!")

main()
