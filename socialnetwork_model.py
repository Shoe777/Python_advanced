# pylint: disable=R0903
'''
Create a DataBase
'''

import os
import peewee as pw

FILE = 'SocialDatabase.db'
if os.path.exists(FILE):
    os.remove(FILE)

DB = pw.SqliteDatabase(FILE)


#  For Unittesting
# DB = pw.SqliteDatabase(':memory:')

class BaseModel(pw.Model):
    """
    BaseModel
    """

    class Meta:
        """
        Meta
        """
        database = DB


class UsersTable(BaseModel):
    """
    This class defines Users and create Users table in database
    """

    user_id = pw.CharField(primary_key=True, max_length=30)
    user_name = pw.CharField(max_length=30)
    user_last_name = pw.CharField(max_length=100)
    user_email = pw.CharField()

    def show(self):
        """ Display an instance of Users"""
        print(self.user_id, self.user_name, self.user_last_name,
              self.user_email)


class StatusTable(BaseModel):
    """
    This class defines User's status and create Status table in database
    """

    status_id = pw.CharField(primary_key=True)
    user_id = pw.ForeignKeyField(UsersTable, on_delete='CASCADE', null=False)
    status_text = pw.CharField()

    def shows(self):
        """ Display an instance of Status"""
        print(self.status_id, self.user_id, self.status_text)
