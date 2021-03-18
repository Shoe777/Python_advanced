'''
Classes for user information for the
social network project
'''

# pylint: disable=W0703
# pylint: disable=W0614

from peewee import *


class UserCollection():
    '''
    Contains a collection of Users objects
    '''

    def __init__(self, users_db):
        self._users_db = users_db

    def add_user(self, user_id, email, user_name, user_last_name):
        '''
        Adds a new user to the collection
        '''
        try:
            new_user = self._users_db.create(user_id=user_id,
                                             user_name=user_name,
                                             user_last_name=user_last_name,
                                             user_email=email)
            new_user.save()
            return True
        except IntegrityError:
            print("User is already exist")
            # except IntegrityError as e:      #TODO what's the best practices?
            #     print("Error: {}".format(e))
            return False

    def modify_user(self, user_id, email, user_name, user_last_name):
        '''
        Modifies an existing user
        '''
        try:
            user = self._users_db.get(self._users_db.user_id == user_id)

            user.user_email = email
            user.user_name = user_name
            user.user_last_name = user_last_name
            user.save()
            return True
        except DoesNotExist:
            print("User_id doesn't exist at the database")
            return False

    def delete_user(self, user_id):
        '''
        Deletes an existing user
        '''
        try:
            user = self._users_db.get(self._users_db.user_id == user_id)
            user.delete_instance()
            return True
        except DoesNotExist:
            print("User_id doesn't exist at the database")
            return False

    def search_user(self, user_id):
        '''
        Searches for user data
        '''
        try:
            user = self._users_db.get(self._users_db.user_id == user_id)
            return user
        except DoesNotExist:
            print("User_id doesn't exist at the database")
            return None
