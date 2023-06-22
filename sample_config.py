import os
ENV = os.environ.get("ENV", False)
try:
    API_ID = int(os.environ.get("API_ID", "20986895"))
except ValueError:
    raise Exception(
        "Your API_ID is not a valid integer.\nPlease Check The APP_ID Correctly"
    )
API_HASH = os.environ.get("API_HASH", "d81ceab1b76c91610efb2e2b016d0e04")
BOT_TOKEN = os.environ.get("BOT_TOKEN", None)
