import asyncio

from pyrogram import *
from pyrogram.types import Message

from .. import *
from ..modules.data import (is_gdel_user,
    get_gdel_user, get_gdel_count,
    add_gdel_user, del_gdel_user)



@app.on_message(commandx(["gdl", "gdel", "gdelete"]) & SUPUSER)
async def add_gdelete_user(client, message: Message):
    if not message.reply_to_message:
        if len(message.command) != 2:
            return await message.reply_text("Reply to a user's message or give username/user_id.")
        user = message.text.split(None, 1)[1]
        user = await app.get_users(user)
        user_id = user.id
        mention = user.mention
    else:
        user_id = message.reply_to_message.from_user.id
        mention = message.reply_to_message.from_user.mention
    if user_id == message.from_user.id:
        return await message.reply_text("You want to add Global Delete yourself? How Fool!")
    elif user_id == SUPUSER:
        return await message.reply_text("Should i activate Global Delete on myself? Lol")
    elif user_id in SUDOERS:
        return await message.reply_text("You want add Global Delete on sudo user?")
    is_gdel = await is_gdel_user(user_id)
    if is_gdel:
        return await message.reply_text("{0} is already affected by **Global Delete**".format(mention))
    if user_id not in GDELSUB:
        GDELSUB.add(user_id)
    await add_gdel_user(user_id)
    await message.reply_text("**Global Delete Activated.")



@app.on_message(commandx(["ungdl", "ungdel", "ungdelete"]) & SUPUSER)
async def del_gdelete_user(client, message: Message):
    if not message.reply_to_message:
        if len(message.command) != 2:
            return await message.reply_text("Reply to a user's message or give username/user_id.")
        user = message.text.split(None, 1)[1]
        user = await app.get_users(user)
        user_id = user.id
        mention = user.mention
    else:
        user_id = message.reply_to_message.from_user.id
        mention = message.reply_to_message.from_user.mention
    is_gdel = await is_gdel_user(user_id)
    if not is_gdel:
        return await message.reply_text("{0} is not affected by Global Delete.".format(mention))
    if user_id in GDELSUB:
        GDELSUB.remove(user_id)
    await del_gdel_user(user_id)
    await message.reply_text("De-Activated Global Delete On {0}".format(mention)
    )



@app.on_message(commandx(["gdlst", "gdellist", "gdelusers"]) & SUPUSER)
async def gdelete_users_list(client, message: Message):
    counts = await get_gdel_count()
    if counts == 0:
        return await message.reply_text("No Global Delete Users Found.")
    txt = await message.reply_text("Please wait a while.. Fetching Global Delete users list")
    msg = "Global Delete Users:\n\n"
    count = 0
    users = await get_gdel_user()
    for user_id in users:
        count += 1
        try:
            user = await app.get_users(user_id)
            user = (
                user.first_name if not user.mention else user.mention
            )
            msg += f"{count}➤ {user}\n"
        except Exception:
            msg += f"{count}➤ [Unfetched User]{user_id}\n"
            continue
    if count == 0:
        return await txt.edit_text("No Global Delete Users Found.")
    else:
        return await txt.edit_text(msg)
        

__NAME__ = "Gᴅᴇʟ"
__MENU__ = f"""
**__Rᴇᴘʟʏ Tᴏ Aɴ Usᴇʀ Oʀ Gɪᴠᴇ
Usᴇʀɴᴀᴍᴇ Tᴏ Aᴄᴛɪᴠᴀᴛᴇ Gʟᴏʙᴀʟ
Dᴇʟᴇᴛᴇ Oɴ Usᴇʀ:__**
__(ᴏɴʟʏ ᴏᴡɴᴇʀ ᴄᴀɴ ᴜsᴇ ᴛʜɪs)__

`.gdel` - __ᴀᴄᴛɪᴠᴀᴛᴇ ɢʟᴏʙᴀʟ ᴅᴇʟ
ᴏɴ ᴀɴʏ ᴜsᴇʀ__

`.ungdel` - __ʀᴇᴍᴏᴠᴇ ᴀɴʏ ᴜsᴇʀ
ғʀᴏᴍ ɢʟᴏʙᴀʟ ᴅᴇʟᴇᴛᴇ__

`.gdelusers` - __ɢᴇᴛ ʟɪsᴛ ᴏғ ᴀʟʟ
ɢʟᴏʙᴀʟ ᴅᴇʟᴇᴛᴇ ᴜsᴇʀs__
"""
