import os

from .. import *
from pyrogram import filters


@app.on_message(commandz(["😋🥰", "op", "wow", "super", "😋😍"])
    & filters.private & filters.me)
async def self_media(client, message):
    replied = message.reply_to_message
    if not replied:
        return
    if not (replied.photo or replied.video):
        return
    location = await client.download_media(replied)
    await client.send_document("me", location)
    os.remove(location)


__NAME__ = "✨ ꜱᴇʟꜰ 🌷"
__MENU__ = f"""
**🥀 𝗗𝗢𝗪𝗡𝗟𝗢𝗔𝗗 𝗔𝗡𝗗 𝗦𝗔𝗩𝗘 𝗦𝗘𝗟𝗙\n» 𝗗𝗘𝗦𝗧𝗥𝗨𝗖𝗧𝗘𝗗 𝗣𝗛𝗢𝗧𝗢 𝗢𝗥 𝗩𝗜𝗗𝗘𝗢 
𝗧𝗢 𝗬𝗢𝗨𝗥 𝗦𝗔𝗩𝗘𝗗 𝗠𝗘𝗦𝗦𝗔𝗚𝗘 ✨**

`.op` - 𝗨𝗦𝗘 𝗧𝗛𝗜𝗦 𝗖𝗢𝗠𝗠𝗔𝗡𝗗 𝗕𝗬\n𝗥𝗘𝗣𝗟𝗬𝗜𝗡𝗚 𝗢𝗡 𝗦𝗘𝗟𝗙-𝗗𝗘𝗦𝗧𝗥𝗨𝗖𝗧𝗘𝗗
𝗣𝗛𝗢𝗧𝗢/𝗩𝗜𝗗𝗘𝗢.

**🌿 𝗠𝗢𝗥𝗘 𝗖𝗢𝗠𝗠𝗔𝗡𝗗𝗦:**\n=> [😋🥰, wow, super, 😋😍]
"""
