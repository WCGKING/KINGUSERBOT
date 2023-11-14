from .. import *
from datetime import datetime


@app.on_message(commandx(["ping"]) & SUDOERS)
async def alive_check(client, message):
    start = datetime.now()
    m = await eor(message, "**🤖 Pong !**")
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    await m.edit(f"**🤖 Pinged !\nLatency:** `{ms}` ms")


__NAME__ = "Ping"
__MENU__ = f"""
**🥀 Check Userbot Server
Ping Latency ✨...**

**Example:** `.ping`
"""
