from ... import app, cdx, eor, super_user_only
from ...console import SUDOERS
from ...modules.mongo.sudoers import add_sudo, del_sudo


@app.on_message(cdx(["addsudo", "as"]))
@super_user_only
async def add_sudo_user(client, message):
    try:
        aux = await eor(message, "**🔄 Processing ...**")
        if not message.reply_to_message:
            if len(message.command) != 2:
                return await aux.edit(
                    "Reply to a user's message or give username/user_id."
                )
            user = message.text.split(None, 1)[1]
            if "@" in user:
                user = user.replace("@", "")
            user = await app.get_users(user)
            if user.id in SUDOERS:
                return await aux.edit(
                "{0} is already a sudo user.".format(user.mention)
            )
            added = await add_sudo(user.id)
            if added:
                SUDOERS.append(user.id)
                await aux.edit("Added **{0}** to Sudo Users.".format(user.mention))
            else:
                await aux.edit("Failed")
            return
        user_id = message.reply_to_message.from_user.id
        if user_id in SUDOERS:
            return await aux.edit(
                "{0} is already a sudo user.".format(
                    message.reply_to_message.from_user.mention
                )
            )
        added = await add_sudo(user_id)
        if added:
            SUDOERS.append(user_id)
            await aux.edit(
                "Added **{0}** to Sudo Users.".format(
                    message.reply_to_message.from_user.mention
                )
            )
        else:
            await aux.edit("Something wrong happened.")
        return
    except Exception as e:
        print("Error: `{e}`")
        return


@app.on_message(cdx(["delsudo", "ds"]))
@super_user_only
async def del_sudo_user(client, message):
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


@app.on_message(cdx(["sudousers", "sudolist", "sl"]))
@super_user_only
async def sudo_users_list(client, message):
    text = "⭐️<u> **SUPER USER:**</u>\n"
    count = 0
    try:
        user = (
            app.me.name if not app.me.mention else app.me.mention
        )
    except Exception:
        pass
    text += f"➤ {user}\n"
    users = 0
    for user_id in SUDOERS:
        if user_id != app.me.id:
            try:
                user = await app.get_users(user_id)
                user = (
                    user.first_name
                    if not user.mention
                    else user.mention
                )
                if users == 0:
                    users += 1
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

`.addsudo` - Use This Command
to Add an User in Sudo List.

`.delsudo` - Use This Command
to Remove an User from Sudo.

`.sudolist` - Check Your Sudo
Users By Getting A List.

**Some Shortcut Commands:**
=> [`.as`, `.ds`, `.sl`]
"""
