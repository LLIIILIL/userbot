from telethon.sync import TelegramClient
from telethon.sessions import StringSession
import os
import heroku3
APP_ID = os.environ.get("APP_ID")
APP_HASH = os.environ.get("APP_HASH")
session = os.environ.get("TERMUX")
sedthon = TelegramClient(StringSession(session), APP_ID, APP_HASH)
sedthon.start()
HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME")
HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY")
Heroku = heroku3.from_key(HEROKU_API_KEY)
