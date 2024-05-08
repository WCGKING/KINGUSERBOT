from ... import *
from ...modules.mongo.streams import *
from pyrogram import filters
from pytgcalls.exceptions import NoActiveGroupCall


@app.on_message(cdx(["join", "joinvc"]) & ~filters.private)
@sudo_users_only
async def join_vc(client, message):
    chat_id = message.chat.id
    a_calls = await call.calls
    if_chat = a_calls.get(chat_id)
    if if_chat:
        return await eor(
            message, "**Already Joined VC!**"
        )
    if not if_chat:
        try:
            await call.play(chat_id)
            return await eor(
                message, "**Joined VC!**"
            )
        except NoActiveGroupCall:
            return await eor(
                message, "**No Active VC!**"
            )
        except Exception as e:
            print(f"Error: {e}")
            pass
        


@app.on_message(cdz(["cjoin", "cjoinvc"]))
@sudo_users_only
async def join_vc_(client, message):
    user_id = message.from_user.id
    chat_id = await get_chat_id(user_id)
    if chat_id == 0:
        return await eor(message,
            "**🥀 No Stream Chat Set❗**"
    )
    a_calls = await call.calls
    if_chat = a_calls.get(chat_id)
    if if_chat:
        return await eor(
            message, "**Already Joined VC!**"
        )
    if not if_chat:
        try:
            await call.play(chat_id)
            return await eor(
                message, "**Joined VC!**"
            )
        except NoActiveGroupCall:
            return await eor(
                message, "**No Active VC!**"
            )
        except Exception as e:
            print(f"Error: {e}")
            pass
