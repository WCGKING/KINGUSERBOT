import asyncio

from .. import *
from ..modules.vars import all_vars
from ..modules.vars import all_vals


@app.on_message(commandx("vars") & SUPUSER)
async def all_vars_(client, message):
    await message.edit("**Please Wait ...**")
    await asyncio.sleep(1)
    await message.edit(f"{all_vars}")
    
@app.on_message(commandx("vals") & SUPUSER)
async def all_vals_(client, message):
    await message.edit("**Please Wait ...**")
    await asyncio.sleep(1)
    await message.edit(f"{all_vals}")



__NAME__ = "✨ ᴠᴀʀꜱ 🌷"
__MENU__ = """**𝗚𝗘𝗧 𝗬𝗢𝗨𝗥 𝗨𝗦𝗘𝗥𝗕𝗢𝗧 𝗩𝗔𝗥𝗜𝗔𝗕𝗟𝗘𝗦**

`.vars` - 𝗨𝗦𝗘 𝗧𝗛𝗜𝗦 𝗖𝗢𝗠𝗠𝗔𝗡𝗗 𝗧𝗢
𝗚𝗘𝗧 𝗔𝗟𝗟 𝗩𝗔𝗥𝗜𝗔𝗕𝗟𝗘 𝗡𝗔𝗠𝗘𝗦.

`.vals` - 𝗨𝗦𝗘 𝗧𝗛𝗜𝗦 𝗖𝗢𝗠𝗠𝗔𝗡𝗗 𝗧𝗢
𝗚𝗘𝗧 𝗔𝗟𝗟 𝗩𝗔𝗥𝗜𝗔𝗕𝗟𝗘 𝗩𝗔𝗟𝗨𝗘𝗦.

**𝗡𝗢𝗧𝗘 🦋:** 𝗗𝗢𝗡'𝗧 𝗨𝗦𝗘 𝗧𝗛𝗜𝗦 𝗖𝗢𝗠𝗠𝗔𝗡𝗗
𝗜𝗡 𝗔𝗡𝗬𝗡𝗣𝗨𝗕𝗟𝗜𝗖 𝗚𝗥𝗢𝗨𝗣𝗦.
"""
