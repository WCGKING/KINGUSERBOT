from pyrogram import filters
from pyrogram.errors import FloodWait

from .. import *
from ..modules.data import is_gdel_user



@app.on_message(filters.incoming, group=2)
async def actions_checker(client, message):
    user_id = message.from_user.id
    if await is_gdel_user(user_id):
        try:
            await message.delete()
        except FloodWait as e:
            await asyncio.sleep(e.value)
        except Exception:
            pass

      
