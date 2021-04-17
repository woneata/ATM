# keep track of user logins
# delete file after logout

import os

user_db_path = "data/user_record/"


def create(number_logins):
    try:
        f = open(user_db_path + str(number_logins) + ".txt", 'x')
    except FileExistsError:
        track_logins = read(user_db_path + str(number_logins) + ".txt")
    if not track_logins:
        delete(number_logins)
