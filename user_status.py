'''
Classes for user status information for the
social network project
'''

# pylint: disable=W0703
# pylint: disable=W0614
# pylint: disable=W0401
# pylint: disable=R1710

from peewee import *


class UserStatusCollection():
    '''
    Contains a collection of Users Status objects
    '''

    def __init__(self, STATUS_table, user_collection):
        self._status_db = STATUS_table
        self._user_collection = user_collection

    def add_status(self, status_id, user_id, status_text):
        '''
        Adds a new status to the collection
        '''
        try:
            if self._user_collection.search_user(user_id):
                self._status_db.insert(STATUS_ID=status_id, USER_ID=user_id,
                                       STATUS_TEXT=status_text)
                return True
            print("There is no corresponding User_id in database")
            return False
        except IntegrityError:
            print("Status_id is already exist at the database")
            return False

    def modify_status(self, status_id, user_id, status_text):
        '''
        Modify a new status at the collection
        '''
        if self._status_db.find_one(STATUS_ID=status_id) is None:
            return False
        self._status_db.update(STATUS_ID=status_id, USER_ID=user_id,
                               STATUS_TEXT=status_text, columns=['STATUS_ID'])
        return True

    def delete_status(self, status_id):
        '''
        Delete status from the collection
        '''
        if self._status_db.find_one(STATUS_ID=status_id) is None:
            return False
        self._status_db.delete(STATUS_ID=status_id)
        return True

    def search_status(self, status_id):
        '''
        Search a status at the collection
        '''
        status = self._status_db.find_one(STATUS_ID=status_id)
        return status
