from class_definitions import User, execute
from peewee import *

execute()  # creates classes and database

User.create(puuid="test",
            region="eu",
            account_level=1,
            name="c00k1e",
            tag="1234")
