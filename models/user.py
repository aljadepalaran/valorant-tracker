from peewee import *
db = SqliteDatabase('main.db')


class User(Model):
    puuid = CharField(unique=True)
    region = CharField()
    account_level = IntegerField()
    image_small_url = CharField()
    image_large_url = CharField()
    image_wide_url = CharField()
    name = CharField()
    tag = CharField()

    class Meta:
        database = db
