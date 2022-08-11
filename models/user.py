from peewee import *
db = SqliteDatabase('main.db')


class User(Model):
    puuid = CharField()
    region = CharField()
    account_level = CharField()
    image_small_url = CharField()
    image_large_url = CharField()
    image_wide_url = CharField()
    name = CharField()
    tag = CharField()

    class Meta:
        database = db
