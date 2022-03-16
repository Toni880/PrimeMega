import os
import re
from platform import python_version as kontol
from telegram import (
  __version__ as telever,
  InlineKeyboardButton,
)
from telethon import (
  events,
  Button,
  __version__ as tlhver,
)
from pyrogram import __version__ as pyrover
from PrimeMega.events import register
from PrimeMega import (
  BOT_NAME,
  BOT_USERNAME,
  OWNER_USERNAME,
  PHOTO,
  SUPPORT_CHAT,
  telethn as tbot,
)


@register(pattern=("/alive"))
async def awake(event):
  PRIME = f"**Hi [{event.sender.first_name}](tg://user?id={event.sender.id}), I'm {BOT_NAME}.** \n\n"
  PRIME += "⚪ **I'm Working Properly** \n\n"
  PRIME += f"⚪ **My Master : [Lord](https://t.me/{OWNER_USERNAME})** \n\n"
  PRIME += f"⚪ **Library Version :** `{telever}` \n\n"
  PRIME += f"⚪ **Telethon Version :** `{tlhver}` \n\n"
  PRIME += f"⚪ **Pyrogram Version :** `{pyrover}` \n\n"
  PRIME += "**Thanks For Adding Me Here ❤️**"
  BUTTON = [
    [
      InlineKeyboardButton(text="Help", url=f"https://t.me/{BOT_USERNAME}start=help"),
      InlineKeyboardButton(text="Support", url=f"https://t.me/{SUPPORT_CHAT}"),
    ]
  ]
  await tbot.send_file(event.chat_id, PHOTO, caption=PRIME,  buttons=BUTTON)
