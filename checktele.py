from concurrent.futures import thread
import random
import asyncio
import telethon
from telethon.tl import functions, types
from telethon import events
import requests
from telethon.sync import functions, types
from user_agent import generate_user_agent
import requests
from user_agent import *
from help import *
from config import *
from telethon.tl.functions.messages import DeleteMessagesRequest
from threading import Thread
a = 'qwertyuiopassdfghjklzxcvbnm'
b = '1234567890'
e = 'qwertyuiopassdfghjklzxcvbnm1234567890'

banned = []
isclaim = ["off"]
isauto = ["off"]
with open("banned.txt", "r") as f:
    f = f.read().split()
    banned.append(f)


class thv(Thread):
    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs={}, Verbose=None):
        Thread.__init__(self, group, target, name, args, kwargs, Verbose)
        self._return = None

    def run(self):
        if self._Thread__target is not None:
            self._return = self._Thread__target(*self._Thread__args,
                                                **self._Thread__kwargs)

    def join(self):
        Thread.join(self)
        return self._return


def check_user(username):
    url = "https://t.me/"+str(username)
    headers = {
        "User-Agent": generate_user_agent(),
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7"}

    response = requests.get(url, headers=headers)
    if response.text.find('If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"') >= 0:
        return "Available"
    else:
        return "Unavailable"


@sedthon.on(events.NewMessage(outgoing=True, pattern=r"\.تشيكر تلي"))
async def _(event):
    await event.edit(tele_checker)


@sedthon.on(events.NewMessage(outgoing=True, pattern=r"\.اليوزرات المبندة"))
async def _(event):
    await sedthon.send_file(event.chat_id, 'banned.txt')


@sedthon.on(events.NewMessage(outgoing=True, pattern=r"\.الانواع"))
async def _(event):
    await event.edit(tele_checker2)

# كلايم عدد نوع قناة


@sedthon.on(events.NewMessage(outgoing=True, pattern=r"\.كلايم (.*)"))
async def _(event):
    isclaim.clear()
    isclaim.append("on")
    msg = ("".join(event.text.split(maxsplit=1)[1:])).split(" ", 2)
    ch = str(msg[2])
    choice = str(msg[1])
    trys = 0
    await event.edit(f"حسناً سأفحص نوع `{choice}` من اليوزرات على `{ch}` , بعدد `{msg[0]}` من المحاولات !")

    @sedthon.on(events.NewMessage(outgoing=True, pattern=r"\.حالة الكلايم"))
    async def _(event):
        if "on" in isclaim:
            await event.edit(f"الكلايم وصل لـ({trys}) من المحاولات")
        elif "off" in isclaim:
            await event.edit("لايوجد كلايم شغال !")
        else:
            await event.edit("خطأ")
    for i in range(int(msg[0])):
        username = ""
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
        if choice == "6":
            c = d = random.choices(a)
            d = random.choices(b)
            f = [c[0], c[0], c[0], c[0], d[0]]
            random.shuffle(f)
            username = ''.join(f)
            if username in banned[0]:
                c = d = random.choices(a)
                d = random.choices(b)
                f = [c[0], c[0], c[0], c[0], d[0]]
                random.shuffle(f)
                username = ''.join(f)
        if choice == "7":
            c = d = random.choices(a)
            d = random.choices(b)
            f = [c[0], c[0], c[0], c[0], d[0], c[0], c[0]]
            random.shuffle(f)
            username = ''.join(f)
            if username in banned[0]:
                c = d = random.choices(a)
                d = random.choices(b)
                f = [c[0], c[0], c[0], c[0], d[0]]
                random.shuffle(f)
                username = ''.join(f)
        isavv = thv(target=check_user, args=username)
        isavv.start()
        isav = isavv.join()
        if "Available" in isav:
            await asyncio.sleep(0.5)
            try:
                await sedthon(functions.channels.UpdateUsernameRequest(
                    channel=ch, username=username))
                await event.client.send_message(event.chat_id, f'''
تم صيد (@{username}) !
سـيـدثـون : @Sedthon
''')
                break
            except telethon.errors.rpcerrorlist.UsernameInvalidError:
                with open("banned.txt", "a") as f:
                    f.write(f"\n{username}")
            except:
                await event.client.send_message(event.chat_id, f"خطأ مع `{username}`")
                break
        else:
            pass
        trys += 1

    isclaim.clear()
    isclaim.append("off")
    trys = ""
    await event.client.send_message(event.chat_id, "تم الانتهاء من الفحص")


@sedthon.on(events.NewMessage(outgoing=True, pattern=r"\.تثبيت (.*)"))
async def _(event):
    trys = 0
    msg = ("".join(event.text.split(maxsplit=1)[1:])).split(" ", 1)
    if msg[0] == "تلقائي":  # تثبيت تلقائي عدد يوزر قناة
        isauto.clear()
        isauto.append("on")
        msg = ("".join(event.text.split(maxsplit=2)[2:])).split(" ", 2)
        username = str(msg[2])
        ch = str(msg[1])
        await event.edit(f"حسناً سأحاول تثبيت `{username}` على `{ch}` , بعدد `{msg[0]}` من المحاولات !")

        @sedthon.on(events.NewMessage(outgoing=True, pattern=r"\.حالة التثبيت التلقائي"))
        async def _(event):
            if "on" in isauto:
                msg = await event.edit(f"التثبيت وصل لـ({trys}) من المحاولات")
                await asyncio.sleep(2)
                try:
                    await event.delete()
                except:
                    pass
            elif "off" in isauto:
                await event.edit("لايوجد تثبيت شغال !")
            else:
                await event.edit("خطأ")
        for i in range(int(msg[0])):
            isav = Thread(target=check_user(username))
            if "Available" in isav:
                try:
                    await sedthon(functions.channels.UpdateUsernameRequest(
                        channel=ch, username=username))
                    await event.client.send_message(event.chat_id, f'''
تم صيد (@{username}) !
سـيـدثـون : @Sedthon
''')
                    break
                except telethon.errors.rpcerrorlist.UsernameInvalidError:
                    await event.client.send_message(event.chat_id, f"مبند `{username}` ❌❌")
                    break
                except:
                    await event.client.send_message(event.chat_id, f"خطأ مع `{username}`")
                    break
            else:
                pass
            trys += 1

            await asyncio.sleep(2)
        trys = ""
        isclaim.clear()
        isclaim.append("off")
        await sedthon.send_message(event.chat_id, "تم الانتهاء من التثبيت التلقائي")
    if msg[0] == "يدوي":  # تثبيت يدوي يوزر قناة
        msg = ("".join(event.text.split(maxsplit=1)[1:])).split(" ", 1)
        username = str(msg[1])
        ch = str(msg[2])
        try:
            await sedthon(functions.channels.UpdateUsernameRequest(
                channel=ch, username=username))
            await event.client.send_message(event.chat_id, f'''
تم صيد (@{username}) !
سـيـدثـون : @Sedthon
''')
        except telethon.errors.rpcerrorlist.UsernameInvalidError:
            await event.client.send_message(event.chat_id, f"مبند `{username}` ❌❌")
        except:
            await event.client.send_message(event.chat_id, "خطأ")
