import random


def register():
    registration = True
    while registration:
        print("please enter")
        user3_username = str.upper(input("username: "))
        user3_password = str.upper(input("password: "))
        confirm_password = str.upper(input("Confirm password: "))
        user3_email = str(input("email: "))
        user3_fullname = str(input("Full name: "))
        if confirm_password == user3_password:
            user_record = open("user.txt", "w")
            user_details = f"{user1_username} {user1_password} {user1_email} {user1_fullname} {user2_username} {user2_password} {user2_email} {user2_fullname} {user3_username} {user3_password} {user3_email} {user3_fullname}"
            user_record.write(user_details)
            user_record.close()
            print("Registration successful, now you can proceed to login")
            registration = False
        elif confirm_password != user3_password:
            print("password does not match,please check and try again")


def check_details():
    print("please provide")
    username = str.upper(input("username: "))
    password = str.upper(input("password: "))
    user = open("user.txt", "r")
    info = user.read()
    login_info = info.split()
    if username == login_info[0] and password == login_info[1] or username == login_info[6] and password == login_info[7] or username == login_info[12] and password == login_info[13]:
        print("login successful")
        session = open("session.txt", "w")
        session.write(f"{username} logged in successfully")
        session.close()
        options = True
        while options:
            print(f"hello {username}, what would you like to do? ")
            print(" ")
            print("1. create new account")
            print("2. check account details")
            print("3. logout")
            choice = str(input("press 1,2 or 3 to select preferred option: "))
            if choice == "1":
                print("please enter the following")
                acct_name = str.upper(input("account name: "))
                open_bal = str(input("opening balance: "))
                acct_type = str.upper(input("account type: "))
                acct_email = str.upper(input("account email: "))
                acct_number = random.randint(1000000000, 9999999999)
                details = open("customer.txt", "w")
                acct_details = f"{acct_name} {open_bal} {acct_type} {acct_email} {acct_number}"
                details.write(acct_details)
                details.close()
                print("account created successfully")
                print(f"your account number is {acct_number}")

            elif choice == "2":
                account_number = (input("please enter customer's 10 digit account number: "))
                det = open("customer.txt", "r")
                the_details = det.read()
                get_details = the_details.split()
                if account_number in get_details:
                    print(f"your account details are [Account name, opening balance, account type, email, account number] = [{the_details}]")

                else:
                    print("The account number does not match any account in our records.")
                    print("please check and try again or create new account")

            elif choice == "3":
                close_session = open("session.txt", "w").close()
                options = False

            else:
                print("invalid entry. Please select 1, 2 or 3")

    else:
        print("incorrect username or password. Please check and try again")


print("Welcome to Dragon bank")
user1_username = "DONLARJE"
user1_password = "LIONEL10"
user1_email = "frank@gmail.com"
user1_fullname = "Eze Franklin C"

user2_username = "FAV"
user2_password = "FAV2002"
user2_email = "mysweetness@gmail.com"
user2_fullname = "Arumeze Favour M"


user_record = open("user.txt", "w")
user_details = f"{user1_username} {user1_password} {user1_email} {user1_fullname} {user2_username} {user2_password} {user2_email} {user2_fullname}"
user_record.write(user_details)
user_record.close()

operations = True
while operations:
    operation = str(input("For login, press 1. \n"
                          "New customer? press 2 to register\n"
                          "To close app, press 3\n"
                          ": "))

    if operation == "1":
        try:
            check_details()
        except IndexError:
            print("incorrect username or password. Please check and try again")

    elif operation == "2":
        register()

    elif operation == "3":
        operations = False

    else:
        print("invalid entry. Please select 1 or 2")
