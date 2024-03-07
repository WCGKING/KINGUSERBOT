import asyncio, os, yt_dlp

from . import queues
from ..clients.clients import call
from ...console import USERBOT_PICTURE

from asyncio.queues import QueueEmpty
from pytgcalls.types import MediaStream
from pytgcalls.types import AudioQuality, VideoQuality
from youtubesearchpython.__future__ import VideosSearch


async def get_result(query: str):
    results = VideosSearch(query, limit=1)
    for result in (await results.next())["result"]:
        url = result["link"]
        try:
            thumbnail = result["thumbnails"][0]["url"].split("?")[0]
        except:
            thumbnail = USERBOT_PICTURE
        
    return url, thumbnail


async def run_stream(link, type):
    if type == "Audio":
        stream = MediaStream(
            media_path=link,
            video_flags=MediaStream.IGNORE,
            audio_parameters=AudioQuality.STUDIO,
        )

    elif type == "Video":
        stream = MediaStream(
            media_path=link,
            audio_parameters=AudioQuality.STUDIO,
            video_parameters=VideoQuality.HD_720p,
        )

    return stream


async def close_stream(chat_id):
    try:
        await queues.clear(chat_id)
    except QueueEmpty:
        pass
    try:
        return await call.leave_group_call(chat_id)
    except:
        pass
