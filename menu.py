'''
Provides a basic frontend
'''

# pylint: disable=C0103
# Disable only for names "user_collection" and "status_collection"

from timeit import timeit as timer
import time
from datetime import datetime
import logging
import sys
import main
from mongodb import DB

LOG_FORMAT = "%(asctime)s %(filename)s:%(lineno)-3d %(levelname)s %(message)s"
FILENAME_CUSTOM = datetime.now().strftime('log_%m_%d_%Y.log')
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT,
                    filename=FILENAME_CUSTOM)
logging.info("menu.py testing is started.")

# repetitions = 1000

def load_users():
    '''
    Loads user accounts from a file
    '''
    filename = input('Enter filename of user file: ')
    tic = time.perf_counter()
    main.load_users(filename)
    toc = time.perf_counter()
    print(f"time for load users in {toc-tic:0.4f} second")
    # print(timer('load_users', globals=globals(), number=repetitions))


def load_status_updates():
    '''
    Loads status updates from a file
    '''
    filename = input('Enter filename for status file: ')
    tic = time.perf_counter()
    main.load_status_updates(filename)
    toc = time.perf_counter()
    print(f"time for load status in {toc-tic:0.4f} second")


def add_user():
    '''
    Adds a new user into the database
    '''
    user_id = input('User ID: ')
    user_name = input('User name: ')
    user_last_name = input('User last name: ')
    email = input('User email: ')
    if not main.add_user(user_id, user_name, user_last_name, email,
                         user_collection):
        print("An error occurred while trying to add new user")
    else:
        print("User was successfully added")


def update_user():
    '''
    Updates information for an existing user
    '''
    user_id = input('User ID: ')
    user_name = input('User name: ')
    user_last_name = input('User last name: ')
    email = input('User email: ')
    tic = time.perf_counter()
    if not main.update_user(user_id, user_name, user_last_name, email,
                            user_collection):
        print("An error occurred while trying to update user")
    else:
        print("User was successfully updated")
    toc = time.perf_counter()
    print(f"time for user update in {toc-tic:0.4f} second")


def search_user():
    '''
    Searches a user in the database
    '''
    user_id = input('Enter user ID to search: ')
    tic = time.perf_counter()
    result = main.search_user(user_id, user_collection)
    if result is None:
        print("ERROR: User does not exist")
    else:
        print(f'User ID: {result["_id"]}')
        print(f'Email: {result["user_email"]}')
        print(f'Name: {result["user_name"]}')
        print(f'Last name: {result["user_last_name"]}')
    toc = time.perf_counter()
    print(f"time for search user is {toc-tic:0.4f} second")


def delete_user():
    '''
    Deletes user from the database
    '''
    user_id = input('User ID: ')
    if not main.delete_user(user_id, user_collection):
        print("An error occurred while trying to delete user")
    else:
        main.delete_status_by_user_id(user_id,
                                      status_collection)
        print("User was successfully deleted")


def add_status():
    '''
    Adds a new status into the database
    '''
    status_id = input('Status ID: ')
    user_id = input('User ID: ')
    status_text = input('Status text: ')
    tic = time.perf_counter()
    if main.search_user(user_id, user_collection) is not None:
        if not main.add_status(status_id, user_id, status_text,
                               status_collection):
            print("An error occurred while trying to add new status")
        else:
            print("New status was successfully added")
    else:
        print("There is no associated User_id for this Status")
    toc = time.perf_counter()
    print(f"time to add status is {toc-tic:0.4f} second")


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
    status_id = input('Enter Status_ID to search: ')
    tic = time.perf_counter()
    result = main.search_status(status_id, status_collection)
    if result is None:
        print("ERROR: Status does not exist")
    else:
        print(f"Status ID: {result['_id']}")
        print(f"User ID: {result['user_id']}")
        print(f"Status text: {result['status_text']}")
    toc = time.perf_counter()
    print(f"time to search status is {toc-tic:0.4f} second")

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
    yorn = input("drop DB? (y/n)")
    if yorn.upper == "Y":
        DB.drop_database('UserAccounts')
        DB.drop_database('StatusUpdates')
        # StatusUpdates.drop()
    sys.exit()


if __name__ == '__main__':
    UserAccounts = DB['UserAccounts']
    StatusUpdates = DB['StatusUpdates']

    user_collection = main.init_user_collection(UserAccounts)
    status_collection = main.init_status_collection(StatusUpdates)
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