import os

from .console import LOGGER
from .modules.core import Daxx
from .modules.vars import Config
from .modules.utils import commandx
from .modules.utils import commandz

__version__ = "v2.0.1"

if Config.API_ID == 0:
    LOGGER.error("API_ID is missing! Kindly check again!")
    exit()
if not Config.API_HASH:
    LOGGER.error("API_HASH is missing! Kindly check again!")
    exit()
if not Config.BOT_TOKEN:
    LOGGER.error("BOT_TOKEN is missing! Kindly check again!")
    exit()
if not Config.STRING_SESSION:
    LOGGER.error("STRING_SESSION is missing! Kindly check again!")
    exit()
if not Config.MONGO_DATABASE:
    LOGGER.error("DATABASE_URL is missing! Kindly check again!")
    exit()
if Config.LOG_GROUP_ID == 0:
    LOGGER.error("LOG_GROUP_ID is missing! Kindly check again!")
    exit()

for file in os.listdir():
    if file.endswith(".session"):
        os.remove(file)
for file in os.listdir():
    if file.endswith(".session-journal"):
        os.remove(file)


Daxx = Daxx()
app = Daxx.app
bot = Daxx.bot
call = Daxx.call
log = LOGGER
var = Config()

db = {}
flood = {}
OLD_MSG = {}

commandx = commandx
commandz = commandz

PLUGINS = var.PLUGINS
SUPUSER = var.SUPUSER
SUDOERS = var.SUDOERS
GDELSUB = var.GDELSUB


from .modules.func import eor
eor = eor

from .modules.misc import sudo_user_only
sudo_user_only = sudo_user_only
