from .. import call, db
from typing import Union
from pyrogram.types import Message
from pytgcalls.types import *
from pytgcalls.types.stream import *


async def edit_or_reply(message: Message, *args, **kwargs) -> Message:
    msg = (
        message.edit_text
        if bool(message.from_user and message.from_user.is_self or message.outgoing)
        else (message.reply_to_message or message).reply_text
    )
    return await msg(*args, **kwargs)


eor = edit_or_reply


async def put_que(chat_id, file, type):
    put = {
        "chat_id": chat_id,
        "file": file,
        "type": type,
    }
    check = db.get(chat_id)
    if not check:
        db[chat_id] = []
        db[chat_id].append(put)
    else:
        que = db[chat_id]
        que.append(put)
        return int(len(que)-1)


@call.on_kicked()
async def kicked_handler(_, chat_id: int):
    try:
        check = db.get(chat_id)
        if check:
            return check.pop(0)
        return
    except:
        pass


@call.on_closed_voice_chat()
async def closed_voice_chat_handler(_, chat_id: int):
    try:
        check = db.get(chat_id)
        if check:
            return check.pop(0)
        return
    except:
        pass


@call.on_left()
async def left_handler(_, chat_id: int):
    try:
        check = db.get(chat_id)
        if check:
            return check.pop(0)
        return
    except:
        pass


@call.on_stream_end()
async def stream_end_handler(_, update: Update):
    chat_id = update.chat_id
    try:
        check = db.get(chat_id)
        if check:
            que = db[chat_id]
            que.pop(0)
            if len(que) == 0:
                db.pop(chat_id)
                return await call.leave_group_call(chat_id)
            else:
                file = check[0]["file"]
                type = check[0]["type"]
                if type == "Audio":
                    stream = AudioPiped(
                        file,
                        HighQualityAudio(),
                    )
                elif type == "Video":
                    stream = AudioVideoPiped(
                        file,
                        HighQualityAudio(),
                        HighQualityVideo(),
                    )
                return await call.change_stream(chat_id, stream)
        return
    except Exception as e:
        print(f"**Error:** `{e}`")
