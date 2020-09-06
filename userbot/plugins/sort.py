#python 3.7.1

import time
import os,sys
"""الأوامر المتوفرة:
.support"""

from telethon import events

import asyncio

from userbot.utils import admin_cmd

@borg.on(admin_cmd("(.*)"))

async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.3
    animation_ttl = range(0, 5)
    input_str = event.pattern_match.group(1)
    if input_str == "support":
        await event.edit(input_str)
        animation_chars = ["مرحبا,",
            "اررررحب يا سيدي",
            "انضم لا جروبنا" ,
            "[اشترك هنا](t.me/meaallh100)",
            "[المساعدة](t.me/meaallh100)"
          ]

        for i in animation_ttl:
        	
            await asyncio.sleep(animation_interval)
            await event.edit(animation_chars[i %5 ])