from os import environ

from dotenv import load_dotenv

load_dotenv(override=True)

MONGO_URI = environ.get("MONGO_URI")
