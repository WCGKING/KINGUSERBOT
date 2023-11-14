from .. import *

@app.on_message(commandx(["alive"]))
async def alive_check(client, message):
    await message.reply_text("**🥀 𝗜 𝗔𝗠 𝗔𝗟𝗜𝗩𝗘 𝗠𝗬 𝗗𝗘𝗔𝗥 𝗕𝗥𝗔𝗡𝗗𝗘𝗗 𝗞𝗜𝗡𝗚 𝗠𝗔𝗦𝗧𝗘𝗥✨ ...**")



__NAME__ = "✨ Alive 🌷"
__MENU__ = f"""
**🥀 Check Userbot Working
Or Not ..**

**Example:** `.alive`
"""
