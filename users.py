'''
Classes for user information for the
social network project
'''

# pylint: disable=W0703

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
        except Exception as exep:
            print(exep)
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
        except Exception as exep:
            print(exep)
            return False

    def delete_user(self, user_id):
        '''
        Deletes an existing user
        '''
        try:
            user = self._users_db.get(self._users_db.user_id == user_id)
            user.delete_instance()
            return True
        except Exception as exep:
            print(exep)
            return False

    def search_user(self, user_id):
        '''
        Searches for user data
        '''
        try:
            user = self._users_db.get(self._users_db.user_id == user_id)
            return user
        except Exception as exep:
            print(exep)
            return None
        # except IntegrityError:
        #     print("user_id doesn't not exist")
        #     return None
