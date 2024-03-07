from ... import console
from pyrogram import filters
from typing import Union, List


def commandx(commands: Union[str, List[str]]):
    return filters.command(commands, console.COMMAND_PREFIXES)

def commandz(commands: Union[str, List[str]]):
    return filters.command(commands, console.COMMAND_HANDLERS)
