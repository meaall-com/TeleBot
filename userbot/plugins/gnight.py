# 
# Kangers keep credits 😐
from userbot.utils import register

@register(outgoing=True, pattern="^.night$")

async def join(e):

    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):

        await e.edit("ا")
