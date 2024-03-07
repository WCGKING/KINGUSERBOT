from typing import Union
from pyrogram.types import *


async def edit_or_reply(message: Message, *args, **kwargs) -> Message:
    try:
        msg = (
            message.edit_text
            if bool(message.from_user and message.from_user.is_self or message.outgoing)
            else (message.reply_to_message or message).reply_text
        )
    except:
        msg = (
            message.edit_text
            if bool(message.from_user and message.outgoing)
            else (message.reply_to_message or message).reply_text
        )
    
    return await msg(*args, **kwargs)


def get_audio_name(audio: Union[Audio, Voice]):
    try:
        file_name = (
            audio.file_unique_id
            + "."
            + (
                (audio.file_name.split(".")[-1])
                if (not isinstance(audio, Voice))
                else "ogg"
            )
        )
    except:
        file_name = audio.file_unique_id + "." + ".ogg"
        
    return file_name


def get_video_name(video: Union[Video, VideoNote]):
    try:
        file_name = (
            video.file_unique_id
            + "."
            + (video.file_name.split(".")[-1])
        )
    except:
        file_name = video.file_unique_id + "." + "mp4"
    
    return file_name

