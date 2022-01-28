from pyrogram import Client, filters
from pyrogram.types import (
    Message, InlineKeyboardMarkup,
    InlineKeyboardButton
)
from plugins.buttons import main_markup
from config import BaseConfig
from pyrogram.errors import *
# from bot import Rohith
dt = BaseConfig.OWNER_ID


@Client.on_message(filters.command(
    ["start", "ping"],
    ["/", "", "?", "!", "#"]
) & filters.private)
async def start_message(client: Client, message: Message):
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

    et = await client.get_users(dt)
    dr = et.username
    await client.send_animation(
    chat_id=message.chat.id, 
    animation=BaseConfig.STRT_IMG,
    caption=f'''
Hi {message.from_user.first_name}! 
I am Aniko, *nods*
A Bot that helps you to watch/search anime online. *slight smile*
I am currently Hosted on Heroku, *cries*
And I am still in development On AI Api. *uwu*
I am Currently in Beta Version, *nods*
so please be patient. `uwu`

My Owner : @{dr}
''',
                             reply_markup=main_markup)
    return
