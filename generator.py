from Config import *
import logging
from pyromod import listen
from pyrogram import Client, idle
from pyrogram.errors import (
    ApiIdInvalid, AccessTokenInvalid, ApiIdPublishedFlood)


logging.basicConfig(
    level=logging.WARNING, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


app = Client(
    ":memory:",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="StringSessionBot"),
)


# Run Bot
if __name__ == "__main__":
    try:
        app.start()
    except (ApiIdInvalid, ApiIdPublishedFlood):
        raise Exception("Your API_ID/API_HASH is not valid.")
    except AccessTokenInvalid:
        raise Exception("Your BOT_TOKEN is not valid.")
    uname = app.get_me().username
    print("➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖")
    print("🔰Support Group🔰 [LOGS] : @LegendBot_OP")
    print("⚜️Update Group⚜️  [LOGS] : @LegendBot_AI")
    print(f"✨Bot Username [LOGS] :@{uname}!")
    print("➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖")
    idle()
    app.stop()
    print("⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️")
    print("Bot Stopped")
    print(f"✨Bot Username✨ [LOGS] :@{uname}")
    print("⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️")
