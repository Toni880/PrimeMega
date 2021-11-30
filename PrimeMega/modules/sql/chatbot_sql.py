import threading

from sqlalchemy import Column, String
from PrimeMega.modules.sql import BASE, SESSION

class PrimeChats(BASE):
    __tablename__ = "prime_chats"
    chat_id = Column(String(14), primary_key=True)

    def __init__(self, chat_id):
        self.chat_id = chat_id

PrimeChats.__table__.create(checkfirst=True)
INSERTION_LOCK = threading.RLock()


def is_prime(chat_id):
    try:
        chat = SESSION.query(PrimeChats).get(str(chat_id))
        return bool(chat)
    finally:
        SESSION.close()

def set_prime(chat_id):
    with INSERTION_LOCK:
        primechat = SESSION.query(PrimeChats).get(str(chat_id))
        if not primechat:
            primechat = PrimeChats(str(chat_id))
        SESSION.add(primechat)
        SESSION.commit()

def rem_prime(chat_id):
    with INSERTION_LOCK:
        primechat = SESSION.query(PrimeChats).get(str(chat_id))
        if primechat:
            SESSION.delete(primechat)
        SESSION.commit()


def get_all_prime_chats():
    try:
        return SESSION.query(PrimeChats.chat_id).all()
    finally:
        SESSION.close()
