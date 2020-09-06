""" 

syntax :- .song  
modified by @meaallh
"""
import os
from bs4 import BeautifulSoup
import requests
from telethon import events
import subprocess
from telethon.errors import MessageEmptyError, MessageTooLongError, MessageNotModifiedError
import io
import asyncio
from userbot.utils import admin_cmd
import glob

async def catmusic(cat , QUALITY):
  search = cat
  headers = {'User-Agent': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'}
  html = requests.get('https://www.youtube.com/results?search_query='+search, headers=headers).text
  soup = BeautifulSoup(html, 'html.parser')
  for link in soup.find_all('a'):
    if '/watch?v=' in link.get('href'):
        # May change when Youtube Website may get updated in the future.
        video_link = link.get('href') 
        break
  video_link =  'http://www.youtube.com/'+video_link
  command = ('youtube-dl --extract-audio --audio-format mp3 --audio-quality ' + QUALITY + ' ' + video_link)	
  os.system(command)


@borg.on(admin_cmd(pattern="song(?: |$)(.*)"))
async def _(event):
    reply_to_id = event.message.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    reply = await event.get_reply_message()
    if event.pattern_match.group(1):
        query = event.pattern_match.group(1)
        await event.edit("wi8 ..!     ....")
    elif reply.message:
        query = reply.message
        await event.edit("  ....")
    else:
    	await event.edit("`    `")
    	return
    await catmusic(str(query),"128k")
    l = glob.glob("*.mp3")
    if l:
        await event.edit("..!       ")
    else:
        await event.edit(f"..!      `{query}`")
    loa = l[0]    
    await borg.send_file(
                event.chat_id,
                loa,
                force_document=True,
                allow_cache=False,
                caption=query,
                reply_to=reply_to_id
            )
    await event.delete()
    os.system("rm -rf *.mp3")
    subprocess.check_output("rm -rf *.mp3",shell=True)
