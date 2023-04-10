from tenant import *


def login():
    print("Apartment Management System")
    print()
    print("Log in required")
    print()
    print("Name: John")
    password = ""
    password = input("Password: ")
    while password != "JohnSnow":
        print("Incorrect Password")
        password = input("Password: ")

def menu(user_input):
    try:
        print("Please select what you would like to display:")
        print("1. Tenant List")
        print("2. Rental Income Record")
        print("3. Expense Record")
        print("4. Annual Summary")
        print("5. Log Out")
        user_input = int(input("Enter Input: "))
        return user_input
    except:
        print("Error: invalid input.")


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
            tOpt = '1'
            try:
                while(tOpt == '1' or tOpt == '2'):
                    print()
                    print("1. add new tenant")
                    print("2. remove existing tenants")
                    print("3. return to main menu")

                    tOpt = input()
                    if (tOpt == '1'):
                        tname = str(input("Enter tenant name that you want to add:"))
                        troomnum = int(input("Enter tenant room number that you want to add:"))
                        Tenant.add_tenant(tname, troomnum)
                    elif (tOpt == '2'):
                        remname = str(input("Enter the tenant name that you want to remove from the list"))
                        Tenant.remove_tenant(remname)
                    elif (tOpt != '1' and tOpt != '2'):
                        break
            except:
                print("Error: invalid input.")
                
        elif(user_input == 2):
            print("Displaying Rental Income record")
            #add display function for rent income record(apartment number, respective rent)
            print()
            print("1. add new payment")
            print("2. add new rooms")
            print("3. remove existing room")
            print("4. return to main menu")

        elif (user_input == 3):
            print("Displaying Expense Record")
            #add display function for expense record(date, payee, amount, category)
            print()
            print("1. add new expense")
            print("2. return to main menu")

        elif (user_input == 4):
            print("Displaying Annual Summary")
            #add display function for annual summary(year, total income, total expense, profit/loss)
            print("total profit/loss: ")
            print()
            #add option to choose from
            print("1. return to main menu")

    print("Successfully Logged out!")

main()