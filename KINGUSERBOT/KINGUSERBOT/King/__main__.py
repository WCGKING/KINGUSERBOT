import asyncio
import importlib

from pytgcalls import idle

from . import Daxx as client
from .import PLUGINS, log
from .plugins import ALL_PLUGINS


loop = asyncio.get_event_loop()

async def aditya():
    await client.start()
    log.info("Importing all plugins ...")
    for all_plugin in ALL_PLUGINS:
        imported_plugin = importlib.import_module(
            "Daxx.plugins." + all_plugin)
        if (hasattr(imported_plugin, "__NAME__"
           ) and imported_plugin.__NAME__):
            imported_plugin.__NAME__ = imported_plugin.__NAME__
            if (hasattr(imported_plugin, "__MENU__"
                ) and imported_plugin.__MENU__):
                PLUGINS[imported_plugin.__NAME__.lower()
                ] = imported_plugin
        log.info(f">> Importing: {all_plugin}.py")
    log.info(">> Successfully Imported All Plugins.")
    await asyncio.sleep(1)
    log.info("Userbot is Now Ready to Use !")
    await idle()

if __name__ == "__main__":
    loop.run_until_complete(aditya())
    log.info("Userbot Has Been Stopped !")
