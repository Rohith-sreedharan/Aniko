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
from config import BaseConfig
from pyrogram.errors import *


@Client.on_message(filters.command('onair') & filters.private)
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

    msg = await message.reply_text('Processing.....')
    try:
        anime = Aniko(
            gogoanime_token="dbakbihihrkqnk3",
            auth_token="EKWBIH4NJTO309U4HKTHI39U9TJ5OJ0UU5J9"
        )
        vv = anime.get_airing_anime(count=15)
        new_list = []
        for i in vv:
            aha = i.animeid
            new_list.append(aha)
        extra = "\n".join(new_list)
        await msg.edit_text(f'''
So The Current On Air Anime Are:

`{extra}`

**
Now You May Use /search <anime name> To Get The Anime Information
**
''',
                                  reply_markup=InlineKeyboardMarkup([
                                      [InlineKeyboardButton("Join Channel",
                                                            url=BaseConfig.CHNL_URL)],
                                      [InlineKeyboardButton("Help Me On This Shit!", "help")]]))
    except Exception as e:
        await message.reply(f"Oops\nAn Error Occured:\nTry Agian Later\n\Don't Forget To Forward This Message To My devs")
        await client.send_message(BaseConfig.CHNL_URL, 
f'''
An Error Occured {e}
For {message.chat.id} 
Who Is Having USername  @{message.from_user.username}
On {datetime.now()}''')
        return
