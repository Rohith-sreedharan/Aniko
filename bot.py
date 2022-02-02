import pyrogram
import logging
from config import *

Rohith = pyrogram.Client(
    ":memory:",
    api_id=BaseConfig.API_ID,
    api_hash=BaseConfig.API_HASH,
    bot_token=BaseConfig.BOT_TOKEN,
    plugins=dict(
        root="plugins"
    )
)
if __name__ == '__main__':
    print('Bot started\nNow Kindly Support @Bots_universe')
    Rohith.run()
    print('Bot stopped')
