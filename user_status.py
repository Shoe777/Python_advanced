'''
Classes for user status information for the
social network project
'''

# pylint: disable=W0614
# pylint: disable=W0401

from peewee import *


class UserStatusCollection():
    '''
    Contains a collection of Users Status objects
    '''

    def __init__(self, _status_db):
        self._status_db = _status_db

    def add_status(self, status_id, user_id, status_text):
        '''
        Adds a new status to the collection
        '''
        try:
            new_status = self._status_db.create(status_id=status_id,
                                                user_id=user_id,
                                                status_text=status_text)
            new_status.save()
            return True
        except IntegrityError:
            print("Status is already exist")
            return False

    def modify_status(self, status_id, user_id, status_text):
        '''
        Modify a new status at the collection
        '''
        try:
            status = self._status_db.get(self._status_db.status_id ==
                                         status_id)
            status.user_id = user_id
            status.status_text = status_text
            status.save()
            return True
        except DoesNotExist:
            print("Status_id doesn't exist at the database")
            return False

    def delete_status(self, status_id):
        '''
        Delete status from the collection
        '''
        try:
            status = self._status_db.get(self._status_db.status_id ==
                                         status_id)
            status.delete_instance()
            return True
        except DoesNotExist:
            print("Status_id doesn't exist at the database")
            return False

    def search_status(self, status_id):
        '''
        Search a status at the collection
        '''
        try:
            status = self._status_db.get(self._status_db.status_id ==
                                         status_id)
            return status
        except DoesNotExist:
            print("Status_id doesn't exist at the database")
            return None

    def search_all_status_updates(self, user_id):
        '''
        Search all status updates for that user
        '''

        query = self._status_db.select().where(
            self._status_db.user_id == user_id)
        return [status.status_text for status in query]

    def filter_status_by_string(self, text):
        '''
        Search all status updates matching a string
        '''
        query = self._status_db.select().where(
            self._status_db.status_text.contains(text)).iterator()
        return query
