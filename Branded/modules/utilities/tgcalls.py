from pytgcalls import filters
from pytgcalls.types import ChatUpdate, Update

from . import queues
from ..clients.clients import app, call
from .streams import run_stream, close_stream


async def run_async_calls():
    @call.on_update(
        filters.chat_update(
            ChatUpdate.Status.CLOSED_VOICE_CHAT
        )
    )
    @call.on_update(
        filters.chat_update(
            ChatUpdate.Status.KICKED | ChatUpdate.Status.LEFT_GROUP,
        ),
    )
    async def stream_services_handler(_, update: Update):
        return await close_stream(update.chat_id)
    
    
    @call.on_update(filters.stream_end)
    async def stream_end_handler(_, update: Update):
        chat_id = update.chat_id
        queues.task_done(chat_id)
        if queues.is_empty(chat_id):
            return await close_stream(chat_id)
        check = queues.get(chat_id)
        file = check["file"]
        type = check["type"]
        stream = await run_stream(file, type)
        return await call.play(chat_id, stream)
    
        
