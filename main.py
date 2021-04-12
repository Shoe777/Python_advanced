'''
Functions to add/delete/modified and so on
information for the social network project
'''
# pylint: disable=W0614
# pylint: disable=W0212
# pylint: disable=W0401

from peewee import *
import users
import user_status


def init_user_collection(users_table):
    '''
    Creates and returns a new instance
    of UserCollection
    '''
    new_uc = users.UserCollection(users_table)
    return new_uc


def init_status_collection(status_table, user_collection):
    '''
    Creates and returns a new instance
    of UserStatusCollection
    '''
    new_usc = user_status.UserStatusCollection(status_table, user_collection)
    return new_usc


def load_users(filename, user_collection):
    '''
    Opens a CSV file with user data and
    adds it to an existing instance of
    UserCollection

    Requirements:
    - If a user_id already exists, it
    will ignore it and continue to the
    next.
    - Returns False if there are any errors
    (such as empty fields in the source CSV file)
    - Otherwise, it returns True.
    '''
    table = user_collection._users_db
    table.insert(USER_ID='test')
    table.create_index(['USER_ID'], unique=True)
    table.delete(USER_ID='test')
    try:
        table.thaw(filename=filename, format='csv')
    except IntegrityError:
        print(f"issues with {filename}: User_id is already "
              f"exist")
    # table.all()[:4]


def load_status_updates(filename, status_collection, user_collection):
    '''
    Opens a CSV file with status data and
    adds it to an existing instance of
    UserStatusCollection

    Requirements:
    - If a status_id already exists, it
    will ignore it and continue to the
    next.
    - Returns False if there are any errors
    (such as empty fields in the source CSV file)
    - Otherwise, it returns True.
    '''
    s_table = status_collection._status_db
    s_table.insert(STATUS_ID='test')
    s_table.create_index(['STATUS_ID'], unique=True)
    s_table.delete(STATUS_ID='test')
    try:
        s_table.thaw(filename=filename, format='csv')
        for row in s_table:
            if user_collection.search_user(row['USER_ID']):
                continue
            status_collection.delete_status(row['STATUS_ID'])
    except IntegrityError:
        print(f"issues with {filename}: Status_id is already "
              f"exist")
    # s_table.all()[:3]

def add_user(user_id, email, user_name, user_last_name, user_collection):
    '''
    Creates a new instance of User and stores it in user_collection
    (which is an instance of UserCollection)

    Requirements:
    - user_id cannot already exist in user_collection.
    - Returns False if there are any errors (for example, if
    user_collection.add_user() returns False).
    - Otherwise, it returns True.
    '''
    return user_collection.add_user(user_id, email, user_name, user_last_name)


def update_user(user_id, email, user_name, user_last_name, user_collection):
    '''
    Updates the values of an existing user

    Requirements:
    - Returns False if there any errors.
    - Otherwise, it returns True.
    '''
    return user_collection.modify_user(user_id, email, user_name,
                                       user_last_name)


def delete_user(user_id, user_collection):
    '''
    Deletes a user from user_collection.

    Requirements:
    - Returns False if there are any errors (such as user_id not found)
    - Otherwise, it returns True.
    '''
    return user_collection.delete_user(user_id)


def search_user(user_id, user_collection):
    '''
    Searches for a user in user_collection
    (which is an instance of UserCollection).

    Requirements:
    - If the user is found, returns the corresponding
    User instance.
    - Otherwise, it returns None.
    '''
    user = user_collection.search_user(user_id)
    return user


def add_status(status_id, user_id, status_text, status_collection):
    '''
    Creates a new instance of UserStatus and stores it in user_collection
    (which is an instance of UserStatusCollection)

    Requirements:
    - status_id cannot already exist in user_collection.
    - Returns False if there are any errors (for example, if
    user_collection.add_status() returns False).
    - Otherwise, it returns True.
    '''
    return status_collection.add_status(status_id, user_id, status_text)


def update_status(status_id, user_id, status_text, status_collection):
    '''
    Updates the values of an existing status_id

    Requirements:
    - Returns False if there any errors.
    - Otherwise, it returns True.
    '''
    return status_collection.modify_status(status_id, user_id, status_text)


def delete_status(status_id, status_collection):
    '''
    Deletes a status_id from user_collection.

    Requirements:
    - Returns False if there are any errors (such as status_id not found)
    - Otherwise, it returns True.
    '''
    return status_collection.delete_status(status_id)


def search_status(status_id, status_collection):
    '''
    Searches for a status in status_collection

    Requirements:
    - If the status is found, returns the corresponding
    UserStatus instance.
    - Otherwise, it returns None.
    '''
    status = status_collection.search_status(status_id)
    return status
