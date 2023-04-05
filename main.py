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
        elif(user_input == 2):
            print("Displaying Rental Income record")
        elif (user_input == 3):
            print("Displaying Expense Record")
        elif (user_input == 4):
            print("Displaying Annual Summary")

    print("Successfully Logged out!")

main()
