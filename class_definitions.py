from peewee import *
db = SqliteDatabase('main.db')


class User(Model):
    puuid = CharField()
    region = CharField()
    account_level = CharField()
    name = CharField()
    tag = CharField()

    class Meta:
        database = db


def execute():
    db.connect()
    db.create_tables([User], safe=True)
