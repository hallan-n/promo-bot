
from dotenv import load_dotenv
from os import environ

load_dotenv(override=True)

ENV = environ.get('ENV')