from .. import *
from datetime import datetime


@app.on_message(commandx(["ping"]) & SUDOERS)
async def alive_check(client, message):
    start = datetime.now()
    m = await eor(message, "**🤖 Pong !**")
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    await m.edit(f"**🤖 Pinged !\nLatency:** `{ms}` ms")


__NAME__ = "✨ ᴘɪɴɢ 🌷"
__MENU__ = f"""
**🥀𝗖𝗛𝗘𝗖𝗞 𝗨𝗦𝗘𝗥𝗕𝗢𝗧 𝗦𝗘𝗥𝗩𝗘𝗥
𝗣𝗜𝗡𝗚 𝗟𝗔𝗧𝗘𝗡𝗖𝗬 ✨...**

**Example:** `.ping`
"""
