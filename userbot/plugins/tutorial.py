"""البرنامج المساعد للحصول على فيديو تعليمي لنشر meaallh
.tut"""

from userbot.utils import register

@register(outgoing=True, pattern="^.tut$")

async def join(e):

    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):

        await e.edit("مابش!!")
