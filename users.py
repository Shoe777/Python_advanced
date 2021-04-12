'''
Classes for user information for the
social network project
'''

# pylint: disable=W0703
# pylint: disable=W0614
# pylint: disable=W0401

from peewee import *


class UserCollection():
    '''
    Contains a collection of Users objects
    '''

    def __init__(self, USERS_TABLE):
        self._users_db = USERS_TABLE

    def add_user(self, user_id, user_name, user_last_name, email):
        '''
        Adds a new user to the collection
        '''
        try:
            if len(user_id) > 30 or len(user_name) > 30 or len(
                    user_last_name) > 100:
                print('Exceed limitation')
                return False
            # self._users_db.insert(USER_ID='test')
            # self._users_db.create_index(['USER_ID'], unique=True)
            # self._users_db.delete(USER_ID='test')
            self._users_db.insert(USER_ID=user_id, NAME=user_name,
                                  LASTNAME=user_last_name,
                                  EMAIL=email)
            return True
        except IntegrityError:
            print("User_id is already exist at the database")
            return False

    def modify_user(self, user_id, email, user_name, user_last_name):
        '''
        Modifies an existing user
        '''

        if self._users_db.find_one(USER_ID=user_id) is None:
            return False
        self._users_db.update(USER_ID=user_id, NAME=user_name,
                              LASTNAME=user_last_name,
                              EMAIL=email, columns=['USER_ID'])
        return True

    def delete_user(self, user_id):
        '''
        Deletes an existing user
        '''
        if self._users_db.find_one(USER_ID=user_id) is None:
            return False
        self._users_db.delete(USER_ID=user_id)
        return True

    def search_user(self, user_id):
        '''
        Searches for user data
        '''
        user = self._users_db.find_one(USER_ID=user_id)
        return user
