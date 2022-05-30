import dotenv
import logging
from os import getenv
dotenv.load_dotenv()



class BaseConfig(object):
    BOT_TOKEN = getenv("BOT_TOKEN")
    OWNER_ID = int(getenv("OWNER_ID", 1207066133))
    API_ID = int(getenv("API_ID"))
    API_HASH = getenv("API_HASH")
    LOG_CHAT_ID = int(getenv("LOG_CHAT_ID", "-1001482059289"))
    LOG_LEVEL = getenv("LOG_LEVEL") or "INFO"
    CHNL_NAME = getenv("UPDATES_CHANNEL", "bots_universe")
    STRT_IMG = getenv("ALIVE_IMG", "https://c.tenor.com/uCVosr0dhnQAAAAC/anime-hello.gif")