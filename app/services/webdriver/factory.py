from services.webdriver.amazon import Amazon
from services.webdriver.instagram import Instagram
from services.webdriver.whatsapp import Whatsapp
from services.webdriver.base import BaseStore, BaseMessenger

def get_store(name: str) -> BaseStore:
    match name:
        case "amazon": return Amazon
        case _: return  None

def get_message(name: str) -> BaseMessenger:
    match name:
        case "instagram": return Instagram
        case "whatsapp": return Whatsapp
        case _: return  None
