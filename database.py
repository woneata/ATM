# create record
# update record
# read record
# delete
# CRUD

# find user
import os
import validation

user_db_path = 'data/user_record/'
auth_session_path = 'data/auth_session/'


def create(user_account_number, first_name, last_name, email, password):
    user_data = first_name + "," + last_name + "," + email + "," + password + "," + str(0)
    if does_account_number_exist(user_account_number):
        return False

    if does_email_exist(email):
        print('User already exists')
        return False

    completion_state = False

    try:

        f = open(user_db_path + str(user_account_number) + ".txt", "x")

    except FileExistsError:

        does_file_contain_data = read(user_db_path + str(user_account_number) + ".txt")
        if not does_file_contain_data:
            delete(user_account_number)


    # delete the already created file, and print out error, then return false
    # check content of file before deleting
    # delete(account_number)

    else:
        f.write(str(user_data))
        completion_state = True

    finally:

        f.close()
        return completion_state

    # create a file - account_number.txt
    # add the user details to the file
    # return true
    # if saving to file file fails, then delete created file


def read(user_account_number):
    # find user with account number
    # fetch content of the file
    is_valid_account_number = validation.account_number_validation(user_account_number)

    try:

        if is_valid_account_number:
            f = open(user_db_path + str(user_account_number) + ".txt", "r")
        else:
            f = open(user_db_path + user_account_number, "r")

    except FileNotFoundError:
        print("User not Found")

    except FileExistsError:
        print("User doesn't exist")

    except TypeError:
        print("Invalid account number format")

    else:
        return f.readline()
    return False


def update(user_account_number, user_details):

    user = user_details[0] + "," + user_details[1] + "," + user_details[3] + "," + user_details[4]
    try: 
        f = open(user_db_path + str(user_account_number) + ".txt", "w")
        f.write(user)
        return True
    except:
        return False 
    
    # find user with account number
    # fetch the contents of the file
    # update the contents of the file
    # save the file
    # return true


def delete(user_account_number):
    print('delete user record')
    is_delete_successful = False
    if os.path.exists(user_db_path + str(user_account_number) + ".txt"):
        try:
            os.remove(user_db_path + str(user_account_number) + ".txt")
            is_delete_successful = True
        except FileNotFoundError:
            print("user not found")
        finally:
            return is_delete_successful

    # find user with account number
    # delete the user record (file)
    # return true


def does_email_exist(email):
    all_users = os.listdir(user_db_path)

    for user in all_users:
        user_list = str.split(read(user), ',')
        if email in user_list:
            return True
    return False


def does_account_number_exist(account_number):
    all_users = os.listdir(user_db_path)
    for user in all_users:
        if user == str(account_number) + ".txt":
            return True
    return False


def authenticated_user(account_number, password):
    if does_account_number_exist(account_number):

        user = str.split(read(account_number), ',')
        if password == user[3]:
            return user
    return False


def login_auth_sesson(account_number, user_details):
    data = user_details[0] + " " + user_details[1] + "logged in."

    try: 
        f = open(auth_session_path + str(account_number) + ".txt", "x")

    except FileExistsError:
        f = open(auth_session_path + str(account_number) + ".txt", "w")

    else: 
        f.write(data)

    finally:
        f.close()

    return True

def get_account_balance(user_details, balance):
    user_details[4] = balance


def logins(account_number):
    is_delete_successful = False
    if os.path.exists(auth_session_path + str(account_number) + ".txt"):
        try:
            os.remove(auth_session_path + str(account_number) + ".txt")
            is_delete_successful = True
        except FileNotFoundError:
            print("user not found")
        finally:
            return is_delete_successful

# print(does_email_exist('woneata@gmail.com'))
# print(read(371976))
# print(read({'one' : 'two'}))
