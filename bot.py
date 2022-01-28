import pyrogram
import logging
from config import *

Rohith = pyrogram.Client(
    ":memory:",
    api_id=BaseConfig.api_id,
    api_hash=BaseConfig.api_hash,
    bot_token=BaseConfig.bot_token,
    plugins=dict(
        root="plugins"
    )
)
if __name__ == '__main__':
    print('Bot started\nNow Kindly Support @Bots_universe')
    Rohith.run()
    print('Bot stopped')