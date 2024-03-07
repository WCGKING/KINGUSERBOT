import asyncio, random

from pyrogram import filters
from pyrogram.enums import *
from pyrogram.types import *

from .clients import app, bot
from ..mongo.pmguard import *
from ..mongo.raidzone import *
from ..strings import raidzone
from ... import console as vars


async def run_async_enums():
    @app.on_message(
        (
            filters.private
            & filters.incoming
            & ~filters.service
            & ~filters.me
            & ~filters.bot
            & ~filters.via_bot
        )
    )
    async def all_events(client, message):
        check = vars.OLD_MSG
        flood = vars.FLOODXD
        user_id = message.from_user.id
        pm_permit = await get_pm_permit()
        permit_image = await get_pm_image()
        permit_text = await get_pm_text()
        if pm_permit:
            if not await is_approved_user(user_id):
                limits = await get_pm_limit()
                async for m in client.get_chat_history(user_id, limit=limits):
                    if m.reply_markup:
                        await m.delete()
                if str(user_id) in flood:
                    flood[str(user_id)] += 1
                else:
                    flood[str(user_id)] = 1
                if flood[str(user_id)] > limits:
                    await message.reply_text("Spammer Detected!\nAutomatic Blocking User!!!")
                    if str(user_id) in check:
                        check.pop(str(user_id))
                        flood.update({user_id: 0})
                    return await client.block_user(user_id)
                pm_security = "**🤖 SECURITY WARNING ‼️ ({}/{})**".format(flood[str(user_id)], limits)
                pm_permit_text = pm_security + "\n\n" + permit_text
                try:
                    msg_dlt = await message.reply_photo(
                        photo=permit_image,
                        caption=pm_permit_text,
                    )
                except Exception:
                    msg_dlt = await message.reply_text(pm_permit_text)
                if str(user_id) in check:
                    try:
                        await check[str(user_id)].delete()
                    except BaseException:
                        pass
                check[str(user_id)] = msg_dlt


    @app.on_message(
        (
            filters.incoming
            & ~filters.service
            & ~filters.me
            & ~filters.bot
            & ~filters.via_bot
        ),
        group=1
    )
    async def run_all_events(client, message):
        try:
            chat_id = message.chat.id
            user_id = message.from_user.id
            cruser = await is_chatraid_user(user_id)
            lruser = await is_loveraid_user(user_id)
            fruser = await is_fuckraid_user(user_id)
        except Exception as e:
            print(f"Error: {e}")
            return

        if cruser:
            pass
        if lruser:
            lraid = random.choice(raidzone.LOVERAID)
            try:
                await app.send_chat_action(
                    chat_id,
                    ChatAction.TYPING,
                )
                await asyncio.sleep(3)
                await message.reply_text(lraid)
            except Exception as e:
                # print(f"Error: {e}")
                pass
        if fruser:
            fraid = random.choice(raidzone.GALIRAID)
            try:
                await app.send_chat_action(
                    chat_id,
                    ChatAction.TYPING,
                )
                await asyncio.sleep(3)
                await message.reply_text(fraid)
            except Exception as e:
                # print(f"Error: {e}")
                pass





