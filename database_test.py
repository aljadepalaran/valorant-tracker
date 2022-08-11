from models.user import User
from peewee import *

db = SqliteDatabase('main.db')  # define which db to use
db.connect()  # connect to the db
db.create_tables([User])  # create the database

try:
    User.create(puuid="SEED-1",
                region="eu",
                account_level=1,
                image_small_url='SEED-image-small-1',
                image_large_url='SEED-image-large-1',
                image_wide_url='SEED-image-wide-1',
                name="SEED-name-1",
                tag="SEED-tag-1")
except IntegrityError:
    print('Something wrong')
