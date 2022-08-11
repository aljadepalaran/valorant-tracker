from models.user import User
from peewee import *
import time

db = SqliteDatabase('main.db')  # define which db to use
db.connect()  # connect to the db

result = User.get(User.name == 'SEED-name-1')  # get a single User
results = User.select(User).where(User.name == 'SEED-name-1')  # returns array of User

print(result.puuid)  # puuid of result
print(results[0].puuid)  # puuid of first User in array
