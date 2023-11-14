import asyncio

from .. import *
from ..modules.vars import all_vars
from ..modules.vars import all_vals


@app.on_message(commandx("vars") & SUPUSER)
async def all_vars_(client, message):
    await message.edit("**Please Wait ...**")
    await asyncio.sleep(1)
    await message.edit(f"{all_vars}")
    
@app.on_message(commandx("vals") & SUPUSER)
async def all_vals_(client, message):
    await message.edit("**Please Wait ...**")
    await asyncio.sleep(1)
    await message.edit(f"{all_vals}")



__NAME__ = "Vars"
__MENU__ = """**Get Your Userbot Variables**

`.vars` - Use This Command To
Get All Variable Names.

`.vals` - Use This Command To
Get All Variable Values.

**Note:** Don't Use This Command
in Any Public Groups.
"""
