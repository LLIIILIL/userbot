import telethon
from telethon import events
from time import sleep
from config import *
import asyncio
from help import *


@sedthon.on(events.NewMessage(outgoing=True, pattern=r"\.تولين"))
async def _(event):
    await event.edit(toolen)


@sedthon.on(events.NewMessage(outgoing=True, pattern=r"\.استثمار تولين (.*)"))
async def _(event):
    for i in range(int("".join(event.text.split(maxsplit=2)[2:]).split(" ", 2)[0])):
        chat = event.chat_id
        await sedthon.send_message(chat, 'فلوسي')
        await asyncio.sleep(0.5)
        msg = await sedthon.get_messages(chat, limit=1)[0].message
        # masg = masg[0].message
        msg = ("".join(msg.split(maxsplit=2)[2:])).split(" ", 2)[0]
        #msg = masg[0]
        await sedthon.send_message(chat, f"استثمار {msg}")
        await asyncio.sleep(5)
