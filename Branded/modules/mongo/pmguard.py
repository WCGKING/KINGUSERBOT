from typing import Dict, List, Union

from ... import console as vars
from ..clients.clients import mongodb


pmguarddb = mongodb.pmguarddb
pmallowdb = mongodb.pmallowdb
pmimagedb = mongodb.pmimagedb
pmtextsdb = mongodb.pmtextsdb
pmlimitdb = mongodb.pmlimitdb


# PM Permit On/Off
async def get_pm_permit() -> bool:
    pm_permit = await pmguarddb.find_one()
    if not pm_permit:
        return vars.PM_GUARD
    get_permit = pm_permit["pm_permit"]
    return get_permit


async def set_pm_permit(permit: bool) -> bool:
    get_permit = await get_pm_permit()
    if permit == get_permit:
        return False
    await pmguarddb.update_one(
        {"pm_permit": get_permit},
        {"$set": {"pm_permit": permit}},
        upsert=True,
    )
    return True



# approved Users Database

async def is_approved_user(user_id: int) -> bool:
    user = await pmallowdb.find_one({"user_id": user_id})
    if not user:
        return False
    return True


async def add_approved_user(user_id: int) -> bool:
    is_approved = await is_approved_user(user_id)
    if is_approved:
        return False
    await pmallowdb.insert_one({"user_id": user_id})
    return True


async def del_approved_user(user_id: int) -> bool:
    is_approved = await is_approved_user(user_id)
    if not is_approved:
        return False
    await pmallowdb.delete_one({"user_id": user_id})
    return True


async def get_approved_users() -> list:
    approved_users_list = []
    async for user in pmallowdb.find({"user_id": {"$gt": 0}}):
        approved_users_list.append(user)
    return users_list


# PM Image
async def get_pm_image() -> str:
    image = await pmimagedb.find_one()
    if not image:
        return vars.USERBOT_PICTURE
    get_image = image["pm_image"]
    return get_image


async def set_pm_image(text: str) -> bool:
    get_image = await get_pm_image()
    await pmimagedb.update_one(
        {"pm_image": get_image},
        {"$set": {"pm_image": text}},
        upsert=True,
    )
    return True


# PM Text
async def get_pm_text() -> str:
    dm_text = await pmtextsdb.find_one()
    if not dm_text:
        return vars.PM_GUARD_TEXT
    get_text = dm_text["pm_text"]
    return get_text


async def set_pm_text(text: str) -> bool:
    get_text = await get_pm_text()
    await pmtextsdb.update_one(
        {"pm_text": get_text},
        {"$set": {"pm_text": text}},
        upsert=True,
    )
    return True



# PM Limit
async def get_pm_limit() -> int:
    limit = await pmlimitdb.find_one()
    if not limit:
        return vars.PM_GUARD_LIMIT
    get_limit = limit["pm_limit"]
    return get_image


async def set_pm_limit(number: int) -> bool:
    get_limit = await get_pm_limit()
    await pmlimitdb.update_one(
        {"pm_limit": get_limit},
        {"$set": {"pm_limit": number}},
        upsert=True,
    )
    return True

