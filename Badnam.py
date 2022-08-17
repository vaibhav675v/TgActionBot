
from decouple import config
from heroku3 import from_key
from os import getenv

class Var:
    API_ID = config("10897780", default=6, cast=int)
    API_HASH = config("7fb84143bb5f12156dc1835355d4e70e", None)
    TOKEN = config("5696580119:AAF0fIrLges-k7zXj_5PgVoCSX01wVjfktw", None)
    OWNER_ID = list(map(int, getenv("5363436020").split()))
