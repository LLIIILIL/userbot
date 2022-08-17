import threading
from telethon import events
from sqlalchemy import Column, PickleType, UnicodeText, distinct, func
from sqlalchemy.ext.declarative import declarative_base
import logging
from asyncio import CancelledError
from config import *
from sqltable import *
BASE = declarative_base()


class Cat_GlobalCollection(BASE):
    __tablename__ = "sed_globalcollection"
    keywoard = Column(UnicodeText, primary_key=True)
    contents = Column(PickleType, primary_key=True, nullable=False)

    def __init__(self, keywoard, contents):
        self.keywoard = keywoard
        self.contents = tuple(contents)

    def __repr__(self):
        return "<Cat Global Collection lists '%s' for %s>" % (
            self.contents,
            self.keywoard,
        )

    def __eq__(self, other):
        return (
            isinstance(other, Cat_GlobalCollection)
            and self.keywoard == other.keywoard
            and self.contents == other.contents
        )


Cat_GlobalCollection.__table__.create(checkfirst=True)

CAT_GLOBALCOLLECTION = threading.RLock()


class COLLECTION_SQL:
    def __init__(self):
        self.CONTENTS_LIST = {}


COLLECTION_SQL_ = COLLECTION_SQL()


def add_to_collectionlist(keywoard, contents):
    with CAT_GLOBALCOLLECTION:
        keyword_items = Cat_GlobalCollection(keywoard, tuple(contents))

        SESSION.merge(keyword_items)
        SESSION.commit()
        COLLECTION_SQL_.CONTENTS_LIST.setdefault(
            keywoard, set()).add(tuple(contents))


def get_collectionlist_items():
    try:
        chats = SESSION.query(Cat_GlobalCollection.keywoard).distinct().all()
        return [i[0] for i in chats]
    finally:
        SESSION.close()


def del_keyword_collectionlist(keywoard):
    with CAT_GLOBALCOLLECTION:
        keyword_items = (
            SESSION.query(Cat_GlobalCollection.keywoard)
            .filter(Cat_GlobalCollection.keywoard == keywoard)
            .delete()
        )
        COLLECTION_SQL_.CONTENTS_LIST.pop(keywoard)
        SESSION.commit()


logger = logging.basicConfig(
    format="[%(levelname)s- %(asctime)s]- %(name)s- %(message)s",
    level=logging.INFO,
    datefmt="%H:%M:%S",
)

LOGS = logger.getLogger(__name__)


@sedthon.on(events.NewMessage(outgoing=True, pattern=r"\.اعادة تشغيل"))
async def _(event):
    "Restarts the bot !!"
    sandy = await event.edit(
        "سيتم اعادة تشغيل السورس - انتضر 1-2 دقائق"
    )
    try:
        ulist = get_collectionlist_items()
        for i in ulist:
            if i == "restart_update":
                del_keyword_collectionlist("restart_update")
    except Exception as e:
        LOGS.error(e)
    try:
        add_to_collectionlist("restart_update", [sandy.chat_id, sandy.id])
    except Exception as e:
        LOGS.error(e)
    try:
        await sedthon.disconnect()
    except CancelledError:
        pass
    except Exception as e:
        LOGS.error(e)
