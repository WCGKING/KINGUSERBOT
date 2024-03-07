import asyncio, importlib

from pytgcalls import idle

from . import logs, plugs, vars
from .plugins import ALL_PLUGINS
from .modules.clients.clients import run_async_clients
from .modules.clients.enums import run_async_enums
from .modules.helpers.inline import run_async_inline
from .modules.utilities.tgcalls import run_async_calls


async def main():
    await run_async_clients()
    for all_plugin in ALL_PLUGINS:
        imported_plugin = importlib.import_module(
            "Branded.plugins" + all_plugin
        )
        if (hasattr
            (
                imported_plugin, "__NAME__"
            ) and imported_plugin.__NAME__
        ):
            imported_plugin.__NAME__ = imported_plugin.__NAME__
            if (
                hasattr(
                    imported_plugin, "__MENU__"
                ) and imported_plugin.__MENU__
            ):
                plugs[imported_plugin.__NAME__.lower()
                ] = imported_plugin
    await run_async_enums()
    logs.info(">> Successfully Imported All Plugins.")
    await run_async_inline()
    logs.info("Successfully Deployed !!")
    await run_async_calls()
    logs.info("Do Visit - @BRANDED_PAID_CC")
    await idle()


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    print("Userbot Stopped !\nGoodBye ...")
