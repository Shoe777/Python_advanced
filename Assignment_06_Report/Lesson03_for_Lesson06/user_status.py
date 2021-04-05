# pylint: disable=W0703

'''
Classes for user status information for the
social network project
'''

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
        except Exception as exep:
            print(exep)
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
        except Exception as exep:
            print(exep)
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
        except Exception as exep:
            print(exep)
            return False

    def search_status(self, status_id):
        '''
        Search a status at the collection
        '''
        try:
            status = self._status_db.get(self._status_db.status_id ==
                                         status_id)
            return status
        except Exception as exep:
            print(exep)
            return None
