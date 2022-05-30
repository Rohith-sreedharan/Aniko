from http.client import EXPECTATION_FAILED
from aniko import Aniko
from pyrogram import Client, filters
from pyrogram.types import (
    Message, InlineKeyboardMarkup,
    InlineKeyboardButton
)
from aniko.error_handlers import *
from plugins.buttons import help_text, help_markup, devs_markup, suppot_markup
from pyrogram.errors import *
from config import BaseConfig

# from bot import Rohith

@Client.on_message(filters.command('get') & filters.private)
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

    msg = await message.reply_text('Processing...')
    try:
        anime = Aniko(
            gogoanime_token="dbakbihihrkqnk3",
            auth_token="EKWBIH4NJTO309U4HKTHI39U9TJ5OJ0UU5J9"
        )
        query = message.text.replace("/get", "").strip().split()

        def listToString(s):
            return "".join(s)
        query1 = listToString(query)
        if len(query1) == 0:
            await msg.edit_text("Please enter the anime name")
            return

        vv = anime.search_anime(query1)
        new_list = []
        if len(query1) == 0:
            await msg.edit_text("Please enter the anime name")
            return
        vv = anime.search_anime(query1)
        new_list = []
        for i in vv:
            aha = i.animeid
            new_list.append(aha)
        extra = "\n".join(new_list)
        await msg.edit_text(f'''
The Available Anime Starting With `{query1}` are:

{extra}

**
Now You May Use /search <anime name> To Get The Anime Information
**
''',
parse_mode="markdown",
reply_markup=InlineKeyboardMarkup(
                                      [[InlineKeyboardButton("Help Me To Search", "search")]]))
        return

    except NoSearchResultsError:
        await msg.edit_text("No Such Anime-show Found\nTry Using /get and /search <anime name>",
                                 reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Help Me On This Shit!", "get")]]))
        return
    except Exception as e:
        await msg.edit_text(f"{e}",
                                 reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Conatct Devloper", "devs")]]))
        return
