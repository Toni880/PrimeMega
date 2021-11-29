import os
import re
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from PrimeMega.events import register
from PrimeMega import telethn as tbot


PHOTO = "https://telegra.ph/file/efc27dec817626cc95016.jpg"

@register(pattern=("/alive"))
async def awake(event):
  PRIME = f"**Hi [{event.sender.first_name}](tg://user?id={event.sender.id}), I'm Prime Mega.** \n\n"
  PRIME += "⚪ **I'm Working Properly** \n\n"
  PRIME += f"⚪ **My Master : [Lord](https://t.me/Bukan_guudlooking)** \n\n"
  PRIME += f"⚪ **Library Version :** `{telever}` \n\n"
  PRIME += f"⚪ **Telethon Version :** `{tlhver}` \n\n"
  PRIME += f"⚪ **Pyrogram Version :** `{pyrover}` \n\n"
  PRIME += "**Thanks For Adding Me Here ❤️**"
  BUTTON = [[Button.url("ʜᴇʟᴘ​", "https://t.me/PrimeMegaBot?start=help"), Button.url("sᴜᴘᴘᴏʀᴛ​", "https://t.me/PrimeSupportGroup")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=PRIME,  buttons=BUTTON)
