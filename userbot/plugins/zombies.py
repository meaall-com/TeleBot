# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

"""Cmd = `.zombie`
الاستخدام: للبحث عن الحسابات المحذوفة في المجموعات والقنوات.
استخدم .zombies clean لإزالة الحسابات المحذوفة من المجموعات والقنوات.
\ n مرفوع بواسطة © [مع الله] (t.me/meaallh100) و © [E"""

from telethon import events
from userbot.utils import admin_cmd
#
from asyncio import sleep
from os import remove

from telethon.errors import (BadRequestError, ChatAdminRequiredError,
                             ImageProcessFailedError, PhotoCropSizeSmallError,
                             UserAdminInvalidError)
from telethon.errors.rpcerrorlist import (UserIdInvalidError,
                                          MessageTooLongError)
from telethon.tl.functions.channels import (EditAdminRequest,
                                            EditBannedRequest,
                                            EditPhotoRequest)
from telethon.tl.types import (ChannelParticipantsAdmins, ChatAdminRights,
                               ChatBannedRights, MessageEntityMentionName,
                               MessageMediaPhoto)


# =================== CONSTANT ===================

BANNED_RIGHTS = ChatBannedRights(
    until_date=None,
    view_messages=True,
    send_messages=True,
    send_media=True,
    send_stickers=True,
    send_gifs=True,
    send_games=True,
    send_inline=True,
    embed_links=True,
)

UNBAN_RIGHTS = ChatBannedRights(
    until_date=None,
    send_messages=None,
    send_media=None,
    send_stickers=None,
    send_gifs=None,
    send_games=None,
    send_inline=None,
    embed_links=None,
)

MUTE_RIGHTS = ChatBannedRights(until_date=None, send_messages=True)

UNMUTE_RIGHTS = ChatBannedRights(until_date=None, send_messages=False)
# ================================================



@borg.on(admin_cmd(pattern=f"zombies", allow_sudo=True))
@borg.on(events.NewMessage(pattern="^.zombies(?: |$)(.*)", outgoing=True))
async def rm_deletedacc(show):
    """ بالنسبة لأمر .zombies ، قم بإدراج جميع حسابات الأشباح / المحذوفة / الزومبي في الدردشة. """

    con = show.pattern_match.group(1).lower()
    del_u = 0
    del_status = "`لم يتم العثور على حسابات محذوفة ، المجموعة نظيفة`"

    if con != "clean":
        await show.edit("`البحث عن حسابات شبح / محذوفة / زومبي ...`")
        async for user in show.client.iter_participants(show.chat_id):

            if user.deleted:
                del_u += 1
                await sleep(1)
        if del_u > 0:
            del_status = f"`Found` ** {del_u} **` حسابات شبح / محذوفة / زومبي في هذه المجموعة ، \
            \ n نظفهم باستخدام .zombies clean`"
        await show.edit(del_status)
        return

    # Here laying the sanity check
    chat = await show.get_chat()
    admin = chat.admin_rights
    creator = chat.creator

    # Well
    if not admin and not creator:
        await show.edit("`أنا لست مشرفًا هنا!`")
        return

    await show.edit("`جارٍ حذف الحسابات المحذوفة ... \ n هل يمكنني فعل ذلك؟!؟!`")
    del_u = 0
    del_a = 0

    async for user in show.client.iter_participants(show.chat_id):
        if user.deleted:
            try:
                await show.client(
                    EditBannedRequest(show.chat_id, user.id, BANNED_RIGHTS))
            except ChatAdminRequiredError:
                await show.edit("`ليس لدي حقوق حظر في هذه المجموعة`")
                return
            except UserAdminInvalidError:
                del_u -= 1
                del_a += 1
            await show.client(
                EditBannedRequest(show.chat_id, user.id, UNBAN_RIGHTS))
            del_u += 1


    if del_u > 0:
        del_status = f"Cleaned **{del_u}** deleted account(s)"

    if del_a > 0:
        del_status = f"Cleaned **{del_u}** deleted account(s) \
        \n**{del_a}** deleted admin accounts are not removed"


    await show.edit(del_status)
    await sleep(2)
    await show.delete()


    if Config.G_BAN_LOGGER_GROUP is not None:
        await show.client.send_message(
            Config.G_BAN_LOGGER_GROUP, "#CLEANUP\n"
            f"Cleaned **{del_u}** deleted account(s) !!\
            \nCHAT: {show.chat.title}(`{show.chat_id}`)")

