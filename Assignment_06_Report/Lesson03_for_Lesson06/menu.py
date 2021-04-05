'''
Provides a basic frontend
'''

# pylint: disable=C0103
# Disable only for names "user_collection" and "status_collection"

from timeit import timeit as timer
from datetime import datetime
import logging
import sys
import main
from socialnetwork_model import DB, UsersTable, StatusTable

LOG_FORMAT = "%(asctime)s %(filename)s:%(lineno)-3d %(levelname)s %(message)s"
FILENAME_CUSTOM = datetime.now().strftime('log_%m_%d_%Y.log')
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT,
                    filename=FILENAME_CUSTOM)
logging.info("menu.py testing is started.")

repetitions = 1000

def load_users():
    '''
    Loads user accounts from a file
    '''
    filename = input('Enter filename of user file: ')
    main.load_users(filename, user_collection)
    print("time for load users")
    print(timer('load_users', globals=globals(), number=repetitions))

def load_status_updates():
    '''
    Loads status updates from a file
    '''
    filename = input('Enter filename for status file: ')
    main.load_status_updates(filename, status_collection)
    print("time for load status updates")
    print(timer('load_status_updates', globals=globals(), number=repetitions))

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
        print("An error occurred while trying to add new user")
    else:
        print("User was successfully added")
    print("time for add user")
    print(timer('add_user', globals=globals(), number=repetitions))

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
        print("An error occurred while trying to update user")
    else:
        print("User was successfully updated")
    print("time for update user")
    print(timer('update_user', globals=globals(), number=repetitions))

def search_user():
    '''
    Searches a user in the database
    '''
    user_id = input('Enter user ID to search: ')
    result = main.search_user(user_id, user_collection)
    if result is None:
        print("ERROR: User does not exist")
    else:
        print(f"User ID: {result.user_id}")
        print(f"Email: {result.user_email}")
        print(f"Name: {result.user_name}")
        print(f"Last name: {result.user_last_name}")
    print("time for search user")
    print(timer('search_user', globals=globals(), number=repetitions))

def delete_user():
    '''
    Deletes user from the database
    '''
    user_id = input('User ID: ')
    if not main.delete_user(user_id, user_collection):
        print("An error occurred while trying to delete user")
    else:
        print("User was successfully deleted")
    print("time for delete user")
    print(timer('delete_user', globals=globals(), number=repetitions))

def add_status():
    '''
    Adds a new status into the database
    '''
    user_id = input('User ID: ')
    status_id = input('Status ID: ')
    status_text = input('Status text: ')
    if not main.add_status(status_id, user_id, status_text, status_collection):
        print("An error occurred while trying to add new status")
    else:
        print("New status was successfully added")
    print("time for add status")
    print(timer('add_status', globals=globals(), number=repetitions))

def update_status():
    '''
    Updates information for an existing status
    '''
    user_id = input('User ID: ')
    status_id = input('Status ID: ')
    status_text = input('Status text: ')
    if not main.add_status(status_id, user_id, status_text,
                           status_collection):
        print("An error occurred while trying to update status")
    else:
        print("Status was successfully updated")
    print("time for update status")
    print(timer('update_status', globals=globals(), number=repetitions))

def search_status():
    '''
    Searches a status in the database
    '''
    status_id = input('Enter status ID to search: ')
    result = main.search_status(status_id, status_collection)
    if result is None:
        print("ERROR: Status does not exist")
    else:
        print(f"User ID: {result.user_id}")
        print(f"Status ID: {result.status_id}")
        print(f"Status text: {result.status_text}")
    print("time for search status")
    print(timer('search_status', globals=globals(), number=repetitions))

def delete_status():
    '''
    Deletes status from the database
    '''
    status_id = input('Status ID: ')
    if not main.delete_status(status_id, status_collection):
        print("An error occurred while trying to delete status")
    else:
        print("Status was successfully deleted")
    print("time for delete status")
    print(timer('delete_status', globals=globals(), number=repetitions))

def quit_program():
    '''
    Quits program
    '''
    DB.close()
    sys.exit()


if __name__ == '__main__':
    DB.connect()
    DB.execute_sql('PRAGMA foreign_keys = ON;')
    DB.create_tables([UsersTable, StatusTable])

    user_collection = main.init_user_collection(UsersTable)
    status_collection = main.init_status_collection(StatusTable)
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
