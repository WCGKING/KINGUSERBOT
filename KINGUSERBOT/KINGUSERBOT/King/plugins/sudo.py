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


__NAME__ = "Sudo"
__MENU__ = f"""
**🥀 Add Or Remove Sudo Users
From Your Userbot ✨...**

`.addsudo` - Reply This Comd
To Any Message Of Target User
To Add in Sudo User.

`.delsudo` - Reply This Comd
To Any Message Of Target User
To Remove From Sudo User.

`.sudolist - Get All Active
Sudo Users List.

**Some Shortcut Commands:**
=> [`.as`, `.ds`, `.sl`]
"""
