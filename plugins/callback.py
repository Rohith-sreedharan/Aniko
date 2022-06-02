from pyrogram import Client, filters
from pyrogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from plugins.buttons import main_markup, help_text, help_markup, devs_markup, suppot_markup


@Client.on_callback_query()
async def callback_query(client: Client, query: CallbackQuery) -> None:
    data = query.data
    message = query.message

    if data == "home":
        await message.edit(
            f"Hi {message.from_user.first_name}! I am Aniko, a bot that helps you to watch/search anime online.",
            reply_markup=main_markup
        )

    elif data == "devs":
        await message.edit(
            "Developers of this bot are:\nAre Listed Below.",
            reply_markup=devs_markup
        )

    elif data == "suppot":
        await message.edit(
            "My Support Group is Linked Below..",
            reply_markup=suppot_markup
        )

    elif data == "help":
        await message.edit(
            help_text,
            reply_markup=help_markup,
            disable_web_page_preview=True
        )
    elif data == "choice":
        text = f'''
**COMMAND NAME** : /random 
**PARAMETERS** : None
**Usage** : This Cmd is For Get Random Choiced,
For Any Show Based On Genere,
Mr.{message.from_user.first_name}
So If You Have No Choice TO Watch? 
Then Try Me...
Hope You Will Like My Recommendations...'''
        await message.edit_text(
            text, "markdown",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("🏠 Home", "home"),
                 InlineKeyboardButton("💻 Devs", "devs")],
                [InlineKeyboardButton("Our Channel", url="t.me/bots_universe")]
            ])
        )
    elif data == "search":
        text = f'''
**COMMAND NAME** : /search 
**Parameters**: [Anime-Name]\n
**Example**: `/search Naruto`
Usage: This Cmd is For Search Anime Shows Based On Name,
Mr.{message.from_user.first_name}
So If You Have Correct Name Of Anime Show Use Me
Else Try /get [Anime-show-start name]
Always Remeber You need to use `-` 
This As Seprator Not `space`.'''
        await message.edit_text(
            text, "md",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("🏠 Home", "home"),
                 InlineKeyboardButton("💻 Devs", "devs")],
                [InlineKeyboardButton(
                    "Our Channel", url="t.me/bots_universe")], [InlineKeyboardButton("📚 Help", "help")]
            ])
        )
    elif data == "get":
        text = f'''
**COMMAND NAME** : /get 
**Parameters** : [Anime-Name] or Naruto (ANIME STARTING NAME)
**Usage** : This Command Used To Get The Exact Anime Name Show
So That You can Use In Search
Remember You Need To Use `-` As Seprator Not `space`sed Mr.{message.from_user.first_name}.'''
        await message.edit_text(
            text, "markdown",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("🏠 Home", "home"),
                 InlineKeyboardButton("💻 Devs", "devs")],
                [InlineKeyboardButton("Our Channel", url="t.me/bots_universe")]
            ])
        )
    elif data == "download":
        text = f'''
**COMMAND** : /dl 
**Parameters** : anime-name int(episode_num)
**Example** : `/dl Naruto 7`
Usage: So This Command Used To Get The Direct Download Link Of Anime Show
So That You can Download Video
Remember You Need To Use `-` As Seprator Not `space` 
Mr.{message.from_user.first_name}.
**Example Command** : `/dl One-punch 25`
**Here** : /dl is Cmd and One-punch is Anime Name and 25 is Episode Number.'''
        await message.edit_text(
            text, "markdown",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("🏠 Home", "home"),
                 InlineKeyboardButton("💻 Devs", "devs")],
                [InlineKeyboardButton("Our Channel", url="t.me/bots_universe")]
            ])
        )

    elif data == "nope":
        return

    else:
        await message.edit(
            "Oops! This button is not working! Please report this to our developers!",
            disable_web_page_preview=True,
            reply_markup=devs_markup
        )

    return None
