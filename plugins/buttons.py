import pyrogram
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import BaseConfig

def title(l: list = ["text", "data", "url", "login_url", "switch_inline_query, switch_inline_query_current_chat"]):
    text = l[0] if l else "No Text"
    data = l[1] if len(l) >= 2 else "nope"
    url = l[2] if len(l) >= 3 else None
    login_url = l[3] if len(l) >= 4 else None
    switch_inline_query = l[4] if len(l) >= 5 else None
    switch_inline_query_current_chat = l[5] if len(l) >= 6 else None

    return InlineKeyboardButton(text, data, url, login_url, switch_inline_query, switch_inline_query_current_chat)


def create_markup(_list: list = [[]]):
    result = []
    for row in _list:
        result.append([])
        for item in row:
            btn = title(item)
            result[-1].append(btn)

    return InlineKeyboardMarkup(result)

CHNL_URL = f't.me/{BaseConfig.CHNL_NAME}'

r_home_btn = ["🏠 Home", "home"]
r_help_btn = ["🙂 Help", "help"]
r_devs_btn = ["💻 Devs", "devs"]
r_ourc_btn = ["💝 Our Channel", None, CHNL_URL]
r_parvat = ["@Parvat_R", None, "t.me/Parvat_R"]
r_rohith = ["@Rohithaditya", None, "t.me/Rohithaditya"]
r_search_btn = ["🔍 Search", "search"]
r_get_btn = ["🔍 Get", "get"]
r_rand_btn = ["❓ Recommendations", "choice"]
r_dl_btn = ["📥 Download", "download"]
r_grp_btn = ["💝 Our Group", None, "https://telegram.me/venilabots1"]

main_markup = create_markup([
    [r_help_btn],
    [r_devs_btn],
    [r_ourc_btn]
])

devs_markup = create_markup([
        [r_rohith],
    [r_parvat],[r_home_btn]
])
# cmd_markup = create_markup([
#     [r_search_btn],
#     [(r_get_btn)], [(r_rand_btn)], [r_dl_btn],
#     [r_home_btn], [(r_devs_btn)]
# ])

help_text = """\
I am `Aniko` Made by [@Bots_Universe](t.me/bots_universe).
I can search you any `Anime Shows` and give you the direct download link 🔗 for the **Anime Show** 🎥.

**Note**
```
The official Go Go Anime is no way supporting or promoting this bot.
The official Go GO Anime has nothing to do with this bot.
This bot is created only for Searching Shows. Don't misuse it.
Use it at your own risk.
```
"""
help_markup = create_markup([
    [r_search_btn], [r_dl_btn],[r_get_btn],
        [r_rand_btn],[r_home_btn],
                [r_devs_btn]
])

suppot_markup = create_markup([
    [r_ourc_btn], [r_grp_btn],
    [r_devs_btn], [r_home_btn]
])
