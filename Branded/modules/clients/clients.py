import os, sys

from pyrogram import Client
from pyrogram import filters
from pytgcalls import PyTgCalls
from motor.motor_asyncio import AsyncIOMotorClient

from ...console import API_ID, API_HASH, STRING_SESSION
from ...console import BOT_TOKEN, SESSION_STRING, LOGGER
from ...console import MONGO_DB_URL, LOG_GROUP_ID, SUDOERS


def async_config():
    LOGGER.info("Checking Variables ...")
    if not API_ID:
        LOGGER.info("'API_ID' - Not Found !")
        sys.exit()
    if not API_HASH:
        LOGGER.info("'API_HASH' - Not Found !")
        sys.exit()
    if not BOT_TOKEN:
        LOGGER.info("'BOT_TOKEN' - Not Found !")
        sys.exit()
    if not STRING_SESSION:
        LOGGER.info("'STRING_SESSION' - Not Found !")
        sys.exit()
    if not MONGO_DB_URL:
        LOGGER.info("'MONGO_DB_URL' - Not Found !")
        sys.exit()
    if not LOG_GROUP_ID:
        LOGGER.info("'LOG_GROUP_ID' - Not Found !")
        sys.exit()
    LOGGER.info("All Required Variables Collected.")


def async_dirs():
    LOGGER.info("Initializing Directories ...")
    if "downloads" not in os.listdir():
        os.mkdir("downloads")
    if "cache" not in os.listdir():
        os.mkdir("cache")
    
    for file in os.listdir():
        if file.endswith(".session"):
            os.remove(file)
    for file in os.listdir():
        if file.endswith(".session-journal"):
            os.remove(file)
    LOGGER.info("Directories Initialized.")

async_dirs()
    

app = Client(
    name = "BRANDEDKING82",
    api_id = API_ID,
    api_hash = API_HASH,
    session_string = STRING_SESSION,
)

ass = Client(
    name = "BRANDEDKING82",
    api_id = API_ID,
    api_hash = API_HASH,
    session_string = SESSION_STRING,
)

bot = Client(
    name = "BRANDEDKING82",
    api_id = API_ID,
    api_hash = API_HASH,
    bot_token = BOT_TOKEN,
)


if not SESSION_STRING:
    call = PyTgCalls(app)
else:
    call = PyTgCalls(ass)


def mongodbase():
    global mongodb
    try:
        LOGGER.info("Connecting To Your Database ...")
        async_client = AsyncIOMotorClient
        mongobase = async_client(MONGO_DB_URL)
        mongodb = mongobase.AdityaHalder
        LOGGER.info("Conected To Your Database.")
    except:
        LOGGER.error("Failed To Connect, Please Change Your Mongo Database !")
        sys.exit()

mongodbase()


async def sudo_users():
    sudoersdb = mongodb.sudoers
    sudoers = await sudoersdb.find_one({"sudo": "sudo"})
    sudoers = [] if not sudoers else sudoers["sudoers"]
    if sudoers:
        for user_id in sudoers:
            SUDOERS.append(int(user_id))
    LOGGER.info(f"Sudo Users Loaded.")
    

async def run_async_clients():
    LOGGER.info("Starting Userbot ...")
    await app.start()
    LOGGER.info("Userbot Started.")
    try:
        await app.send_message(LOG_GROUP_ID, "**Userbot Started.**")
    except:
        pass
    try:
        await app.join_chat("BRANDED_PAID_CC")
        await app.join_chat("BRANDRD_BOT")
    except:
        pass
    if SESSION_STRING:
        LOGGER.info("Starting Assistant ...")
        await ass.start()
        LOGGER.info("Assistant Started.")
        try:
            await ass.send_message(LOG_GROUP_ID, "**Assistant Started.**")
        except:
            pass
        try:
            await app.join_chat("BRANDED_PAID_CC")
            await app.join_chat("BRANDRD_BOT")
        except:
            pass
    LOGGER.info("Starting Helper Robot ...")
    await bot.start()
    LOGGER.info("Helper Robot Started.")
    try:
        await bot.send_message(LOG_GROUP_ID, "**Helper Robot Started.**")
    except:
        pass
    LOGGER.info("Starting PyTgCalls Client...")
    await call.start()
    LOGGER.info("PyTgCalls Client Started.")
    await sudo_users()
    
    
