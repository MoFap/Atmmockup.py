# register
# - first name,last name, password, email
# - generate user account
#

# login
# - account number and password

# bank operations


# Initializing the system

import random
import database


database = {
    1664902096: ["morenike", "fapojuwo", "baffie@yahoo.com", "baffie1990", 500]
}

def init():
    isValidOptionSelected = False
    print("Welcome to bankOBA")

    while isValidOptionSelected == False:

        have_account = int(input("Do you have an account with us: 1 (yes) 2 (no) \n"))

        if have_account == 1:
            isValidOptionSelected = True
            login()
        elif have_account == 2:
            isValidOptionSelected
            print(register())
        else:
            print("You have selected an invalid option")


def login():
    print("*** Login ***")

    account_number_of_user = (input("What is your account number? \n"))

    is_valid_account_number = account_number_validation(account_number_of_user)

    if is_valid_account_number:

        password = input("What is your password \n")

    for account_number, user_details in database.items():
        if account_number == int(account_number_of_user):
            if user_details[3] == password:
                bank_operation(user_details)

    print("Invalid account or password")
    login()


def account_number_validation(account_number):

    if account_number:

        if len(str(account_number)) == 10:

            try:
                int(account_number)
                return True
            except ValueError:
                print("Invalid account number, account number should be an integer")
                return False

        else:
            print("Account number cannot be more than 10 digits")

    else:
        print("Account number is a required field")
        return False


def register():
    print("*** Register ***")

    email = input("What is your email address? \n")
    first_name = input("What is your first name? \n")
    last_name = input("What is your last name? \n")
    password = input("create a password for yourself \n")

    account_number = generation_account_number()

    is_user_created = database.create(account_number, [first_name, last_name, email, password, 0])

    if is_user_created:
        print("Your Account Has Been Created")
        print("Your account number is: %d" % account_number)
        print("Make sure to keep it safe")

        login()

    else:
        print("Something went wrong, please try again")
        register()



def bank_operation(user):
    print("Welcome %s %s " % (user[0], user[1]))

    selected_option = int(input("What would you like to do? (1) deposit (2) withdrawal (3) logout (4) exit \n"))

    if selected_option == 1:
        deposit_operation()

    elif selected_option == 2:
        withdrawal_operation()

    elif selected_option == 3:
        logout_operation()

    elif selected_option == 4:
        exit()
    else:

        print("Invalid option selected")

        bank_operation(user)

def deposit_operation():
    print("deposit")

def withdrawal_operation():
    print("withdrawal")


def generation_account_number():
    return random.randrange(1111111111, 9999999999)

def get_current_balance(user_details):
    return user_details[4]

def logout_operation():
     login()


init()
