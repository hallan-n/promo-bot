import os

from dotenv import load_dotenv

load_dotenv(override=True)

TOKEN_TELEGRAM = os.environ.get("TOKEN_TELEGRAM")
REDIS_CONN = "redis://localhost:6379"
MESSAGE_DELAY = 1
ROUND_DELAY = 240
CHECK_INTERVAL = 10
START_HOUR = 9
END_HOUR = 18
