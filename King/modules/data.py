from .core import mongodb
from typing import Dict, List, Union


sudoersdb = mongodb.sudoers
gdeldb = mongodb.gdel
lraiddb = mongodb.lraid
rraiddb = mongodb.rraid
permitdb = mongodb.pmprotection




# Sudo Users
async def get_sudoers() -> list:
    sudoers = await sudoersdb.find_one({"sudo": "sudo"})
    if not sudoers:
        return []
    return sudoers["sudoers"]


async def add_sudo(user_id: int) -> bool:
    sudoers = await get_sudoers()
    sudoers.append(user_id)
    await sudoersdb.update_one(
        {"sudo": "sudo"}, {"$set": {"sudoers": sudoers}}, upsert=True
    )
    return True


async def del_sudo(user_id: int) -> bool:
    sudoers = await get_sudoers()
    sudoers.remove(user_id)
    await sudoersdb.update_one(
        {"sudo": "sudo"}, {"$set": {"sudoers": sudoers}}, upsert=True
    )
    return True



# Global Delete
async def get_gdel_user() -> list:
    results = []
    async for user in gdeldb.find({"user_id": {"$gt": 0}}):
        user_id = user["user_id"]
        results.append(user_id)
    return results


async def get_gdel_count() -> int:
    users = gdeldb.find({"user_id": {"$gt": 0}})
    users = await users.to_list(length=100000)
    return len(users)


async def is_gdel_user(user_id: int) -> bool:
    user = await gdeldb.find_one({"user_id": user_id})
    if not user:
        return False
    return True


async def add_gdel_user(user_id: int):
    is_gdel = await is_gdel_user(user_id)
    if is_gdel:
        return
    return await gdeldb.insert_one({"user_id": user_id})


async def del_gdel_user(user_id: int):
    is_gdel = await is_gdel_user(user_id)
    if not is_gdel:
        return
    return await gdeldb.delete_one({"user_id": user_id})



# Love Raid
async def get_lraid_user() -> list:
    results = []
    async for user in lraiddb.find({"user_id": {"$gt": 0}}):
        user_id = user["user_id"]
        results.append(user_id)
    return results


async def get_lraid_count() -> int:
    users = lraiddb.find({"user_id": {"$gt": 0}})
    users = await users.to_list(length=100000)
    return len(users)


async def is_lraid_user(user_id: int) -> bool:
    user = await lraiddb.find_one({"user_id": user_id})
    if not user:
        return False
    return True


async def add_lraid_user(user_id: int):
    is_lraid = await is_lraid_user(user_id)
    if is_lraid:
        return
    return await lraiddb.insert_one({"user_id": user_id})


async def del_lraid_user(user_id: int):
    is_lraid = await is_lraid_user(user_id)
    if not is_lraid:
        return
    return await lraiddb.delete_one({"user_id": user_id})



# Reply Raid
async def get_rraid_user() -> list:
    results = []
    async for user in rraiddb.find({"user_id": {"$gt": 0}}):
        user_id = user["user_id"]
        results.append(user_id)
    return results


async def get_rraid_count() -> int:
    users = rraiddb.find({"user_id": {"$gt": 0}})
    users = await users.to_list(length=100000)
    return len(users)


async def is_rraid_user(user_id: int) -> bool:
    user = await rraiddb.find_one({"user_id": user_id})
    if not user:
        return False
    return True


async def add_rraid_user(user_id: int):
    is_rraid = await is_rraid_user(user_id)
    if is_rraid:
        return
    return await rraiddb.insert_one({"user_id": user_id})


async def del_rraid_user(user_id: int):
    is_rraid = await is_rraid_user(user_id)
    if not is_rraid:
        return
    return await rraiddb.delete_one({"user_id": user_id})








# PM Guard database

async def is_approved() -> list:
    pm = await permitdb.find_one({'permit': 'protection'})
    if not pm:
        return []
    return pm['users']


async def approve(user_ud: int):
    pm = await is_approved()
    pm.append(user_ud)
    await permitdb.update_one(
        {'permit': 'protection'},
        {
            '$set': {
                'users': pm
            }
        },
        upsert=True
    )


async def disapprove(user_ud: int):
    pm = await is_approved()
    pm.remove(user_ud)
    await permitdb.update_one(
        {'permit': 'protection'},
        {
            '$set': {
                'users': pm
            }
        },
        upsert=True
    )
