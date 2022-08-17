import os
import random
import asyncio
import time
import telethon
from telethon.tl import functions, types
from telethon import events
import requests
from telethon.sync import functions, types
import user_agent
from user_agent import generate_user_agent
import requests
from user_agent import *
from help import *
from config import *

a = 'qwertyuiopassdfghjklzxcvbnm'
b = '1234567890'
e = 'qwertyuiopassdfghjklzxcvbnm1234567890'
banned = []
with open("banned.txt", "r") as f:
    f = f.read().split()
    banned.append(f)


@sedthon.on(events.NewMessage(outgoing=True, pattern=r"\.تشيكر تلي"))
async def _(event):
    await event.edit(tele_checker)


@sedthon.on(events.NewMessage(outgoing=True, pattern=r"\.اليوزرات المبندة"))
async def _(event):
    await sedthon.send_file(event.chat_id, 'banned.txt')

# كلايم عدد نوع قناة


@sedthon.on(events.NewMessage(outgoing=True, pattern=r"\.كلايم (.*)"))
async def _(event):
    msg = ("".join(event.text.split(maxsplit=1)[1:])).split(" ", 2)
    await event.edit("حسنا")
    for i in range(int(msg[0])):
        await asyncio.sleep(0.3)
        username = ""
        ch = str(msg[2])
        choice = str(msg[1])
        if choice == "1":
            c = d = random.choices(a)
            d = random.choices(b)
            f = [c[0], d[0], c[0], c[0], c[0], d[0]]
            random.shuffle(f)
            username = ''.join(f)
            if username in banned[0]:
                c = d = random.choices(a)
                d = random.choices(b)
                f = [c[0], d[0], c[0], c[0], c[0], d[0]]
                random.shuffle(f)
                username = ''.join(f)
            else:
                pass
        if choice == "2":
            c = random.choices(a)
            d = random.choices(b)
            s = random.choices(e)
            f = [c[0], "_", d[0], "_", s[0]]
            username = ''.join(f)
            if username in banned[0]:
                c = random.choices(a)
                d = random.choices(b)
                s = random.choices(e)
                f = [c[0], "_", d[0], "_", s[0]]
                username = ''.join(f)
            else:
                pass
        if choice == "3":
            c = d = random.choices(a)
            d = random.choices(b)
            f = [c[0], c[0], c[0], c[0], c[0], d[0]]
            random.shuffle(f)
            username = ''.join(f)
            if username in banned[0]:
                c = d = random.choices(a)
                d = random.choices(b)
                f = [c[0], c[0], c[0], c[0], c[0], d[0]]
                random.shuffle(f)
                username = ''.join(f)
            else:
                pass
        if choice == "4":
            c = random.choices(a)
            d = random.choices(b)
            s = random.choices(e)
            f = [c[0], s[0], d[0]]
            random.shuffle(f)
            username = ''.join(f)
            username = username+'bot'
            if username in banned[0]:
                c = random.choices(a)
                d = random.choices(b)
                s = random.choices(e)
                f = [c[0], s[0], d[0]]
                random.shuffle(f)
                username = ''.join(f)
                username = username+'bot'
            else:
                pass
        if choice == "5":
            c = d = random.choices(a)
            d = random.choices(b)
            f = [c[0], d[0], c[0], c[0], d[0]]
            random.shuffle(f)
            username = ''.join(f)
            if username in banned[0]:
                c = d = random.choices(a)
                d = random.choices(b)
                f = [c[0], d[0], c[0], c[0], c[0], d[0]]
                random.shuffle(f)
                username = ''.join(f)
            else:
                pass
        url = "https://t.me/"+str(username)
        headers = {
            "User-Agent": generate_user_agent(),
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7"}

        response = requests.get(url, headers=headers)
        if response.text.find('If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"') >= 0:
            await event.client.send_message(event.chat_id, f"Good {username} ✔️")

            try:
                await sedthon(functions.channels.UpdateUsernameRequest(
                    channel=ch, username=username))
                await event.client.send_message(event.chat_id, f"Taked {username} ✔️✔️")
            except telethon.errors.rpcerrorlist.UsernameInvalidError:
                await event.client.send_message(event.chat_id, f"Banned {username} ❌❌")
                with open("banned.txt", "a") as f:
                    f.write(f"\n{username}")
            except:
                await event.client.send_message(event.chat_id, "Error")
                break
        else:
            pass
    await event.client.send_message(event.chat_id, "تم الانتهاء من الفحص")

# تثبيت يوزر قناة


@sedthon.on(events.NewMessage(outgoing=True, pattern=r"\.تثبيت (.*)"))
async def _(event):
    msg = ("".join(event.text.split(maxsplit=1)[1:])).split(" ", 0)
    if msg[0] == "تلقائي":
        import os

a = 'qwertyuiopassdfghjklzxcvbnm'
b = '1234567890'
e = 'qwertyuiopassdfghjklzxcvbnm1234567890'
banned = []
with open("banned.txt", "r") as f:
    f = f.read().split()
    banned.append(f)


@sedthon.on(events.NewMessage(outgoing=True, pattern=r"\.تشيكر تلي"))
async def _(event):
    await event.edit(tele_checker)


@sedthon.on(events.NewMessage(outgoing=True, pattern=r"\.اليوزرات المبندة"))
async def _(event):
    await sedthon.send_file(event.chat_id, 'banned.txt')

# كلايم عدد نوع قناة


@sedthon.on(events.NewMessage(outgoing=True, pattern=r"\.كلايم (.*)"))
async def _(event):
    msg = ("".join(event.text.split(maxsplit=1)[1:])).split(" ", 2)
    await event.edit("حسنا")
    for i in range(int(msg[0])):
        await asyncio.sleep(0.3)
        username = ""
        ch = str(msg[2])
        choice = str(msg[1])
        if choice == "1":
            c = d = random.choices(a)
            d = random.choices(b)
            f = [c[0], d[0], c[0], c[0], c[0], d[0]]
            random.shuffle(f)
            username = ''.join(f)
            if username in banned[0]:
                c = d = random.choices(a)
                d = random.choices(b)
                f = [c[0], d[0], c[0], c[0], c[0], d[0]]
                random.shuffle(f)
                username = ''.join(f)
            else:
                pass
        if choice == "2":
            c = random.choices(a)
            d = random.choices(b)
            s = random.choices(e)
            f = [c[0], "_", d[0], "_", s[0]]
            username = ''.join(f)
            if username in banned[0]:
                c = random.choices(a)
                d = random.choices(b)
                s = random.choices(e)
                f = [c[0], "_", d[0], "_", s[0]]
                username = ''.join(f)
            else:
                pass
        if choice == "3":
            c = d = random.choices(a)
            d = random.choices(b)
            f = [c[0], c[0], c[0], c[0], c[0], d[0]]
            random.shuffle(f)
            username = ''.join(f)
            if username in banned[0]:
                c = d = random.choices(a)
                d = random.choices(b)
                f = [c[0], c[0], c[0], c[0], c[0], d[0]]
                random.shuffle(f)
                username = ''.join(f)
            else:
                pass
        if choice == "4":
            c = random.choices(a)
            d = random.choices(b)
            s = random.choices(e)
            f = [c[0], s[0], d[0]]
            random.shuffle(f)
            username = ''.join(f)
            username = username+'bot'
            if username in banned[0]:
                c = random.choices(a)
                d = random.choices(b)
                s = random.choices(e)
                f = [c[0], s[0], d[0]]
                random.shuffle(f)
                username = ''.join(f)
                username = username+'bot'
            else:
                pass
        if choice == "5":
            c = d = random.choices(a)
            d = random.choices(b)
            f = [c[0], d[0], c[0], c[0], d[0]]
            random.shuffle(f)
            username = ''.join(f)
            if username in banned[0]:
                c = d = random.choices(a)
                d = random.choices(b)
                f = [c[0], d[0], c[0], c[0], c[0], d[0]]
                random.shuffle(f)
                username = ''.join(f)
            else:
                pass
        url = "https://t.me/"+str(username)
        headers = {
            "User-Agent": generate_user_agent(),
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7"}

        response = requests.get(url, headers=headers)
        if response.text.find('If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"') >= 0:
            await event.client.send_message(event.chat_id, f"Good {username} ✔️")

            try:
                await sedthon(functions.channels.UpdateUsernameRequest(
                    channel=ch, username=username))
                await event.client.send_message(event.chat_id, f"Taked {username} ✔️✔️")
            except telethon.errors.rpcerrorlist.UsernameInvalidError:
                await event.client.send_message(event.chat_id, f"Banned {username} ❌❌")
                with open("banned.txt", "a") as f:
                    f.write(f"\n{username}")
            except:
                await event.client.send_message(event.chat_id, "Error")
                break
        else:
            pass
    await event.client.send_message(event.chat_id, "تم الانتهاء من الفحص")


@sedthon.on(events.NewMessage(outgoing=True, pattern=r"\.تثبيت (.*)"))
async def _(event):
    msg = ("".join(event.text.split(maxsplit=1)[1:])).split(" ", 1)
    if msg[0] == "تلقائي":  # تثبيت تلقائي عدد يوزر قناة
        await event.edit("حسناً")
        msg = ("".join(event.text.split(maxsplit=2)[2:])).split(" ", 2)
        username = str(msg[1])
        ch = str(msg[2])
        for i in range(int(msg[0])):
            try:
                await sedthon(functions.channels.UpdateUsernameRequest(
                    channel=ch, username=username))
                await event.client.send_message(event.chat_id, f"Taked {username} ✔️✔️")
                break
            except:
                pass
            await asyncio.sleep(5)
        await sedthon.send_message(event.chat_id, "تم الانتهاء من التثبيت التلقائي")
    else:  # تثبيت يوزر قناة
        msg = ("".join(event.text.split(maxsplit=1)[1:])).split(" ", 1)
        username = str(msg[0])
        ch = str(msg[1])
        try:
            await sedthon(functions.channels.UpdateUsernameRequest(
                channel=ch, username=username))
            await event.client.send_message(event.chat_id, f"Taked {username} ✔️✔️")
        except:
            await event.client.send_message(event.chat_id, f"Banned {username} ❌❌")
