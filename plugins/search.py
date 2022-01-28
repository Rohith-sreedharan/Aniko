from http.client import EXPECTATION_FAILED
from aniko import Aniko
from matplotlib.image import thumbnail
from pyrogram import Client, filters
from pyrogram.types import (
    Message, InlineKeyboardMarkup,
    InlineKeyboardButton
)
from aniko.error_handlers import *
import datetime
import time
from datetime import *
import os
from config import BaseConfig
# from bot import Rohith
from pyrogram.errors import *

@Client.on_message(filters.command('search') & filters.private)
async def search(client: Client, message: Message):
    update_channel = BaseConfig.CHNL_NAME
    if update_channel:
        try:
            user = await client.get_chat_member(chat_id=f'@{BaseConfig.CHNL_NAME}', user_id=message.chat.id)
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
                            InlineKeyboardButton("Join Updates Channel", url=f"t.me/{BaseConfig.CHNL_NAME}")
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

    try:
        anime = Aniko(
            gogoanime_token="dbakbihihrkqnk3",
            auth_token="EKWBIH4NJTO309U4HKTHI39U9TJ5OJ0UU5J9"
        )
        query = message.text.replace("/search", "").strip().split()

        def listToString(s):
            str1 = ""
            for ele in s:
                str1 += ele
            return str1
        query1 = listToString(query)
        if len(query1) == 0:
            await message.reply_text("Please enter the anime name")
            return
        vv = anime.search_anime(query1)
        for i in vv:
            bb = i.animeid

        ty = anime.get_details(animeid=bb)
        x = f'https://ww1.gogoanime2.org/watch/{bb}/1'
        print(
            f'<<INFO>> [Get Search:{message.chat.id}] {datetime.now()} {bb}\nUsername: {message.from_user.username}')
        msg = f'<< INFO >> [Plugins: Search: By {message.chat.id}] {datetime.now()} {bb}\nUsername: @{message.from_user.username}'
        await client.send_message(-1001482059289, msg)
        await client.send_photo(message.chat.id, ty.image_url, caption=f'''
**Anime Details**     : `{ty.title}`
**Anime Launched On** : `{ty.year}`
**Anime Status **     : `{ty.status}`
**Anime genere **     : `{ty.genres}`
**Anime Episode**     : `{ty.episodes}`  
**Anime season **     : `{ty.season}`

**Anime Download URL**: Ep 1 : `{x}`
Bot By @Rohithaditya

''',
                                reply_markup=InlineKeyboardMarkup([

                                    [InlineKeyboardButton("Join Channels",
                                                          url=BaseConfig.CHNL_URL         )],
                                    [InlineKeyboardButton(
                                        "Help Me On Download", "download")]
                                ]))
    except NetworkError:
        await message.reply_text(f"Network Error {datetime.now()} | Couldn't get the anime details",
                                 reply_markup=InlineKeyboardMarkup([

                                     [InlineKeyboardButton("Join Channels",
                                                           url=BaseConfig.CHNL_URL)],
                                     [InlineKeyboardButton(
                                         "Help Me On Search", "search")]
                                 ]))
        await client.send_message(BaseConfig.LOG_CHAT_ID, f"Network Error {datetime.now()} | Couldn't get the anime details for {message.chat.id}")
        return

    except NoSearchResultsError:
        await message.reply_text(f"No Search Results for Your Query `{query1}` on {datetime.now()}\nCouldn't get the anime details",
                                 reply_markup=InlineKeyboardMarkup([

                                     [InlineKeyboardButton("Join Channels",
                                                           url=BaseConfig.CHNL_URL)],
                                     [InlineKeyboardButton(
                                         "Help Me On Search", "search")]
                                 ]))
        await client.send_message(BaseConfig.LOG_CHAT_ID, f"No Search Results for The Query `{query1}` on {datetime.now()} \nCouldn't get the anime details for {message.chat.id}\nWith USername Of @{message.from_user.username}")
        return

    except Exception as e:
        await message.reply_text(f"Error: {e}\n\nPlease contact @Venilabots_1\nif error persist",
                                 reply_markup=InlineKeyboardMarkup([

                                     [InlineKeyboardButton("Join Channels",
                                                           url=BaseConfig.CHNL_URL)],
                                     [InlineKeyboardButton(
                                         "Help Me On Search", "search")]
                                 ]))
        await client.send_message(BaseConfig.LOG_CHAT_ID, f"Error: {e} on {datetime.now()}\nerror for {message.chat.id}")
        return
