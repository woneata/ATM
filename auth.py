# register
# -first name, last name, password, email
# -generate user id

# login
# - account number, email and password

# bank operations

# Initializing the system

import random
import validation
import database
import login
from getpass import getpass


# database = {
#     648957: ['Woneata', 'Stallworth', 'woneata@gmail.com', 'password', 200]
# }


def init():
    print("Welcome to Bank PHP")

    have_account = int(input("Do you have an account with us: 1 (yes) 2 (no)? \n"))

    if have_account == 1:

        login()
    elif have_account == 2:

        print(register())
    else:
        print("You have selected an invalid option")
        init()


def login():
    print('******* Login *******')

    account_number_from_user = input("What is your account number? \n")

    is_valid_account_number = validation.account_number_validation(account_number_from_user)

    if is_valid_account_number:

        # password = input("What is your password? \n")
        password = getpass("What is your password? \n")

        user = database.authenticated_user(account_number_from_user, password);
        if user:
            operations(user)

        print('Invalid account or password')
        login()
    else:
        print("Account number invalid. Please try again")
        init()


def register():
    print('****** Register ******')

    email = input("What is your email address? \n")
    first_name = input("What is your first name? \n")
    last_name = input("What is your last name? \n")
    password = getpass('Create your password? \n')

    account_number = generate_account_number()
    is_user_created = database.create(account_number, first_name, last_name, email, password)

    if is_user_created:

        # using database module to create new user record
        print("Your account has been created")
        print(" == ==== ===== ===== ===")
        print('Your account number is: %d' % account_number)
        print('Make sure you keep it safe')
        print(" == ==== ===== ===== ===")

        login()
    else:
        print("Something went wrong, please try again")
        register()


def operations(user):
    print('Welcome %s %s' % (user[0], user[1]))

    selected_option = int(input("What would you like to do? (1) deposit (2) withdrawal (3) Logout (4) Exit \n"))

    if selected_option == 1:

        deposit()
    elif selected_option == 2:

        withdrawal()
    elif selected_option == 3:
        logout()

    elif selected_option == 4:

        exit()
    else:
        print("Invalid option selected")
        operations(user)


def withdrawal(user_details):
    get_account_balance = str.split(user_details, ','[4])
    print('Your current balance is ', get_account_balance)
    amount = float(input("How much would you like to withdraw?"))
    if get_account_balance >= amount:
        get_account_balance -= amount
        print("\n You withdrew:", amount)
        print('\n Your current balance is', get_account_balance)
    else:
        print('\n insufficient balance ')
    print('Withdrawal')
    # get current balance
    # get amount to withdraw
    # check if current balance > withdraw balance
    # deduct withdrawn amount from current balance
    # display current balance


def deposit(user_details):
    balance = user_details[4]
    user_details = (database.read(balance))
    get_account_balance = str.split(user_details, ','[4])
    amount = float(input("\n How much would you like to deposit?"))
    current_user_balance = get_account_balance + amount
    print('\n amount deposited:', amount)
    print('\n Your current balance is:', current_user_balance)

    user_details[4] = current_user_balance

    # get current balance
    # get amount to deposit
    # add deposited amount to current balance
    # display current balance


def generate_account_number():
    return random.randrange(111111, 999999)


def set_current_balance(user_details, balance):
    user_details[4] = balance


def get_current_balance(user_details):
    return user_details[4]


def logout():
    login()


init()
