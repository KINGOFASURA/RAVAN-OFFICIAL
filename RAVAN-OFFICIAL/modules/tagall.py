from .. import telethn
from telethon import events
import asyncio
Alain = telethn

#By @Alain_xD

"""
#@bot.on(events.NewMessage(pattern="[!/](tagall)$"))
async def _(event):
   k = event.text.split(" ", maxsplit=1)[1]
   if not event.text
   lel = 0
   lell = ""
   async for x in bot.iter_partcipants(event.chat_id):
    lell +=  f"[{x.first_name}](tg://user?id={x.id})"
    lel += 1
    if lel == 7:
     await bot.send_message(event.chat_id, f"{k}\n\n{lell}")
     asyncio.sleep(1)
     lell = ""
     lel = 0
     if not k:
      sed = await event.get_reply_message()
      no = sed.text
      if lel == 7:
       await bot.send_message(event.chat_id, f"{sed}\n\n{lell}")
       asyncio.sleep(1)
       lell = ""
       lel = 0
"""


@Alain.on(events.NewMessage(pattern="/tagall ?(.*)"))
async def _(event):
  admin = await event.client.get_permissions(event.chat_id, event.sender.id)
  if not admin.is_admin:
   return await event.reply("`Pehele admin to bano sor`")
  if not event.reply_to and not event.pattern_match.group(1):

      return await event.reply("**Eʀʀᴏʀ:**\n`Nᴏ ᴛᴇxᴛ ᴡᴀs ɢɪᴠᴇɴ!`")
  
  if not event.reply_to:
   sed = event.text.split(None, 1)[1]

   lel = 0

   lell = ""

   async for x in event.client.iter_participants(event.chat_id):

    lell +=  f"[{x.first_name}](tg://user?id={x.id}) **,**"

    lel += 1

    if lel == 5:

     await event.client.send_message(event.chat_id, f"{sed}\n\n{lell}")

     await asyncio.sleep(2)

     lell = ""

     lel = 0

    
  else:

     pro = await event.get_reply_message()

     ab = 0

     bc = ""

     async for y in event.client.iter_participants(event.chat_id):

      bc +=  f"[{y.first_name}](tg://user?id={y.id}) **,**"

      ab += 1

      if ab == 5:

       await event.client.send_message(event.chat_id, f"{pro.text}\n\n{bc}")

       await asyncio.sleep(2)

       bc = ""

       ab = 0
