import asyncio

from pyrogram import filters
from pyrogram.enums import ChatType

from ... import app, cdx, eor, vars
from ...modules.mongo.pmguard import *


@app.on_message(cdx(["pm", "pmpermit", "pmguard"]) & filters.me)
async def pm_on_off(client, message):
    if len(message.command) < 2:
        return await eor(message,
            "Hey, What You Want To Do ?\n\nExample: `.pm on` | `.pm off`")
    aux = await eor(message, "Processing ...")
    query = message.text.split(None, 1)[1].lower()
    if query == "on":
        set_permit = await set_pm_permit(True)
        if set_permit:
            return await aux.edit("PM Permit Turned On !")
        return await aux.edit("PM Permit Already On !")
        
    elif query == "off":
        set_permit = await set_pm_permit(False)
        if set_permit:
            return await aux.edit("PM Permit Turned Off !")
        return await aux.edit("PM Permit Already Off !")
        


@app.on_message(cdx(["a", "approve"]) & filters.private  & filters.me)
async def pm_approve(client, message):
    check = vars.OLD_MSG
    flood = vars.FLOODXD
    uid = message.chat.id
    if message.reply_to_message:
        reply = message.reply_to_message
        replied_user = reply.from_user
        if replied_user.is_self:
            return await message.edit("You can't do that to yourself.")
    permit = await add_approved_user(uid)
    if permit:
        if str(uid) in check and str(uid) in flood:
            try:
                await check[str(uid)].delete()
                flood[str(uid)] = 0
            except BaseException:
                pass
        await message.edit("Successfully Approved.")
    else:
        await message.edit("This user already approved.")
    await asyncio.sleep(2)
    return await message.delete()


@app.on_message(cdx(["da", "disapprove"]) & filters.private & filters.me)
async def pm_disapprove(client, message):
    uid = message.chat.id
    if message.reply_to_message:
        reply = message.reply_to_message
        replied_user = reply.from_user
        if replied_user.is_self:
            return await message.edit("You can't do that to yourself.")
    permit = await del_approved_user(uid)
    if permit:
        await message.edit("Successfully Disapproved.")
    else:
        await message.edit("This user is not approved !")
    await asyncio.sleep(2)
    return await message.delete()


@app.on_message(cdx(["block"]) & filters.me)
async def block_user_func(client, message):
    if message.chat.type == ChatType.PRIVATE:
        user_id = message.chat.id
    elif message.chat.type != ChatType.PRIVATE:
        if not message.reply_to_message:
            return await message.edit("Reply to user message.")
        reply = message.reply_to_message
        replied_user = reply.from_user
        if replied_user.is_self:
            return await message.edit("You can't do that to yourself.")
        user_id = replied_user.id
    await message.edit("Successfully Block User!!!")
    await client.block_user(user_id)


@app.on_message(cdx(["unblock"]) & filters.me)
async def unblock_user_func(client, message):
    if message.chat.type == ChatType.PRIVATE:
        user_id = message.chat.id
    elif message.chat.type != ChatType.PRIVATE:
        if not message.reply_to_message:
            return await message.edit("Reply to user message.")
        reply = message.reply_to_message
        replied_user = reply.from_user
        if replied_user.is_self:
            return await message.edit("You can't do that to yourself.")
        user_id = replied_user.id
    await client.unblock_user(user_id)
    await message.edit("Unblock User Successfully !")


__NAME__ = "Guard"
__MENU__ = f"""
**🥀 An Advanced Security System
To Protect From DM Spams ✨.**

`.pmguard [`on`|off`] - Activate
or Deactivate PM Guard Security.

`.approve` - Approve An User For
Chat With in DM.

`.disapprove` - To Disapprove An
User (Remove From Allowed List).

`.block` - Block An User And Add
in Your Blocklist.

`.unblock` - Unblock An User And
Renove From Your Blocklist.
"""

