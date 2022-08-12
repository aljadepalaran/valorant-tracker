from peewee import *
import time
import Debug

db = SqliteDatabase('main.db')


class User(Model):
    puuid = CharField(unique=True)
    region = CharField()
    account_level = CharField()
    image_small_url = CharField()
    image_large_url = CharField()
    image_wide_url = CharField()
    name = CharField()
    tag = CharField()
    time_last_updated_unix = IntegerField()

    class Meta:
        database = db

    def should_update_from_api(self):
        Debug.log(f"#should_update_from_api, data: {self.time_last_updated_unix + 300 < time.time()}")
        return self.time_last_updated_unix + 300 < time.time()
