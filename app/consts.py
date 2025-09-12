
from dotenv import load_dotenv
from os import environ

load_dotenv(override=True)

DAYS_TO_EXPIRE_SESSION = 5
ENV = environ.get('ENV')