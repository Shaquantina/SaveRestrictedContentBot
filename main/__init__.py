#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = 27510499
API_HASH = "23a87ce25f0fffdb11f693b93e338215"
BOT_TOKEN = "6248076574:AAEjiBfzRwBv0-ahuKYelIbdfALg58OzXlA"
SESSION = "AQBBOfSgntDix-U3qMSCuuiHHzUrpEfaoxmF7XWnXJw942LRe39iey1irUm3GVmSS754DOKd8r3bMtmjeH4mz7lMDL6BoYK6A0z5JdluHqhHHhTC7eDCceOfDcwg1xTUNiDyhfg8EiTLQW8fLZkew2dkhiXuqKRgrCGsKCX_KNXFIkVOtQmnhMydJ8giygXvE2st15DE1dnjVr_Vh2wra57rlWiz8EdZtMNsA2YRcLmBd9XaNukVDmQrx7PSs5KwK-qB5F8Pa_5UpHGWVfENwmpFJ8coN_GzB9LpHmKFzRiWaLwgl-lb683uhQzmvwgEIenWt1UOK0gcCuWwVrM29joKAAAAAXBJMXAA"
FORCESUB = config("FORCESUB", default=None)
AUTH = 6178812272

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client(
    session_name=SESSION, 
    api_hash=API_HASH, 
    api_id=API_ID)

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
