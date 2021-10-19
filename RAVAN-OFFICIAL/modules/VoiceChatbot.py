# Voics Chatbot Module Credits Pranav Ajay 🐰Github = Red-Aura 🐹 Telegram= @madepranav
# @lyciachatbot support Now
import os
import aiofiles
import aiohttp
from random import randint
from pyrogram import filters
from RAVANOFFICIAL import pbot as RAVAN


async def fetch(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            try:
                data = await resp.json()
            except:
                data = await resp.text()
    return data


async def ai_RAVAN(url):
    ai_name = "RAVAN.mp3"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            if resp.status == 200:
                f = await aiofiles.open(ai_name, mode="wb")
                await f.write(await resp.read())
                await f.close()
    return ai_name


@Asuna.on_message(filters.command("voice"))
async def Asuna(_, message):
    if len(message.command) < 2:
        await message.reply_text("RAVAN AI Voice Chatbot")
        return
    text = message.text.split(None, 1)[1]
    Asuna = text.replace(" ", "%20")
    m = await message.reply_text("RAVAN Is Best...")
    try:
        L = await fetch(
            f"https://api.affiliateplus.xyz/api/chatbot?message={lycia}&botname=@My_Asuna_Robot&ownername=@The_Ghost_Hunter&user=1"
        )
        chatbot = L["message"]
        VoiceAi = f"https://lyciavoice.herokuapp.com/lycia?text={chatbot}&lang=hi"
        name = "RAVAN"
    except Exception as e:
        await m.edit(str(e))
        return
    await m.edit("Made By @D3VILRAVANXOP...")
    AsunaVoice = await ai_Asuna(VoiceAi)
    await m.edit("Repyping...")
    await message.reply_audio(audio=AsunaVoice, title=chatbot, performer=name)
    os.remove(AsunaVoice)
    await m.delete()
