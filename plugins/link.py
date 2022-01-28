from http.client import EXPECTATION_FAILED
from aniko import Aniko
from matplotlib.image import thumbnail
from pyrogram import Client, filters
from pyrogram.types import (
    Message, InlineKeyboardMarkup,
    InlineKeyboardButton
)
from aniko.error_handlers import *
from plugins.buttons import main_markup
import requests
from config import BaseConfig
from pyrogram.errors import *

vic = "https://ww1.gogoanime2.org/watch/naruto-dub/1"
buh = "https://www1.gogoanime.pe/bakusou-kyoudai-lets-go-wgp-episode-35"
dr = "https://gogoanime.run/bakusou-kyoudai-lets-go-wgp-episode-35"
bh = "https://gogoanime.onl/episode/kiratto-prichan-season-3-episode-49"

dt = "https://gogoanime.run"
ah = "https://gogoanime.onl"
fg = "https://gogoanime.pe"
gi = "https://ww1gogoanime2.org"


if requests.get(vic).status_code == 200:
    site = gi
if requests.get(dr).status_code == 200:
    site = dt
elif requests.get(bh).status_code == 200:
    site = ah
elif requests.get(buh).status_code == 200:
    site = fg
else:
    print('Error [DOWNLOAD LINK.PY] | @Venilabots1')

    async def error(client: Client, message: Message):
        await client.send_message(BaseConfig.CHNL_URL, 'Error [DOWNLOAD LINK.PY] | Contact @Venilabots1\nThis is Serious..')
        await exit()


@Client.on_message(filters.command('dl') & filters.private)
async def dl(client: Client, message: Message):
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
        msg = await message.reply('Processing...')
        zz, ep = message.text.split(" ", 1)[1].split(" ", 1)
        anime = Aniko(
            gogoanime_token="dbakbihihrkqnk3",
            auth_token="EKWBIH4NJTO309U4HKTHI39U9TJ5OJ0UU5J9"
        )
        vv = anime.search_anime(zz)
        for i in vv:
            bb = i.animeid
        # x = f'{site}/watch/{bb}/{ep}'
        if site == gi:
            d = f'{site}/watch/{bb}/{ep}'
        if site == ah:
            d = f'{site}/{bb}-episode-{ep}'
        if site == dt:
            d = f'{site}/{bb}-episode-{ep}'
        if site == fg:
            d = f'{site}/episode/{bb}-episode-{ep}'

        await msg.edit_text(f'''
Your Download Url: {d}''',
                            reply_markup=InlineKeyboardMarkup([
                                [InlineKeyboardButton("Help on This Shit !", "download")], ]))
    except IndexError:
        await msg.edit_text("Please enter the anime name and episode number",
                            reply_markup=InlineKeyboardMarkup([
                                [InlineKeyboardButton("Help on This Shit !", "download")], ]))
        return

    except ValueError:
        await msg.edit_text("Please enter the anime name and episode number",
                            reply_markup=main_markup)
        return

    except Exception as e:
        await msg.edit_text(f"Error: {e}\n\nPlease contact @Venilabots_1\nif error persist",
                            reply_markup=InlineKeyboardMarkup([
                                [InlineKeyboardButton("Help on This Shit !", "download")], ]))
        return
