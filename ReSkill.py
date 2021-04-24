#register
# - first name,last name, password, email
# - generate user account
#

 #login
# - account number and password

#bank operations


#Initializing the system

import random

database = {}  #dictionary

def init():

    isValidOptionSelected = False
    print("Welcome to bankOBA")

    while isValidOptionSelected == False:

        haveAccount = int(input("Do you have an account with us: 1 (yes) 2 (no) \n"))

        if(haveAccount == 1):
            isValidOptionSelected = True
            login()
        elif(haveAccount == 2):
            isValidOptionSelected
            print(register())
        else:
            print("You have selected an invalid option")


def login():

    print("*** Login ***")

    accountNumberOfUser = int(input("What is your account number? \n"))
    password = input("What is your password \n")

    for accountNumber,userDetails in database.items():
        if(accountNumber == accountNumberOfUser):
            if(userDetails[3] == password):
                bankOperation(userDetails)

    print("Invalid account or password")
    login()



def register():

    print("*** Register ***")
    email = input("What is your email address? \n")
    first_name = input("What is your first name? \n")
    last_name = input("What is your last name? \n")
    password = input("create a password for yourself \n")

    accountNumber = generationAccountNumber()

    database[accountNumber] = [first_name, last_name, email, password]

    print("Your Account Has Been Created")
    print("Your account number is: %d" % accountNumber)
    print("Make sure to keep it safe")



    login()


def bankOperation(User):
    print("some operations")

def generationAccountNumber():

    return random.randrange(1111111111, 9999999999)

### ACTUAL BANKKING SYSTEM ####


init()









