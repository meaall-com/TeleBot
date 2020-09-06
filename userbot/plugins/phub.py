"""Emoji

Available Commands:

.emoji shrug

.emoji apple

.emoji :/

.emoji -_-"""

from telethon import events

import asyncio





@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.5

    animation_ttl = range(0, 101)

    input_str = event.pattern_match.group(1)

    if input_str == "مع الله":

        await event.edit(input_str)

        animation_chars = [

            "م_",

            "مع_",

            "مع _",

            "مع ا_",
            
            "مع ال_",
            
            "مع الل_",
            
           "مع اللـ_", 
           
           "مع اللـه",

        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 10])


@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.5

    animation_ttl = range(0, 101)

    input_str = event.pattern_match.group(1)

    if input_str == "قوة القوة":

        await event.edit(input_str)

        animation_chars = [

            "قو_",

            "قوو_",

            "قووة_",

            "قووة ا_",
            
            "قووة الق_",
            
            "قووة القوة_",
            
            "قووة القوة💪",

        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 10])



"""Emoji

Available Commands:

.emoji shrug

.emoji apple

.emoji :/

.emoji -_-"""





@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.5

    animation_ttl = range(0, 101)

    input_str = event.pattern_match.group(1)

    if input_str == "ضخم":

        await event.edit(input_str)

        animation_chars = [

            "_",

            "ض_",

            "ضخ_",

            "ضخم_",
            
            "ضخم⁦✔️⁩_",
            
            "ضخم⁦✔️⁩",
            
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 10])
