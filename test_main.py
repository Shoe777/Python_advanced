# pylint: disable=W0614
# pylint: disable=W0401
# pylint: disable=C0116

'''
Test File
'''
from unittest import TestCase
import user_status as US
import users as U
from playhouse.dataset import DataSet

# Create an empty Database
DB = DataSet('sqlite:///:memory:')
USERS_TABLE = DB['UsersTable']
STATUS_TABLE = DB['StatusTable']


def _is_empty_user(user):  # Will return None
    return user is None


class UsersTests(TestCase):
    '''
    Test for functions from user.py
    '''

    def setUp(self):  # setUp is called before each individual test
        print("Test of function from users.py")
        self.new_uc = U.UserCollection(USERS_TABLE)
        table = U.UserCollection(USERS_TABLE)._users_db
        table.insert(USER_ID='test')
        table.create_index(['USER_ID'], unique=True)
        table.delete(USER_ID='test')
        self.new_uc.add_user('alex', 'alex_name',
                             'alex_last_name', 'a@a')  # create known db
        # print(self.new_uc['USER_ID'])

    def tearDown(self):  # tearDown is called after every test
        print("End of test for function from users.py")

    def test_delete_user_exist(self):
        expected = True
        # Check if the user_id is exist.
        # Then delete it.
        # Check if there is no such user_id in the file
        self.assertFalse(_is_empty_user(self.new_uc.search_user('alex')))
        self.assertEqual(self.new_uc.delete_user('alex'), expected)
        self.assertTrue(_is_empty_user(self.new_uc.search_user('alex')))

    def test_delete_user_absent(self):
        # Check if the user_id is not exist.
        # Then try to delete it.
        self.assertTrue(_is_empty_user(self.new_uc.search_user('zzz')))
        self.assertEqual(self.new_uc.delete_user('zzz'), False)

    def test_search_user_exist(self):
        expected = ('alex_last_name')
        # check if the search_user function return user_last_name
        user_data = self.new_uc.search_user('alex')
        self.assertEqual(user_data['LASTNAME'], expected)

    def test_search_user_absent(self):
        expected = None
        user_data = self.new_uc.search_user('zzz')
        self.assertEqual(user_data, expected)

    def test_modify_user_exist(self):
        expected = True
        self.assertFalse(_is_empty_user(self.new_uc.search_user('alex')))
        #  modify user_email
        self.assertEqual(self.new_uc.modify_user('alex', 'new@a', 'alex_name',
                                                 'alex_last_name'), expected)
        # check that user_email is modified
        user_data = self.new_uc.search_user('alex')
        self.assertEqual(user_data['EMAIL'], 'new@a')

    def test_modify_user_absent(self):
        expected = False
        self.assertEqual(self.new_uc.modify_user('zzz', 'new@a', 'alex_name',
                                                 'alex_last_name'), expected)

    def test_add_user_success(self):
        expected = True
        self.assertTrue(_is_empty_user(self.new_uc.search_user('zzz_01')))
        self.assertEqual(self.new_uc.add_user('zzz_01', 'z@gmail', 'zzz_name',
                                              'zzz_last_name'), expected)
        #  check there is new user_id 'zzz_01' in the data base
        self.assertFalse(_is_empty_user(self.new_uc.search_user('zzz_01')))

    def test_add_user_fail(self):
        # Test if user_id is already exist
        expected = False
        self.assertFalse(_is_empty_user(self.new_uc.search_user('alex')))
        self.assertEqual(self.new_uc.add_user('alex', 'alex', 'alex', 'alex'),
                         expected)

    def test_add_user_fail_length(self):
        # Test if user_id length exceed limitation
        expected = False
        self.assertTrue(_is_empty_user(self.new_uc.search_user(
            'alex30lettersaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')))
        self.assertEqual(self.new_uc.add_user(
            'alex30lettersaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa', 'alex', 'alex',
            'alex'),
                         expected)


def _is_empty_status(status):  # Will return None
    return status is None


class UsersStatusTests(TestCase):
    '''
    Test for functions from user_status.py
    '''

    def setUp(self):  # setUp is called before each individual test
        print("Test of function from user_status.py")
        self.new_uc = U.UserCollection(USERS_TABLE)
        table = U.UserCollection(USERS_TABLE)._users_db
        table.insert(USER_ID='test')
        table.create_index(['USER_ID'], unique=True)
        table.delete(USER_ID='test')
        self.new_uc.add_user('alex', 'alex_name',
                             'alex_last_name', 'a@a')  # create known db
        # print(self.new_uc['USER_ID'])
        self.new_usc = US.UserStatusCollection(STATUS_TABLE, self.new_uc)
        s_table = US.UserStatusCollection(STATUS_TABLE, U)._status_db
        s_table.insert(STATUS_ID='test')
        s_table.create_index(['STATUS_ID'], unique=True)
        s_table.delete(STATUS_ID='test')
        self.new_usc.add_status('alex01', 'alex', 'Congratulation')
        self.new_usc.add_status('alex02', 'alex', 'Hello')  #
        # create new known Table

    def tearDown(self):  # tearDown is called after every test
        print("End of test for function from user_status.py ")

    def test_delete_status_exist(self):
        expected = True
        # Check if the status_id is exist.
        # Then delete it.
        # Check if there is no such status_id in the file
        self.assertFalse(_is_empty_status(self.new_usc.search_status(
            'alex01')))
        self.assertEqual(self.new_usc.delete_status('alex01'), expected)
        self.assertTrue(_is_empty_status(self.new_usc.search_status(
            'alex01')))

    def test_delete_status_absent(self):
        # Check if the user_id is not exist.
        # Then try to delete it.
        self.assertTrue(_is_empty_status(self.new_usc.search_status('zzz')))
        self.assertEqual(self.new_usc.delete_status('zzz'), False)

    def test_search_status_exist(self):
        expected = 'Congratulation'
        # check if the search_status function return status_text
        status_data = self.new_usc.search_status('alex01')
        self.assertEqual(status_data['STATUS_TEXT'], expected)

    def test_search_status_absent(self):
        expected = None
        status_data = self.new_usc.search_status('zzz_02')
        self.assertEqual(status_data, expected)

    def test_modify_status_exist(self):
        expected = True
        self.assertFalse(_is_empty_status(self.new_usc.search_status(
            'alex01')))
        # modify status_text
        self.assertEqual(
            self.new_usc.modify_status('alex02', 'alex02',
                                       'Double Hello'),
            expected)
        # check that Status_text is modified
        status_data = self.new_usc.search_status('alex02')
        self.assertEqual(status_data['STATUS_TEXT'], 'Double Hello')

    def test_modify_status_absent(self):
        expected = False
        self.assertEqual(
            self.new_usc.modify_status('new_zzz01', 'zzzz', 'Congratulation'),
            expected)

    def test_add_status_success(self):
        expected = True
        self.assertTrue(_is_empty_status(self.new_usc.search_status(
            'zzz01')))
        self.assertEqual(
            self.new_usc.add_status('zzz01', 'alex', 'Nice Congratulation'),
            expected)
        # check there is new status_id 'zzz01' in the data base
        self.assertFalse(_is_empty_status(self.new_usc.search_status('zzz01')))

    def test_add_status_fail(self):
        # Test if status_id is already exist
        expected = False
        self.assertFalse(_is_empty_status(self.new_usc.search_status(
            'alex02')))
        self.assertEqual(self.new_usc.add_status('alex02', 'alex',
                                                 'Congrats'), expected)

    def test_add_status_fail_2(self):
        # There is no corresponding User_id in database
        expected = False
        self.assertFalse(_is_empty_status(self.new_usc.search_status(
            'alex02')))
        self.assertEqual(self.new_usc.add_status('alex02', 'alex111',
                                                 'No Status'), expected)
