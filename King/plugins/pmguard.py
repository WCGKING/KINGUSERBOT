import asyncio

from pyrogram import Client, filters
from pyrogram.enums import ChatType
from pyrogram.types import *

from .. import *
from ..modules.data import approve, disapprove, is_approved

MSG_PERMIT = """
PM_SECURITY Daxx-USERBOT

{}
▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂
⍟ You have {}/{} warning!!!
"""

DEFAULT = """
WELCOME....

Hi, this is the keeper of private messages. Don't spam ya or I'll block you. Wait until my master receives your message.
"""


@app.on_message(
    (
        filters.private
        & filters.incoming
        & ~filters.service
        & ~filters.me
        & ~filters.bot
        & ~filters.via_bot
    )
)
async def pmpermit_func(client: Client, message: Message):
    user_ = message.from_user
    approved = await is_approved()
    pmper = var.PMPERMIT
    if pmper == str(False):
        return True
    if user_.is_bot:
        return
    if user_.is_self:
        return
    if user_.is_contact:
        return
    if user_.is_verified:
        return
    if user_.is_scam:
        await message.reply_text("Imposter Detected!\nAutomatic Blocking!!!")
        await client.block_user(user_.id)
        return
    if user_.is_support:
        return
    if user_.id in approved:
        return
    limits = var.PERMIT_LIMIT
    async for m in client.get_chat_history(user_.id, limit=limits):
        if m.reply_markup:
            await m.delete()
    if str(user_.id) in flood:
        flood[str(user_.id)] += 1
    else:
        flood[str(user_.id)] = 1
    if flood[str(user_.id)] > limits:
        await message.reply_text("Spammer Detected!\nAutomatic Blocking User!!!")
        if str(user_.id) in OLD_MSG:
            OLD_MSG.pop(str(user_.id))
            flood.update({user_.id: 0})
        return await client.block_user(user_.id)
    getmsg = Config.PERMIT_MSG
    pm_message = DEFAULT if not getmsg else getmsg
    msg_dlt = await client.send_message(
        user_.id,
        MSG_PERMIT.format(pm_message, flood[str(user_.id)], limits),
    )
    if str(user_.id) in OLD_MSG:
        try:
            await OLD_MSG[str(user_.id)].delete()
        except BaseException:
            pass
    OLD_MSG[str(user_.id)] = msg_dlt


@app.on_message(commandx(["approve", "a"]))
async def pm_approve(client: Client, message: Message):
    permit = await is_approved()
    if message.reply_to_message:
        reply = message.reply_to_message
        replied_user = reply.from_user
        if replied_user.is_self:
            await message.edit("You can't do that to yourself.")
            return
        uid = replied_user.id
        if uid in permit:
            return await message.reply("This user already exists in the database.")
        await approve(uid)
        xnxx = await message.reply("Your message was received.")
        if str(uid) in OLD_MSG and str(uid) in flood:
            await OLD_MSG[str(uid)].delete()
            flood[str(uid)] = 0
        await asyncio.sleep(3)
        await xnxx.delete()
    else:
        aname = message.chat
        if not aname.type == ChatType.PRIVATE:
            await message.reply(
                "You're not currently in PM and you haven't replied to someone's messages."
            )
            return
        uid = aname.id
        if uid in permit:
            return await message.reply("This user already exists in the database")
        await approve(uid)
        xnxx = await message.reply("Your message was received.")
        try:
            if str(uid) in OLD_MSG and str(uid) in flood:
                await OLD_MSG[str(uid)].delete()
                flood[str(uid)] = 0
        except BaseException:
            pass
        await asyncio.sleep(3)
        await xnxx.delete()


@app.on_message(commandx(["disapprove", "da"]))
async def pm_disapprove(client: Client, message: Message):
    permit = await is_approved()
    if message.reply_to_message:
        reply = message.reply_to_message
        replied_user = reply.from_user
        if replied_user.is_self:
            await message.reply("You can't do that to yourself.")
            return
        uid = replied_user.id
        if uid not in permit:
            return await message.reply("User does not exist in database.")
        await disapprove(uid)
        xnxx = await message.reply("Your message has been rejected.")
        await asyncio.sleep(3)
        await xnxx.delete()
    else:
        aname = message.chat
        if aname.type != ChatType.PRIVATE:
            await message.edit(
                "You're not currently in PM and you haven't replied to someone's messages."
            )
            return
        uid = aname.id
        if uid not in permit:
            return await message.reply("User does not exist in database.")
        await disapprove(uid)
        xnxx = await message.reply("Your message has been rejected.")
        await asyncio.sleep(3)
        await xnxx.delete()


@app.on_message(commandx(["block"]))
async def block_user_func(client: Client, message: Message):
    if not message.reply_to_message:
        return await message.reply("Reply to user message.")
    user_id = message.reply_to_message.from_user.id
    # Blocking user after editing the message so that other person can get the
    # update.
    await message.reply("Successfully Block User!!!")
    await client.block_user(user_id)


@app.on_message(commandx(["unblock"]))
async def unblock_user_func(client: Client, message: Message):
    if not message.reply_to_message:
        return await message.reply("Reply to user message.")
    user_id = message.reply_to_message.from_user.id
    await client.unblock_user(user_id)
    await message.reply("Unblock User Successfully!!!")


__NAME__ = "PM"
__MENU__ = f"""
**🥀 Private Message Guard ✨...**

`.a` or `.approve`
For approve user

`.da` or `.disapprove`
For rejected user

`.block`
For Blocking User

`.unblock`
For Unblock User
"""
