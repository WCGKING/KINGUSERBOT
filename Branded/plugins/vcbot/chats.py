from ... import *
from ...modules.mongo.streams import *


@app.on_message(cdx(["cset", "schat", "setchat"]))
@sudo_users_only
async def set_stream_chat(client, message):
    aux = await eor(message, "**Processing ...**")
    user_id = message.from_user.id
    if len(message.command) < 2:
        chat_id = message.chat.id
    else:
        try:
            chat_id = message.text.split(None, 1)[1]
            if "@" in chat_id:
                chat_id = chat_id.replace("@", "")
                chat = await app.get_chat(chat_id)
                chat_id = chat.id
        except:
            return await aux.edit("**Error !**")
    if len(str(chat_id)) != 14:
        return await aux.edit("Give Me Correct Chat ID !")
    try:
        add_chat = await set_chat_id(user_id, int(chat_id))
        if add_chat:
            return await aux.edit("Already Set.")
        return await aux.edit("Chat ID Added.")
    except Exception as e:
        await aux.delete()
        print(f"Error: `{e}`")

  
