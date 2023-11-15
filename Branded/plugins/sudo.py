from .. import *
from ..modules.data import add_sudo, del_sudo
from pyrogram.types import Message


@app.on_message(commandx(["addsudo", "as"]) & SUPUSER)
async def add_sudo_user(client, message: Message):
    if not message.reply_to_message:
        if len(message.command) != 2:
            return await message.edit("Reply to a user's message or give username/user_id.")
        user = message.text.split(None, 1)[1]
        if "@" in user:
            user = user.replace("@", "")
        user = await app.get_users(user)
        if user.id in SUDOERS:
            return await message.edit(
                "{0} is already a sudo user.".format(user.mention)
            )
        added = await add_sudo(user.id)
        if added:
            SUDOERS.add(user.id)
            await message.edit("Added **{0}** to Sudo Users.".format(user.mention))
        else:
            await message.edit("Failed")
        return
    user_id = message.reply_to_message.from_user.id
    if user_id in SUDOERS:
        return await message.edit(
            "{0} is already a sudo user.".format(
                message.reply_to_message.from_user.mention
            )
        )
    added = await add_sudo(user_id)
    if added:
        SUDOERS.add(user_id)
        await message.edit(
            "Added **{0}** to Sudo Users.".format(
                message.reply_to_message.from_user.mention
            )
        )
    else:
        await message.edit("Something wrong happened.")
    return


@app.on_message(commandx(["delsudo", "ds"]) & SUPUSER)
async def del_sudo_user(client, message: Message):
    if not message.reply_to_message:
        if len(message.command) != 2:
            return await message.edit("Reply to a user's message or give username/user_id.")
        user = message.text.split(None, 1)[1]
        if "@" in user:
            user = user.replace("@", "")
        user = await app.get_users(user)
        if user.id not in SUDOERS:
            return await message.edit("Not a part of Bot's Sudo.")
        removed = await del_sudo(user.id)
        if removed:
            SUDOERS.remove(user.id)
            await message.edit("Removed from Bot's Sudo User")
            return
        else:
            await message.edit(f"Something wrong happened.")
            return
    user_id = message.reply_to_message.from_user.id
    if user_id not in SUDOERS:
        return await message.edit("Not a part of Bot's Sudo.")
    removed = await del_sudo(user_id)
    if removed:
        SUDOERS.remove(user_id)
        await message.edit("Removed from Bot's Sudo User")
        return
    else:
        await message.edit(f"Something wrong happened.")
        return

@app.on_message(commandx(["sudousers", "sudolist", "sl"]) & SUPUSER)
async def sudo_users_list(client, message: Message):
    text = "⭐️<u> **SUPER USER:**</u>\n"
    count = 0
    try:
        user = (
            app.name if not app.mention else app.mention
        )
    except Exception:
        pass
    text += f"➤ {user}\n"
    smex = 0
    for user_id in SUDOERS:
        if user_id != app.id:
            try:
                user = await app.get_users(user_id)
                user = (
                    user.first_name
                    if not user.mention
                    else user.mention
                )
                if smex == 0:
                    smex += 1
                    text += "\n⭐️<u> **SUDO USERS:**</u>\n"
                count += 1
                text += f"{count}➤ {user}\n"
            except Exception:
                continue
    if not text:
        await message.edit("No Sudo Users Found!")
    else:
        await message.edit(text)


__NAME__ = "✨ ꜱᴜᴅᴏ 🌷"
__MENU__ = f"""
**🥀 𝗔𝗗𝗗 𝗢𝗥 𝗥𝗘𝗠𝗢𝗩𝗘 𝗦𝗨𝗗𝗢 𝗨𝗦𝗘𝗥𝗦
𝗙𝗥𝗢𝗠 𝗬𝗢𝗨𝗥 𝗨𝗦𝗘𝗥𝗕𝗢𝗧 ✨...**

`.addsudo` - 𝗥𝗘𝗣𝗟𝗬 𝗧𝗛𝗜𝗦 𝗖𝗢𝗠𝗗
𝗧𝗢 𝗔𝗡𝗬 𝗠𝗘𝗦𝗦𝗔𝗚𝗘 𝗢𝗙 𝗧𝗔𝗥𝗚𝗘𝗧 𝗨𝗦𝗘𝗥 
𝗧𝗢 𝗔𝗗𝗗 𝗜𝗡 𝗦𝗨𝗗𝗢 𝗨𝗦𝗘𝗥.

`.delsudo` - 𝗥𝗘𝗣𝗟𝗬 𝗧𝗛𝗜𝗦 𝗖𝗢𝗠𝗗
T𝗢 𝗔𝗡𝗬 𝗠𝗘𝗦𝗦𝗔𝗚𝗘 𝗢𝗙 𝗧𝗔𝗥𝗚𝗘𝗧 𝗨𝗦𝗘𝗥 
𝗧𝗢 𝗥𝗘𝗠𝗢𝗩𝗘 𝗙𝗥𝗢𝗠 𝗦𝗨𝗗𝗢 𝗨𝗦𝗘𝗥.

`.sudolist -𝗚𝗘𝗧 𝗔𝗟𝗟 𝗔𝗖𝗧𝗜𝗩𝗘
𝗦𝗨𝗗𝗢 𝗨𝗦𝗘𝗥 𝗟𝗜𝗦𝗧.

**𝗦𝗢𝗠𝗘 𝗦𝗛𝗢𝗥𝗧𝗖𝗨𝗧 𝗖𝗢𝗠𝗠𝗔𝗡𝗗𝗦:**
=> [`.as`, `.ds`, `.sl`]
"""
