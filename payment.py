from config import *
from telethon import events
from help import *

@sedthon.on(events.NewMessage(outgoing=True))
async def _(event):
    id = str(event.sender_id)
    idas = await sedthon.get_messages("sedupay", limit=1)
    msg = str(idas[0].message)
    if id in msg and ispay[0] == 'no':
        ispay.clear()
        ispay.append("yes")
    elif id not in msg and ispay[0] == 'yes':
        ispay.clear()
        ispay.append("no")
    else:
        pass
