from userbot.utils import register

@register(outgoing=True, pattern="^.group$")

async def join(e):

    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):

        await e.edit("This is my community.\n\n[Channel](http://t.me/meaallh100)\n\n[Chat Group](https://t.me/)\n\n[UserBot Tutorial - TeleBot](https://t.me/)\n\n[TeleBot Chat]()\n\n[YouTube]()")
