import os
from telethon import TelegramClient, events

api_id = int(os.environ.get("APP_ID", "10897780"))
api_hash = os.environ.get("API_HASH", "7fb84143bb5f12156dc1835355d4e70e")
bot_token = os.environ.get("TOKEN", "5696580119:AAF0fIrLges-k7zXj_5PgVoCSX01wVjfktw")
