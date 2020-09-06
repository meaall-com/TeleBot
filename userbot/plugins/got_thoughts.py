# BY @Deonnn
"""
Game of Thrones Thoughts plugin
by @
command .gott

"""

from telethon import events

import asyncio

import os

import sys

import random



@borg.on(events.NewMessage(pattern=r"\.gott", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    await event.edit("Typing...")

    await asyncio.sleep(2)

    x=(random.randrange(1,40))

    if x==1:

        await event.edit("`\"كل علماء العالم ومثقفيه وهداته ودعاة الفضيلة فيه لا يستطيعون هداية من لايهتدِ بالقرآن  ولايستطيعون مهما فعلوا تحرير قلب غوي من هواه ، ولا تحطيم إسار تبعية مرتزق خسيس يعبد المال ويهوى السلطة ، ولا بعث الهمة والحمية والمروءة في روحه الخسيسة؛ لأن القرآن وقيمه ومبادئه وأخلاقه هي من تصنع في روح وقلب الانسان التقي  البطولة والحمية والهمة والغيرة والكرامة -إن العزة لله ورسوله والذين آمنوا-\"`")

    if x==2:

        await event.edit("`\"ا\"`")

    if x==3:

        await event.edit("`\"ن\"`")

    if x==4:

        await event.edit("`\"ا\"`")

    if x==5:

        await event.edit("`\"ا\"`")

    if x==6:

        await event.edit("`\"س\"`")

    if x==7:

        await event.edit("`\"ا\"`")    

    if x==8:

        await event.edit("`\"ع\"`")

    if x==9:

        await event.edit("`\"غ\"`")

    if x==10:

        await event.edit("ا")
        
    if x==11:

        await event.edit("`\"ن\"`")
        
    if x==12:

        await event.edit("عععع")
        
    if x==13:

        await event.edit("ا")
        
    if x==14:

        await event.edit("`\"The day will come when you think you are safe and happy, and your joy will turn to ashes in your mouth.\"`")
        
    if x==15:

        await event.edit("`\"The night is dark and full of terrors.\"`")
        
    if x==16:

        await event.edit("`\"You know nothing, Jon Snow.\"`")
        
    if x==17:

        await event.edit("`\"Night gathers, and now my watch begins!\"`")
        
    if x==18:

        await event.edit("`\"A Lannister always pays his debts.\"`")
        
    if x==19:

        await event.edit("`\"Burn them all!\"`")
        
    if x==20:

        await event.edit("`\"What do we say to the God of death?\"`")
        
    if x==21:

        await event.edit("`\"There's no cure for being a c*nt.\"`")
        
    if x==22:

        await event.edit("`\"Winter is coming!\"`")
        
    if x==23:

        await event.edit("`\"That's what I do: I drink and I know things.\"`")
        
    if x==24:

        await event.edit("`\"I am the dragon's daughter, and I swear to you that those who would harm you will die screaming.\"`")
        
    if x==25:

        await event.edit("`\"A lion does not concern himself with the opinion of sheep.\"`")
        
    if x==26:

        await event.edit("`\"Chaos isn't a pit. Chaos is a ladder.\"`")
    
    if x==27:

        await event.edit("`\"I understand that if any more words come pouring out your c*nt mouth, I'm gonna have to eat every f*cking chicken in this room.\"`")
        
    if x==28:

        await event.edit("`\"If you think this has a happy ending, you haven't been paying attention.\"`")
        
    if x==29:

        await event.edit("`\"If you ever call me sister again, I'll have you strangled in your sleep.\"`")
        
    if x==30:

        await event.edit("`\"A girl is Arya Stark of Winterfell. And I'm going home.\"`")
        
    if x==31:

        await event.edit("`\"Any man who must say 'I am the King' is no true King.\"`")
        
    if x==32:

        await event.edit("`\"If I fall, don't bring me back.\"`")
        
    if x==33:

        await event.edit("`\"Lannister, Targaryen, Baratheon, Stark, Tyrell... they're all just spokes on a wheel. This one's on top, then that one's on top, and on and on it spins, crushing those on the ground.\"`")
        
    if x==34:

        await event.edit("`\"Hold the door!`")
        
    if x==35:

        await event.edit("`\"When people ask you what happened here, tell them the North remembers. Tell them winter came for House Frey.\"`")
        
    if x==36:

        await event.edit("`\"Nothing f*cks you harder than time.\"`")
        
    if x==37:

        await event.edit("`\"There is only one war that matters. The Great War. And it is here.\"`")
        
    if x==38:

        await event.edit("`\"Power is power!\"`")
        
    if x==39:

        await event.edit("`\"I demand a trial by combat!\"`")
        
    if x==40:

        await event.edit("`\"I wish I was the monster you think I am!\"`")
