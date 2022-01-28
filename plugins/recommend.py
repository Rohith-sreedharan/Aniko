from http.client import EXPECTATION_FAILED
from aniko import Aniko
from matplotlib.image import thumbnail
from pyrogram import Client, filters
from pyrogram.types import (
    Message, InlineKeyboardMarkup,
    InlineKeyboardButton
)
import random
from aniko.error_handlers import *
from config import BaseConfig
from pyrogram.errors import *

@Client.on_message(filters.command('random') & filters.private)
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

    msg = await message.reply_text("Searching...")
    try:
        anime = Aniko(
            gogoanime_token="dbakbihihrkqnk3",
            auth_token="EKWBIH4NJTO309U4HKTHI39U9TJ5OJ0UU5J9"
        )
        tk = [
            'action',
            'adventure',
            'cars',
            'comedy',
            'dementia',
            'demons',
            'drama',
            'dub',
            'ecchi',
            'fantasy',
            'game',
            'harem',
            'hentai',
            'historical',
            'horror',
            'josei',
            'kids',
            'magic',
            'martial-arts',
            'mecha',
            'military',
            'music',
            'mystery',
            'parody',
            'police',
            'psychological',
            'romance',
            'samurai',
            'school',
            'sci-fi',
            'seinen',
            'shoujo',
            'shoujo-ai',
            'shounen-ai',
            'shounen',
            'space',
            'sports',
            'super-power',
            'supernatural',
            'thriller',
            'vampire',
            'yaoi',
            'yuri',
        ]
        for i in tk:
            xx = random.choice(list(tk))

        vv = anime.get_by_genres(xx, '10')
        new_list = []
        for i in vv:
            aha = i.animeid
            new_list.append(aha)
        extra = "\n".join(new_list)
        await msg.edit_text(f'''
So The Randomised Genere is : `{xx}`
Here are the 10 Anime in this Genere : 

{extra}

**
Now You May Use /search <anime name> To Get The Anime Information
**''',
parse_mode="markdown",
                                  reply_markup=InlineKeyboardMarkup([
                                      [InlineKeyboardButton("Join Channel",
                                                            url=BaseConfig.CHNL_URL)],
                                      [InlineKeyboardButton("Help Me On This Search!", "search")]]))
    except InvalidGenreNameError:
        await msg.edit_text('Oops\nRandom Got Problem On Network Error!\nTry Again Now\nStill Issuses : Conatct @Venilabots_1')
