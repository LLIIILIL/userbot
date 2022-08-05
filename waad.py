import telethon
from telethon import events
from time import sleep
from config import *
import asyncio
from help import *


@sedthon.on(events.NewMessage(outgoing=True, pattern=r"\.وعد"))
async def _(event):
    await event.edit(waad)


@sedthon.on(events.NewMessage(outgoing=True, pattern=r"\.كلمات وعد (.*)"))
async def _(event):
    for i in range(int("".join(event.text.split(maxsplit=2)[2:]).split(" ", 2)[0])):
        chat = event.chat_id
        await sedthon.send_message(chat, 'كلمات')
        await asyncio.sleep(0.5)
        masg = await sedthon.get_messages(chat, limit=1)
        masg = masg[0].message
        masg = ("".join(masg.split(maxsplit=3)[3:])).split(" ", 2)
        if len(masg) == 2:
            msg = masg[0]
            await sedthon.send_message(chat, msg)
        else:
            msg = masg[0] + " " + masg[1]
            await sedthon.send_message(chat, msg)
# ↢ ()


@sedthon.on(events.NewMessage(outgoing=True, pattern=r"\.استثمار وعد (.*)"))
async def _(event):
    for i in range(int("".join(event.text.split(maxsplit=2)[2:]).split(" ", 2)[0])):
        chat = event.chat_id
        await sedthon.send_message(chat, 'فلوسي')
        await asyncio.sleep(0.5)
        masg = await sedthon.get_messages(chat, limit=1)
        masg = masg[0].message
        masg = ("".join(masg.split(maxsplit=2)[2:])).split(" ", 2)
        msg = masg[0]
        if int(msg) > 500000000:
            await sedthon.send_message(chat, f"استثمار {msg}")
            await asyncio.sleep(0.5)
            mssag2 = sedthon.get_messages(chat, limit=1)
            await mssag2[0].click(text="اي")
        else:
            await sedthon.send_message(chat, f"استثمار {msg}")
        await asyncio.sleep(5)
