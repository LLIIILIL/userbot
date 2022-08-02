from telethon.sync import TelegramClient
from telethon.sessions import StringSession
import os
import heroku3
APP_ID = 18922496
APP_HASH = "371d1dc33eccaa19bb0814a27bb98f3c"
session = '''1ApWapzMBu14nXzvAY0-SEK5GjUI8XIQLiEmQx3lIAfOjpiuzMBLeoJfTsUprfUg6WkvqhYZftYCbFodovh4NsmJbv-F0qDinr92sJjipRbd9YnmIMMOypyIhdFRUB1DnOFf_kHlqiwV3dLSjXLnAr2d25_3DqW95Uwd1TLV-ysnGFjNCzAI-7HhtiHZ5B35EDFEo7SGpWu60PHEfrcqRfR66VjZHG57kk8wgcEaMcRKML9szDiCfvr1A6a1fXlNQ-kAzfvOjDRohRRJjeQaQa5pruqFi6OmNMMUnC4EWPa8tbsEdnXP36yiTqbi5tiI_cT4b74yUyJYzHu6c6lq0y3hThTXW-9c='''
sedthon = TelegramClient(StringSession(session), APP_ID, APP_HASH)
sedthon.start()
HEROKU_APP_NAME = os.environ.get("Heroku app name")
HEROKU_API_KEY = os.environ.get("Heroku app key")
Heroku = heroku3.from_key(HEROKU_API_KEY)
