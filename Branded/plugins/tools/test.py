from ... import *
from datetime import datetime

@app.on_message(cdx("status"))
@sudo_users_only
async def get_call_stats(client, message):
    chat_id = message.chat.id
    calls = await call.calls
    chat_call = calls.get(chat_id)
    if chat_call:
        call_status = chat_call.status
        print(call_status)
    # await m.edit(f"**🤖 Pinged !\nLatency:** `{ms}` ms")



__NAME__ = "status"
__MENU__ = """
`.ping` - **Check call status
Of Your Userbot Server.**
"""
