from pytgcalls.types import Update

from . import queues
from ..clients.clients import app, call
from .streams import run_stream, close_stream


async def run_async_calls():
    @call.on_left()
    @call.on_kicked()
    @call.on_closed_voice_chat()
    async def stream_services_handler(_, chat_id: int):
        return await close_stream(chat_id)
    
    
    @call.on_stream_end()
    async def stream_end_handler(_, update: Update):
        chat_id = update.chat_id
        queues.task_done(chat_id)
        if queues.is_empty(chat_id):
            return await close_stream(chat_id)
        check = queues.get(chat_id)
        file = check["file"]
        type = check["type"]
        stream = await run_stream(file, type)
        return await call.change_stream(chat_id, stream)
    
        
