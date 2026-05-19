from dotenv import load_dotenv
from os import environ
load_dotenv(override=True)

MONGO_URI = environ.get("MONGO_URI")