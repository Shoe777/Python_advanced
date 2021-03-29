'''
Functions to add/delete/modified and so on
information for the social network project
'''

import csv
import users
import user_status


def init_user_collection():
    '''
    Creates and returns a new instance
    of UserCollection
    '''
    new_uc = users.UserCollection()
    return new_uc


def init_status_collection():
    '''
    Creates and returns a new instance
    of UserStatusCollection
    '''
    new_usc = user_status.UserStatusCollection()
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
    errors = False
    with open(filename, newline='') as csv_accounts:
        accounts_reader = csv.reader(csv_accounts)
        next(accounts_reader)  # ignoring header
        for row in accounts_reader:
            if len(row) < 4:  # check for empty rows
                errors = True
                continue
            if any(not x.strip() for x in row):  # check for empty cells
                errors = True
                continue
            user_id, email, user_name, user_last_name = row  # unpack
            if user_id in user_collection.database:
                print('user_id is already exist')
                errors = True
                continue
            user_collection.add_user(user_id, email, user_name, user_last_name)
        return not errors


def save_users(filename, user_collection):
    '''
    Saves all users in user_collection into
    a CSV file

    Requirements:
    - If there is an existing file, it will
    overwrite it.
    - Returns False if there are any errors
    (such an invalid filename).
    - Otherwise, it returns True.
    '''
    errors = False
    fields = ['USER_ID', 'EMAIL', 'NAME', 'LASTNAME']
    if filename.lower().endswith('.csv'):
        with open(filename, 'w') as writer:
            wtr = csv.writer(writer, lineterminator='\n')
            wtr.writerow(fields)
            for user in user_collection.database:
                data = user_collection.database[user]
                values = [data.user_id, data.email, data.user_name,
                          data.user_last_name]
                wtr.writerow(values)
    else:
        errors = True
    return not errors


def load_status_updates(filename, status_collection):
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
    errors = False
    with open(filename, newline='') as csv_status_upd:
        status_reader = csv.reader(csv_status_upd, delimiter=',')
        next(status_reader)  # ignoring header
        for row in status_reader:
            if len(row) < 3:  # check for empty rows
                errors = True
                continue
            if any(not x.strip() for x in row):  # check for empty cells
                errors = True
                continue

            status_id, user_id, status_text = row  # unpack
            if status_id in status_collection.database:
                print('status_id is already exist')
                errors = True
                continue
            status_collection.add_status(status_id, user_id, status_text)
        return not errors


def save_status_updates(filename, status_collection):
    '''
    Saves all statuses in status_collection into
    a CSV file

    Requirements:
    - If there is an existing file, it will
    overwrite it.
    - Returns False if there are any errors
    (such an invalid filename).
    - Otherwise, it returns True.
    '''
    errors = False
    fields = ['STATUS_ID', 'USER_ID', 'STATUS_TEXT']
    if filename.lower().endswith('.csv'):
        with open(filename, 'w') as writer:
            wtr = csv.writer(writer, lineterminator='\n')
            wtr.writerow(fields)
            for status in status_collection.database:
                data = status_collection.database[status]
                values = [data.status_id, data.user_id, data.status_text]
                wtr.writerow(values)
    else:
        errors = True
    return not errors


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
    if user.user_id is not None:
        return user
    return None


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
    if status.status_id is not None:
        return status
    return None
