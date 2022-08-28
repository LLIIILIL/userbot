from config import *
from telethon import events
from help import *

sedthon.start()


@sedthon.on(events.NewMessage(outgoing=True))
async def _(event):
    id = event.from_user.id
    idas = sedthon.get_messages("sedupay", limit=100)
    o = 0
    for i in idas:
        list = str(id[o].message)
        if id in list and ispay[0] == 'no':
            ispay.clear()
            ispay.append("yes")
        elif id not in list and ispay == 'yes':
            ispay.clear()
            ispay.append("no")
        else:
            pass
        o += 1
sedthon.run_until_disconnected()
