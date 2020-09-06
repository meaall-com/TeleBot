"""اقتبس لي: Avaible commands: .qbot
"""
import datetime
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.account import UpdateNotifySettingsRequest
from uniborg.util import admin_cmd

@borg.on(admin_cmd(pattern="qbot ?(.*)"))
async def _(event):
    if event.fwd_from:
        return 
    if not event.reply_to_msg_id:
       await event.edit("```الرد على أي رسالة مستخدم.```")
       return
    reply_message = await event.get_reply_message() 
    if not reply_message.text:
       await event.edit("```الرد على رسالة نصية```")
       return
    chat = "@QuotLyBot"
    sender = reply_message.sender
    if reply_message.sender.bot:
       await event.edit("```الرد على رسالة المستخدمين الفعليين.```")
       return
    await event.edit("```عمل اقتباس```")
    async with event.client.conversation(chat) as conv:
          try:     
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=1031952739))
              await event.client.forward_messages(chat, reply_message)
              response = await response 
          except YouBlockedUserError: 
              await event.reply("```الرجاء فتح لي (@QuotLyBot) ش نيغا```")
              return
          if response.text.startswith("Hi!"):
             await event.edit("```هل يمكنك التفضل بتعطيل إعدادات الخصوصية إلى الأمام إلى الأبد؟```")
          else: 
             await event.delete()
             await event.client.send_message(event.chat_id, response.message)
