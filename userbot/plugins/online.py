# Copyright TeleBot
# For @TeleBotHelp coded by @xditya
# Kangers keep credits else I'll take down 🧐

import sys
from telethon import events, functions, version, __version__
import random
from userbot.utils import register
from userbot import ALIVE_NAME

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "No name set yet, check pinned in @TeleBotHelp"

ONLINESTR = [
	"هممممم",
	f"t.me/meaallh109"
]

@register(outgoing=True, pattern="^.online$")
async def online(event):
    """ Greet everyone! """
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(random.choice(ONLINESTR))
