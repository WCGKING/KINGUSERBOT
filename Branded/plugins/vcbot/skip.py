from asyncio.queues import QueueEmpty
from pyrogram import filters
from pytgcalls.exceptions import GroupCallNotFound

from ... import app, eor, cdx, cdz
from ...modules.helpers.wrapper import *
from ...modules.mongo.streams import *
from ...modules.utilities import queues
from ...modules.utilities.streams import *


@app.on_message(cdx(["skp", "skip"]) & ~filters.private)
@sudo_users_only
async def skip_stream(client, message):
    chat_id = message.chat.id
    try:
        a = await call.get_call(chat_id)
        if (a.status == "playing"
            or a.status == "paused"
        ):
            queues.task_done(chat_id)
            if queues.is_empty(chat_id):
                await call.leave_group_call(chat_id)
                return await eor(message, "**Empty Queue, So\nLeaving VC!**")
            check = queues.get(chat_id)
            file = check["file"]
            type = check["type"]
            stream = await run_stream(file, type)
            await call.change_stream(chat_id, stream)
            return await eor(message, "**Stream Skipped!**")
        elif a.status == "not_playing":
            await eor(message, "**Nothing Playing!**")
    except GroupCallNotFound:
        await eor(message, "**I am Not in VC!**")
    except Exception as e:
        print(f"Error: {e}")



@app.on_message(cdz(["cskp", "cskip"]) & ~filters.private)
@sudo_users_only
async def skip_stream_(client, message):
    user_id = message.from_user.id
    chat_id = await get_chat_id(user_id)
    if chat_id == 0:
        return await eor(message,
            "**🥀 No Stream Chat Set❗**"
    )
    try:
        a = await call.get_call(chat_id)
        if (a.status == "playing"
            or a.status == "paused"
        ):
            queues.task_done(chat_id)
            if queues.is_empty(chat_id):
                await call.leave_group_call(chat_id)
                return await eor(message, "**Empty Queue, So\nLeaving VC!**")
            check = queues.get(chat_id)
            file = check["file"]
            type = check["type"]
            stream = await run_stream(file, type)
            await call.change_stream(chat_id, stream)
            return await eor(message, "**Stream Skipped!**")
        elif a.status == "not_playing":
            await eor(message, "**Nothing Playing!**")
    except GroupCallNotFound:
        await eor(message, "**I am Not in VC!**")
    except Exception as e:
        print(f"Error: {e}")

