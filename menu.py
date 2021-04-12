'''
Provides a basic frontend
'''

# pylint: disable=C0103
# Disable only for names "user_collection" and "status_collection"

from datetime import datetime
import logging
import sys
from playhouse.dataset import DataSet
import main

LOG_FORMAT = "%(asctime)s %(filename)s:%(lineno)-3d %(levelname)s %(message)s"
FILENAME_CUSTOM = datetime.now().strftime('log_%m_%d_%Y.log')
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT,
                    filename=FILENAME_CUSTOM)
logging.info("menu.py testing is started.")


def load_users():
    '''
    Loads user accounts from a file
    '''
    # filename = '1.csv'
    filename = input('Enter filename of user file: ')
    main.load_users(filename, user_collection)
    # for user in user_collection._users_db:
    #     print(user)


def load_status_updates():
    '''
    Loads status updates from a file
    '''
    # filename = '2.csv'
    filename = input('Enter filename for status file: ')
    main.load_status_updates(filename, status_collection, user_collection)
    # for status in status_collection._status_db:
    #     print(status)


def add_user():
    '''
    Adds a new user into the database
    '''
    user_id = input('User ID: ')
    email = input('User email: ')
    user_name = input('User name: ')
    user_last_name = input('User last name: ')
    if not main.add_user(user_id, email, user_name, user_last_name,
                         user_collection):
        print("An error occurred while trying to add new user. User_id is "
              "already exist")
    else:
        print("User was successfully added")


def update_user():
    '''
    Updates information for an existing user
    '''
    user_id = input('User ID: ')
    email = input('User email: ')
    user_name = input('User name: ')
    user_last_name = input('User last name: ')
    if not main.update_user(user_id, email, user_name, user_last_name,
                            user_collection):
        print("An error occurred while trying to update user. There is no such"
              "User Id at database")
    else:
        print("User was successfully updated")


def search_user():
    '''
    Searches a user in the database
    '''
    user_id = input('Enter user ID to search: ')
    result = main.search_user(user_id, user_collection)
    if result is None:
        print("ERROR: User does not exist")
    else:
        print(f"User ID: {result['USER_ID']}")
        print(f"Email: {result['EMAIL']}")
        print(f"Name: {result['NAME']}")
        print(f"Last name: {result['LASTNAME']}")


def delete_user():
    '''
    Deletes user from the database
    '''
    user_id = input('User ID: ')
    if not main.delete_user(user_id, user_collection):
        print("An error occurred while trying to delete user. There is no such"
              "User Id at database")
    else:
        print("User was successfully deleted")


def add_status():
    '''
    Adds a new status into the database
    '''
    status_id = input('Status ID: ')
    user_id = input('User ID: ')
    status_text = input('Status text: ')

    if not main.add_status(status_id, user_id, status_text, status_collection):
        print("An error occurred while trying to add new status")
    else:
        print("New status was successfully added")


def update_status():
    '''
    Updates information for an existing status
    '''
    status_id = input('Status ID: ')
    user_id = input('User ID: ')
    status_text = input('Status text: ')
    if not main.update_status(status_id, user_id, status_text,
                              status_collection):
        print("An error occurred while trying to update status")
    else:
        print("Status was successfully updated")


def search_status():
    '''
    Searches a status in the database
    '''
    status_id = input('Enter status ID to search: ')
    result = main.search_status(status_id, status_collection)
    if result is None:
        print("ERROR: Status does not exist")
    else:
        print(f"User ID: {result['USER_ID']}")
        print(f"Status ID: {result['STATUS_ID']}")
        print(f"Status text: {result['STATUS_TEXT']}")


def delete_status():
    '''
    Deletes status from the database
    '''
    status_id = input('Status ID: ')
    if not main.delete_status(status_id, status_collection):
        print("An error occurred while trying to delete status")
    else:
        print("Status was successfully deleted")


def quit_program():
    '''
    Quits program
    '''
    DB.close()
    sys.exit()


if __name__ == '__main__':
    DB = DataSet('sqlite:///:memory:')
    USERS_TABLE = DB['UsersTable']
    STATUS_TABLE = DB['StatusTable']

    user_collection = main.init_user_collection(USERS_TABLE)
    status_collection = main.init_status_collection(STATUS_TABLE,
                                                    user_collection)

    MENU_OPTIONS = {
        'A': load_users,
        'B': load_status_updates,
        'C': add_user,
        'D': update_user,
        'E': search_user,
        'F': delete_user,
        'H': add_status,
        'I': update_status,
        'J': search_status,
        'K': delete_status,
        'Q': quit_program
    }
    while True:
        USER_SELECTION = input("""
                            A: Load user database
                            B: Load status database
                            C: Add user
                            D: Update user
                            E: Search user
                            F: Delete user
                            H: Add status
                            I: Update status
                            J: Search status
                            K: Delete status
                            Q: Quit

                            Please enter your choice: """)
        if USER_SELECTION.upper() in MENU_OPTIONS:
            MENU_OPTIONS[USER_SELECTION.upper()]()
        else:
            print("Invalid option")
