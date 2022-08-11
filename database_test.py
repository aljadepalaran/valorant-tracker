from models.user import User
from peewee import *

User.create(puuid="test",
            region="eu",
            account_level=1,
            name="c00k1e",
            tag="1234")
