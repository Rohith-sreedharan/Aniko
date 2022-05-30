from plugins.buttons import help_text, help_markup, devs_markup, suppot_markup
from http.client import EXPECTATION_FAILED
from aniko import Aniko
from matplotlib.image import thumbnail
from pyrogram import Client, filters
from pyrogram.types import (
    Message, InlineKeyboardMarkup,
    InlineKeyboardButton
)
from pyrogram.errors import *
from config import BaseConfig

@Client.on_message(filters.command("help")&filters.private)
async def help_message(client: Client, message: Message):
    if update_channel := BaseConfig.UPDATES_CHANNEL:
        try:
            user = await client.get_chat_member(update_channel, client.chat.id)
            if user.status == "kicked":
               await client.send_message(
                   chat_id=message.chat.id,
                   text="Sorry Sir, You are Banned to use me. Contact my [Support Group](https://t.me/Bots_Universe).",
                   parse_mode="markdown",
                   disable_web_page_preview=True
               )
               return
        except UserNotParticipant:
            await client.send_message(
                chat_id=message.chat.id,
                text="**Please Join My Updates Channel to use this Bot!**",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("Join Updates Channel", url=BaseConfig.CHNL_URL)
                        ]
                    ]
                ),
                parse_mode="markdown"
            )
            return
        except Exception as e:
            await client.send_message(
                chat_id= message.chat.id,
                text=f"Something went Wrong. Contact my [Support Group](https://t.me/Bots_Universe).\nError: {e}",
                parse_mode="markdown",
                disable_web_page_preview=True)
            return

    msg = await message.reply_text('Processing.....'),
    vaop = f'''
Hello User {message.from_user.first_name},
Avaliable Commands Are
1. /search <anime name> - Search Anime
2. /dl <anime name> <episode number> - Download Anime
3. /help - Show this message
4. /get <anime name> - Get anime name
5. /random - To Get Recommendations Based on Genere
6. /shorts <anime name> - To View The Summary Of Anime Show
7. /start - To Restart The Bot
8. /onair - To View The Anime Currently On Air
Click Button Down To Know More
'''
    await msg.edit_text(
        vaop,
        reply_markup=help_markup,
        parse_mode="markdown"
    )
    return
