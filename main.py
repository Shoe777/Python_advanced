'''
Functions to add/delete/modified and so on
information for the social network project
'''

import pandas as pd
import users
import user_status
import multiprocessing
from mongodb import DB
import concurrent.futures


def init_user_collection(users_db):
    '''
    Creates and returns a new instance
    of UserCollection
    '''
    new_uc = users.UserCollection(users_db)
    return new_uc


def init_status_collection(status_db):
    '''
    Creates and returns a new instance
    of UserStatusCollection
    '''
    new_usc = user_status.UserStatusCollection(status_db)
    return new_usc


def load_users(filename, size=300):
    '''
    Imports CSV file in chunks of a defined size
    '''
    cpu = multiprocessing.cpu_count()
    print(f'Number of cpu is: {cpu}')
    chunks = [chunk for chunk in pd.read_csv(filename, chunksize=size,
                                             iterator=True)]
    chunk_number = [i for i in range(len(chunks))]
    print('Starting workers')
    with concurrent.futures.ProcessPoolExecutor(max_workers=6) as executor:
        for chunk_idx, result in zip(chunk_number,
                                     executor.map(worker1,
                                                  zip(chunks, chunk_number))):
            print(f"CHUNK {chunk_idx}")
            print(f"CHUNK {result}")
            executor.shutdown(wait=True)
            print('Done')


def worker1(pair):
    chunk, idx = pair
    UserAccounts = DB['UserAccounts']
    user_collection = init_user_collection(UserAccounts)
    for index, row in chunk.iterrows():
        user_id = row['USER_ID']
        user_name = row['NAME']
        user_last_name = row['LASTNAME']
        email = row['EMAIL']  # unpack
        created = user_collection.add_user(user_id, user_name,
                                           user_last_name, email)
        if not created:
            print('user_id is already exist')
            continue


def load_status_updates(filename, size=25000):
    '''
    Imports CSV file in chunks of a defined size
    '''
    chunks = [chunk for chunk in pd.read_csv(filename, chunksize=size,
                                             iterator=True)]
    chunk_number = [i for i in range(len(chunks))]
    print('Starting workers')
    with concurrent.futures.ProcessPoolExecutor(max_workers=8) as executor:
        for chunk_idx, result in zip(chunk_number,
                                     executor.map(worker2, zip(chunks,
                                                               chunk_number))):
            print(f"CHUNK {chunk_idx}")
            executor.shutdown(wait=True)
            print('Done')


def worker2(pair):
    chunk, idx = pair
    StatusUpdates = DB['StatusUpdates']
    status_collection = init_status_collection(StatusUpdates)
    for index, row in chunk.iterrows():
        status_id = row['STATUS_ID']
        user_id = row['USER_ID']
        status_text = row['STATUS_TEXT']
        created = status_collection.add_status(status_id, user_id, status_text)
        if not created:
            print('user_id is already exist')
            continue


def add_user(user_id, user_name, user_last_name, email, user_collection):
    '''
    Creates a new instance of User and stores it in user_collection
    (which is an instance of UserCollection)

    Requirements:
    - user_id cannot already exist in user_collection.
    - Returns False if there are any errors (for example, if
    user_collection.add_user() returns False).
    - Otherwise, it returns True.
    '''
    return user_collection.add_user(user_id, user_name, user_last_name, email)


def update_user(user_id, user_name, user_last_name, email, user_collection):
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


def delete_status_by_user_id(user_id, status_collection):
    '''
    Deletes a status_id from user_collection by user_id.
    '''
    return status_collection.delete_status_by_user_id(user_id)


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
