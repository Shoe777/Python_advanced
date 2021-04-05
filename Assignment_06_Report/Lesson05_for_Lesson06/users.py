'''
Classes for user information for the
social network project
'''

# pylint: disable=R0903
import logging
import pymongo


class UserCollection():
    """
    Contains a collection of Users objects
    """

    def __init__(self, _users_db):
        logging.info('New user collection instance created')
        self._users_db = _users_db

    def add_user(self, user_id, user_name, user_last_name, email):
        '''
        Adds a new user to the collection
        '''
        try:
            users_ip = {"_id": user_id, "user_name": user_name,
                        "user_last_name": user_last_name, "user_email": email}
            self._users_db.insert_one(users_ip)
            # print(users_ip)
            # print("TOTAL DOCS:", self._users_db.count_documents({}))
            return True

        except pymongo.errors.DuplicateKeyError:
            print("User_id is already exist at the database")
            return False

    def modify_user(self, user_id, email, user_name, user_last_name):
        '''
        Modifies an existing user
        '''
        for user in self._users_db.find():
            if user_id == user["_id"]:
                self._users_db.update_one({"_id": user_id}, {"$set": {
                    "user_email": email, "user_name": user_name,
                    "user_last_name": user_last_name}})
                logging.info('User modified')
                return True
        logging.error('User_id does not exists')
        return False

    def delete_user(self, user_id):
        '''
        Deletes an existing user
        '''
        for user in self._users_db.find():
            if user_id == user["_id"]:
                query = {"_id": user_id}
                self._users_db.delete_one(query)
                logging.info('User deleted')
                return True
        logging.error('User_id does not exists')
        return False

    def search_user(self, user_id):
        '''
        Searches for user data
        '''
        for user in self._users_db.find():
            # print(user['_id'])
            if user_id == user['_id']:
                return user
        print("User_id doesn't exist at the database")
        return None
