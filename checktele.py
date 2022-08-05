import os
import random
import asyncio
import time
from telethon.tl import functions, types
from telethon import events
import requests
from telethon.sync import functions, types
import user_agent
from user_agent import generate_user_agent
import requests
from user_agent import *
from config import *
from help import *
abc = 'qwertyuiopasdfghjklzxcvbnm'
abc2 = 'qwertyuiopasdfghjklzxcvbnm1234567890'


@sedthon.on(events.NewMessage(outgoing=True, pattern=r"\.تشيكر تلي"))
async def _(event):
    await event.edit(tele_checker)

'''
# كلايم عدد نوع قناة
@sedthon.on(events.NewMessage(outgoing=True, pattern=".كلايم (.*)"))
async def _(event):
    msg = ("".join(event.text.split(maxsplit=1)[1:])).split(" ", 2)
    for i in range(int(msg[0])):
        l1 = str(''.join(random.choice(abc)))
        l2 = str(''.join(random.choice(abc)))
        l3 = str(''.join(random.choice(abc)))
        n1 = str(''.join(random.choice(abc2)))
        n2 = str(''.join(random.choice(abc2)))
        username = ""
        ch = str(msg[2])
        choice = str(msg[1])
        if choice == "1":
            username = l1+n1+n1+l1+l1+l1

        if choice == "2":
            username = l1+'_'+n1+'_'+n2

        if choice == "3":
            username = l1+n1+l1+n1+l1+n1

        if choice == "4":
            username = l1+n1+n2+"BOT"

        url = "https://t.me/"+str(username)
        headers = {
            "User-Agent": generate_user_agent(),
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7"}
        response = requests.get(url, headers=headers)
        if response.text.find('If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"') >= 0:
            await event.client.send_message(event.chat_id, f"Good {username} ✔️")
            time.sleep(0.5)
            try:
                await sedthon(functions.channels.UpdateUsernameRequest(
                    channel=ch, username=username))
                await event.client.send_message(event.chat_id, f"Taked {username} ✔️✔️")
            except:
                await event.client.send_message(event.chat_id, f"Banned {username} ❌❌")
        else:
            await event.edit(f"Bad {username} ❌")
            time.sleep(0.3)
    await event.edit("تم الانتهاء من الفحص")
'''

# تثبيت يوزر قناة


@sedthon.on(events.NewMessage(outgoing=True, pattern=".تثبيت (.*)"))
async def _(event):
    msg = ("".join(event.text.split(maxsplit=1)[1:])).split(" ", 1)
    username = str(msg[0])
    ch = str(msg[1])
    try:
        await sedthon(functions.channels.UpdateUsernameRequest(
            channel=ch, username=username))
        await event.client.send_message(event.chat_id, f"Taked {username} ✔️✔️")
    except:
        await event.client.send_message(event.chat_id, f"Banned {username} ❌❌")
