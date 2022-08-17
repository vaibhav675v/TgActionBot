
from decouple import config
from heroku3 import from_key
from os import getenv

class Var:
    API_ID = config("API_ID", "10897780", default=6, cast=int)
    API_HASH = config("API_HASH", "7fb84143bb5f12156dc1835355d4e70e")
    TOKEN = config("TOKEN", "5696580119:AAF0fIrLges-k7zXj_5PgVoCSX01wVjfktw")
    OWNER_ID = list(map(int, getenv("OWNER_ID", "5363436020").split()))
