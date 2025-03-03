#(©)CodeXBotz

import os
import logging
from dotenv import load_dotenv
from logging.handlers import RotatingFileHandler

load_dotenv()

#Bot token @Botfather
TG_BOT_TOKEN = "7889374164:AAFZOqT8YqbVkt2q_rcU9GhYPPxR9bbHsT8"

#Your API ID from my.telegram.org
APP_ID = 7973001

#Your API Hash from my.telegram.org
API_HASH = "1d942be6801b1335cd0666d0f3a8054b"

#Your db channel Id
CHANNEL_ID = -1002380406612

#OWNER ID
OWNER_ID = 1098983599

#Port
PORT = os.environ.get("PORT", "8000")

#Database 
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://anonstore:anonstore@cluster0.rej0n.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DATABASE_NAME", "AdultFilmsPlus")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "0"))
JOIN_REQUEST_ENABLE = os.environ.get("JOIN_REQUEST_ENABLED", None)

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_PIC = os.environ.get("START_PIC","https://te.legra.ph/file/91820fa385ba7e60324de-d01cc4acc318dd71e3.jpg")
START_MSG = """<b>Hello 🤗, {username}
 
🌟 I'm [Anonymous File Store Bot](https://t.me/AnonFileStoreBot)

✨ Powered By : [Adult Films](https://t.me/AdultFilmsPlus)

☀️ Files Will Be Deleted In 10 Mins Due To Copyrights

🌊 Make Sure To Download (or) Forward Files Before They Deleted</b>
"""
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "1277905393 1098983599 1093731624 2090127712").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hello {first}\n\n<b>You need to join in my Channel/Group to use me\n\nKindly Please join Channel</b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

# Auto delete time in seconds.
AUTO_DELETE_TIME = int(os.getenv("AUTO_DELETE_TIME", "600"))
AUTO_DELETE_MSG = os.environ.get("AUTO_DELETE_MSG", "<b>🗂️ 𝐅𝐢𝐥𝐞𝐬 𝐖𝐢𝐥𝐥 𝐁𝐞 𝐃𝐞𝐥𝐞𝐭𝐞𝐝 𝐈𝐧 𝟏𝟎 𝐌𝐢𝐧𝐬 𝐃𝐮𝐞 𝐓𝐨 𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 𝐑𝐞𝐚𝐬𝐨𝐧𝐬\n📥 𝐒𝐚𝐯𝐞 (𝐨𝐫) 𝐅𝐨𝐫𝐰𝐚𝐫𝐝 𝐓𝐡𝐞𝐦 𝐓𝐨 𝐘𝐨𝐮𝐫 𝐒𝐚𝐯𝐞𝐝 𝐌𝐞𝐬𝐬𝐚𝐠𝐞𝐬.</b>")
AUTO_DEL_SUCCESS_MSG = os.environ.get("AUTO_DEL_SUCCESS_MSG", "🗂️ 𝐘𝐨𝐮𝐫 𝐅𝐢𝐥𝐞𝐬 𝐀𝐫𝐞 𝐒𝐮𝐜𝐜𝐞𝐬𝐬𝐟𝐮𝐥𝐥𝐲 𝐃𝐞𝐥𝐞𝐭𝐞𝐝 𝐁𝐲 𝐁𝐨𝐭.")
#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "<b>You Are Not Allowed To Do That , Only Owner And Admins Can Use Me 🔌</b>"

ADMINS.append(OWNER_ID)
ADMINS.append(1250450587)

LOG_FILE_NAME = "AdultFilmsPlus.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
