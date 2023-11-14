import asyncio

from pyrogram import Client
from pyrogram.types import ChatPrivileges
from pytgcalls import PyTgCalls
from motor.motor_asyncio import AsyncIOMotorClient

from .vars import Config
from ..console import LOGGER

ass_power = ChatPrivileges(
    can_change_info=True,
    can_delete_messages=True,
    can_restrict_members=True,
    can_pin_messages=True,
    can_manage_video_chats=True,
    can_promote_members=True,    
    can_invite_users=True
)

bot_power = ChatPrivileges(
    can_change_info=True,
    can_delete_messages=True,
    can_restrict_members=True,
    can_pin_messages=True,
    can_manage_video_chats=True,
    can_promote_members=True,    
    can_invite_users=True
)

try:
    LOGGER.info("Connecting To Mongo Database ...")
    MONGO_DB_URL = Config.MONGO_DATABASE
    _mongo_async_ = AsyncIOMotorClient(MONGO_DB_URL)
    mongodb = _mongo_async_.Daxx
    LOGGER.info("Succesfully Connected.")
except Exception as e:
    print(f"Error: {e}")
    LOGGER.error("Failed To Connect To Your Mongo Database.")
    exit()

class Daxx(Client, PyTgCalls):
    def __init__(self):
        self.app = Client(
            name = "Daxx",
            api_id = Config.API_ID,
            api_hash = Config.API_HASH,
            session_string = Config.STRING_SESSION,
        )
        self.ass = Client(
            name = "Daxx",
            api_id = Config.API_ID,
            api_hash = Config.API_HASH,
            session_string = Config.SESSION_STRING,
        )
        self.bot = Client(
            name = "iam_daxx",
            api_id = Config.API_ID,
            api_hash = Config.API_HASH,
            bot_token = Config.BOT_TOKEN,
        )
        if Config.SESSION_STRING:
            self.call = PyTgCalls(self.ass)
        else:
            self.call = PyTgCalls(self.app)
  

    
    async def start(self):
        LOGGER.info("Starting Userbot")
        await self.app.start()
        self.app.name = self.app.me.first_name + "" + (self.app.me.last_name or "")
        self.app.username = self.app.me.username if self.app.me.username else self.app.me.mention
        self.app.mention = self.app.me.mention
        self.app.id = self.app.me.id
        if self.app.id not in Config.SUDOERS:
            Config.SUDOERS.add(int(self.app.id))
        try:
            await self.app.join_chat("HEROKUFREECC")
            await self.app.join_chat("HEROKUFREECC")
            await self.app.join_chat("HEROKUFREECC")
        except:
            pass
        await self.app.send_message(Config.LOG_GROUP_ID, "**Userbot Started**")
        LOGGER.info(f"Userbot Started as {self.app.name}")
        LOGGER.info("Starting PyTgCalls")
        if Config.SESSION_STRING:
            await self.ass.start()
            self.ass.name = self.ass.me.first_name + "" + (self.ass.me.last_name or "")
            self.ass.username = self.ass.me.username
            self.ass.mention = self.ass.me.mention
            self.ass.id = self.ass.me.id
            try:
                await self.ass.join_chat("HEROKUFREECC")
                await self.ass.join_chat("HEROKUFREECC")
                await self.ass.join_chat("HEROKUFREECC")
            except:
                pass
            try:
                await self.ass.send_message(Config.LOG_GROUP_ID, "**Vc Assistant Started.**")
            except:
                pass
            LOGGER.info(f"Vc Assistant Started as {self.ass.name}")
        await self.call.start()
        LOGGER.info("Starting Helperbot")
        await self.bot.start()
        self.bot.name = self.bot.me.first_name + "" + (self.bot.me.last_name or "")
        self.bot.username = self.bot.me.username
        self.bot.mention = self.bot.me.mention
        self.bot.id = self.bot.me.id
        try:
            await self.app.send_message(f"@{self.bot.username}", "/start")
            await self.app.promote_chat_member(Config.LOG_GROUP_ID, self.bot.id, bot_power)
        except Exception as e:
            LOGGER.info(e)
            pass
        try:
            await asyncio.sleep(1)
            await self.app.send_message(f"@botfather", "/setinline")
            await asyncio.sleep(1)
            await self.app.send_message(f"@botfather", f"@{self.bot.username}")
            await asyncio.sleep(1)
            await self.app.send_message(f"@botfather", "🥀 𝐃𝐚𝐱𝐱 𝐔𝐬𝐞𝐫𝐁𝐨𝐭 ✨")
        except:
            pass
        try:
            await self.bot.send_message(Config.LOG_GROUP_ID, "**Helper Bot Started.**")
        except:
            LOGGER.error("Please Promote Bot in Your Log Group")
            exit()
        LOGGER.info(f"Helperbot Started as {self.bot.name}")
        if self.app.id not in Config.SUDOERS:
            Config.SUDOERS.add(int(self.app.id))
        sudoersdb = mongodb.sudoers
        sudoers = await sudoersdb.find_one({"sudo": "sudo"})
        sudoers = [] if not sudoers else sudoers["sudoers"]
        if self.app.id not in sudoers:
            sudoers.append(self.app.id)
            await sudoersdb.update_one(
                {"sudo": "sudo"},
                {"$set": {"sudoers": sudoers}},
                upsert=True,
            )
        if sudoers:
            for user_id in sudoers:
                if user_id not in Config.SUDOERS:
                    Config.SUDOERS.add(user_id)
        LOGGER.info(f"All Sudoers Loaded.")
        

