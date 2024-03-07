# Ai-Userbot Version
__version__ = "v2.1.0"


# All Clients
from .modules.clients.clients import (
    app, bot, call
)
app = app
bot = bot
call = call


# Command Handlers
from .modules.helpers.filters import (
    commandx, commandz
)
cdx = commandx
cdz = commandz


# Edit Or Reply
from .modules.helpers.events import (
    edit_or_reply
)
eor = edit_or_reply


# Logger
from .console import LOGGER
logs = LOGGER


# Plugins
from .console import PLUGINS
plugs = PLUGINS


# Variables
from . import console as config
vars = config


# Decorators
from .modules.helpers.wrapper import (
    super_user_only, sudo_users_only
)
super_user_only = super_user_only
sudo_users_only = sudo_users_only

