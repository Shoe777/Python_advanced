# pylint: disable=W0703

'''
Classes for user status information for the
social network project
'''
from peewee import *


class UserStatusCollection():
    '''
    Contains a collection of Users Status objects
    '''

    def __init__(self, _status_db):
        self._status_db = _status_db

    def __iter__(self):
        return self

    def __next__(self):
        return self.next()

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

        # # TODO counting:
        # query = self._status_db.select().where(
        #     self._status_db.user_id == user_id).count()
        #
        # return query



        for query in self._status_db.select().where(
            self._status_db.user_id == user_id):
            yield query.status_text

        # TODO list comprehension?
        # return [status.status_text for status in query]
        # query.iterator()
        # for status in query:
        #     yield status.status_text

    # count = 0
    # for count in query:
    #     count += 1
    #     return count.save()


# TODO queries are smart, in that you can iterate, index and slice the query
# TODO  multiple times but the query is only executed once.


# # TODO to extract one status use .get?
# while True:
#     status = self._status_db.get(self._status_db.used_id == user_id)
#     yield status.status_text
# else:
#     print(f"You have reached the last update for {user_id}")

def filter_status_by_string(self):
    query = self._status_db.select().where(
        self._status_db.status_text.contains('Check')).iterator()
    next_result = next(query)
    print(f"User: {next_result.status_text}")
    pass
