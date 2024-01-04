

import os
import sys
import asyncio
import re
from random import choice
from config import (bot, HNDLR, SUDO_USERS, LOGS_CHANNEL)
from pyrogram import Client, filters
from pyrogram.types import Message
from Modules.helpers.data import *


usage = f"** ❌ Wrong Usage ❌** \n Type `{HNDLR}help spam`"


@Client.on_message(filters.user(SUDO_USERS) & filters.command(["delayspam"], prefixes=HNDLR))
@Client.on_message(filters.me & filters.command(["delayspam"], prefixes=HNDLR))
async def delayspam(xspam: Client, e: Message): 
    Kaal = "".join(e.text.split(maxsplit=1)[1:]).split(" ", 2)
    Kaalop = Kaal[1:]
    if len(Kaalop) == 2:
       counts = int(Kaalop[0])
       if int(e.chat.id) in GROUP:
            return await e.reply_text("**Sorry !! i Can't Spam Here.**")
       msg = str(Kaalop[1])
       if re.search(Owners.lower(), msg.lower()):
            return await e.reply_text(usage)("**Sorry !!** I can't Spam On @kaalxsupport owner")
       sleeptime = float(Kaal[0])
       if e.reply_to_message:
          reply_to_id = e.reply_to_message.message_id
          for _ in range(counts):
              await xspam.send_message(e.chat.id, msg, reply_to_message_id=reply_to_id)
              await asyncio.sleep(sleeptime)
          return
       for _ in range(counts):
           await xspam.send_message(e.chat.id, msg)
           await asyncio.sleep(sleeptime)
    else:
        await e.reply_text(usage)   
    if LOGS_CHANNEL:
         try:
             await xspam.send_message(LOGS_CHANNEL, f"started Delay Spam By User: {e.from_user.id} \n\n Chat: {e.chat.id} \n Counts: {counts} \n Spam Message: {msg} \n Delay Time: {sleeptime}")
         except Exception as a:
             print(a)
             pass




@Client.on_message(filters.user(SUDO_USERS) & filters.command(["pornspam"], prefixes=HNDLR))
@Client.on_message(filters.me & filters.command(["pornspam"], prefixes=HNDLR))
async def pornspam(xspam: Client, e: Message): 
    counts = e.command[1]
    if not counts:
        return await e.reply_text(usage)
    if int(e.chat.id) in GROUP:
         return await e.reply_text("**Sorry !! i Can't Spam Here.**")
    kaal = "**#Pornspam**"
    count = int(counts)
    for _ in range(count):
         prn = choice(PORM)
         if ".jpg" in prn or ".png" in prn:
              await xspam.send_photo(e.chat.id, prn, caption=kaal)
              await asyncio.sleep(0.4)
         if ".mp4" in prn or ".MP4," in prn:
              await xspam.send_video(e.chat.id, prn, caption=kaal)
              await asyncio.sleep(0.4)
    if LOGS_CHANNEL:
         try:
            await xspam.send_message(LOGS_CHANNEL, f"started Porn Spam By User: {e.from_user.id} \n Chat: {e.chat.id} \n Counts: {count}")
         except Exception as a:
             print(a)
             pass


@Client.on_message(filters.user(SUDO_USERS) & filters.command(["raid"], prefixes=HNDLR))
@Client.on_message(filters.me & filters.command(["raid"], prefixes=HNDLR))
async def raid(xspam: Client, e: Message):  
      Kaal = "".join(e.text.split(maxsplit=1)[1:]).split(" ", 2)
      if len(Kaal) == 2:
          counts = int(Kaal[0])
          if int(e.chat.id) in GROUP:
               return await e.reply_text("**Sorry !! i Can't Spam Here.**")
          ok = await xspam.get_users(Kaal[1])
          id = ok.id
          if int(id) in KAALX:
                text = f"I can't raid on @kaalxsupport Owner"
                await e.reply_text(text)
          elif int(id) in SUDO_USERS:
                text = f"This guy is a sudo user."
                await e.reply_text(text)
          else:
              fname = ok.first_name
              mention = f"[{fname}](tg://user?id={id})"
              for _ in range(counts):
                    reply = choice(RAID)
                    msg = f"{mention} {reply}"
                    await xspam.send_message(e.chat.id, msg)
                    await asyncio.sleep(0.10)
      elif e.reply_to_message:
          #msg_id = e.reply_to_message.message_id
          counts = int(Kaal[0])
          if int(e.chat.id) in GROUP:
               return await e.reply_text("**Sorry !! i Can't Spam Here.**")
          #Kaal = xspam.get_messages(e.chat.id, msg_id)
          user_id = e.reply_to_message.from_user.id
          ok = await xspam.get_users(user_id)
          id = ok.id
          if int(id) in KAALX:
                text = f"I can't raid on @kaalxsupport Owner"
                await e.reply_text(text)
          elif int(id) in SUDO_USERS:
                text = f"This guy is a sudo user."
                await e.reply_text(text)
          else:
              fname = ok.first_name
              mention = f"[{fname}](tg://user?id={id})"
              for _ in range(counts):
                    reply = choice(RAID)
                    msg = f"{mention} {reply}"
                    await xspam.send_message(e.chat.id, msg)
                    await asyncio.sleep(0.10)
      else:
          await e.reply_text(usage)
      if LOGS_CHANNEL:
         try:
            await xspam.send_message(LOGS_CHANNEL, f"started Raid By User: {e.from_user.id} \n\n On User: {mention} \n Chat: {e.chat.id} \n Counts: {counts}")
         except Exception as a:
             print(a)
             pass


@Client.on_message(filters.user(SUDO_USERS) & filters.command(["fspam", "fastspam", "spam", "bigspam"], prefixes=HNDLR))
@Client.on_message(filters.me & filters.command(["fspam", "fastspam", "spam", "bigspam"], prefixes=HNDLR))
async def fastspam(xspam: Client, e: Message):
    Kaal = "".join(e.text.split(maxsplit=1)[1:]).split(" ", 1)
    if len(Kaal) == 2:
       counts = int(Kaal[0])
       if int(e.chat.id) in GROUP:
            return await e.reply_text("**Sorry !! i Can't Spam Here.**")
       msg = str(Kaal[1])
       if e.reply_to_message:
          reply_to_id = e.reply_to_message.message_id
          for _ in range(counts):
              await xspam.send_message(e.chat.id, msg, reply_to_message_id=reply_to_id)
              await asyncio.sleep(0.002)
          return
       for _ in range(counts):
           await xspam.send_message(e.chat.id, msg)
           await asyncio.sleep(0.002)
    else:
        await e.reply_text(usage)
    if LOGS_CHANNEL:
         try:
            await xspam.send_message(LOGS_CHANNEL, f"started Spam By User: {e.from_user.id} \n\n Chat: {e.chat.id} \n Counts: {counts} \n Spam Message: {msg}")
         except Exception as a:
             print(a)
             pass

__NAME__ = "✨ Spam 🌷"
