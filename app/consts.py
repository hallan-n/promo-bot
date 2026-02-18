import os

from dotenv import load_dotenv

load_dotenv(override=True)

TOKEN_TELEGRAM = os.environ.get("TOKEN_TELEGRAM")
