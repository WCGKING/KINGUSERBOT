from ... import *
from ...modules.mongo.streams import *
from pyrogram import filters
from pytgcalls.exceptions import GroupCallNotFound


@app.on_message(cdx(["pse", "pause"]) & ~filters.private)
@sudo_users_only
async def pause_stream(client, message):
    chat_id = message.chat.id
    try:
        a = await call.get_call(chat_id)
        if a.status == "playing":
            await call.pause_stream(chat_id)
            await eor(message, "**Stream Paused!**")
        elif a.status == "paused":
            await eor(message, "**Already Paused!**")
        elif a.status == "not_playing":
            await eor(message, "**Nothing Streaming!**")
    except GroupCallNotFound:
        await eor(message, "**I am Not in VC!**")
    except Exception as e:
        print(f"Error: {e}")


@app.on_message(cdz(["cpse", "cpause"]))
@sudo_users_only
async def pause_stream_(client, message):
    user_id = message.from_user.id
    chat_id = await get_chat_id(user_id)
    if chat_id == 0:
        return await eor(message,
            "**🥀 No Stream Chat Set❗**"
    )
    try:
        a = await call.get_call(chat_id)
        if a.status == "playing":
            await call.pause_stream(chat_id)
            await eor(message, "**Stream Paused!**")
        elif a.status == "paused":
            await eor(message, "**Already Paused!**")
        elif a.status == "not_playing":
            await eor(message, "**Nothing Streaming!**")
    except GroupCallNotFound:
        await eor(message, "**I am Not in VC!**")
    except Exception as e:
        print(f"Error: {e}")

  
