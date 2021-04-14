def account_number_validation(account_number):
    # check if account_number is not empty
    # if account_number is 6 digits
    # if the account_number is an integer
    if account_number:

        try:
            int(account_number)
            if len(str(account_number)) == 6:

                return True

        except ValueError:
            return False
        except TypeError:
            return False

    return False
