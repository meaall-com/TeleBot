"""قم بتمكين Seen Counter في أي رسالة لمعرفة عدد المستخدمين الذين شاهدوا رسالتك
Syntax: .fwd كرد على أي رسالة"""

from telethon import events
from telethon import sync
from telethon.tl import types, functions
from userbot.utils import admin_cmd

@borg.on(admin_cmd(pattern="frwd"))
async def _(event):
    if event.fwd_from:
        return
    if Config.CHANNEL_ID is None:
        await event.edit("يرجى تعيين متغير البيئة المطلوب `CHANNEL_ID` for this plugin to work")
        return
    try:
        e = await borg.get_entity(Config.CHANNEL_ID)
    except Exception as e:
        await event.edit(str(e))
    else:
        re_message = await event.get_reply_message()
        # 
        fwd_message = await borg.forward_messages(
            e,
            re_message,
            silent=True
        )
        await borg.forward_messages(
            event.chat_id,
            fwd_message
        )
        await fwd_message.delete()
        await event.delete()
