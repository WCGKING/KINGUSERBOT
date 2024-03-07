from typing import Dict, List, Union

from ... import console as vars
from ..clients.clients import mongodb


chatraiddb = mongodb.chatraiddb
fuckraiddb = mongodb.fuckraiddb
loveraiddb = mongodb.loveraiddb



# ChatRaid Users Database

async def is_chatraid_user(user_id: int) -> bool:
    user = await chatraiddb.find_one({"user_id": user_id})
    if not user:
        return False
    return True


async def add_chatraid_user(user_id: int) -> bool:
    is_chatraid = await is_chatraid_user(user_id)
    if is_chatraid:
        return False
    await chatraiddb.insert_one({"user_id": user_id})
    return True


async def del_chatraid_user(user_id: int) -> bool:
    is_chatraid = await is_chatraid_user(user_id)
    if not is_chatraid:
        return False
    await chatraiddb.delete_one({"user_id": user_id})
    return True




# FuckRaid Users Database

async def is_fuckraid_user(user_id: int) -> bool:
    user = await fuckraiddb.find_one({"user_id": user_id})
    if not user:
        return False
    return True


async def add_fuckraid_user(user_id: int) -> bool:
    is_fuckraid = await is_fuckraid_user(user_id)
    if is_fuckraid:
        return False
    await fuckraiddb.insert_one({"user_id": user_id})
    return True


async def del_fuckraid_user(user_id: int) -> bool:
    is_fuckraid = await is_fuckraid_user(user_id)
    if not is_fuckraid:
        return False
    await fuckraiddb.delete_one({"user_id": user_id})
    return True



# LoveRaid Users Database

async def is_loveraid_user(user_id: int) -> bool:
    user = await loveraiddb.find_one({"user_id": user_id})
    if not user:
        return False
    return True


async def add_loveraid_user(user_id: int) -> bool:
    is_loveraid = await is_loveraid_user(user_id)
    if is_loveraid:
        return False
    await loveraiddb.insert_one({"user_id": user_id})
    return True


async def del_loveraid_user(user_id: int) -> bool:
    is_loveraid = await is_loveraid_user(user_id)
    if not is_loveraid:
        return False
    await loveraiddb.delete_one({"user_id": user_id})
    return True

