from models.user import User
from peewee import *

db = SqliteDatabase('main.db')
db.connect()


def get_user_from_name_and_tag(_name, _tag):
    result = User.get(User.name == _name and User.tag == _tag)
    return result
