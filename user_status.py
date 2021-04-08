'''
Classes for status information for the
social network project
'''

# pylint: disable=R0903

import logging
import pymongo


class UserStatusCollection():
    '''
    Contains a collection of User Status objects
    '''

    def __init__(self, _status_db):
        logging.info('New status collection instance created')
        self._status_db = _status_db

    def add_status(self, status_id, user_id, status_text):
        '''
        Adds a new status to the collection
        '''
        try:
            status_ip = {"_id": status_id, "user_id": user_id,
                         "status_text": status_text}
            self._status_db.insert_one(status_ip)
            logging.info("Add status")
            # print(status_ip)
            return True

        except pymongo.errors.DuplicateKeyError:
            logging.error('Status_id is already exists')
            print("Status_id is already exist at the database")
            return False

    def modify_status(self, status_id, user_id, status_text):
        '''
        Modifies an existing status
        '''
        for status in self._status_db.find():
            # print(status['_id'])
            if status_id == status['_id']:
                self._status_db.update_one({"_id": status_id}, {"$set": {
                    "user_id": user_id, "status_text": status_text}})
                logging.info('Status modified')
                return True
        logging.error('Status_id does not exists')
        return False

    def delete_status(self, status_id):
        '''
        Deletes an existing status
        '''
        for status in self._status_db.find():
            if status_id == status["_id"]:
                query = {"_id": status_id}
                self._status_db.delete_one(query)
                logging.info('Status_id is deleted')
                return True
        logging.error('Status_id does not exists')
        return False

    def delete_status_by_user_id(self, user_id):
        '''
        Deletes an existing status
        '''
        for user in self._status_db.find():
            if user_id == user['user_id']:
                query = {"_id": user['_id']}
                self._status_db.delete_many(query)
                logging.info('Status_id is deleted')
        logging.error('Status_id does not exists')
        return False

    def search_status(self, status_id):
        '''
        Searches for status data
        '''
        for status in self._status_db.find():
            # print(status['_id'])
            if status_id == status['_id']:
                logging.info('Status exist')
                return status
        logging.error('Status_id does not exists')
        print("Status_id doesn't exist at the database")
        return None
