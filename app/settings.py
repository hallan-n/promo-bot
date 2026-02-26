from models import Group
from services.webdriver.amazon import Amazon

settings = {
    "tech": {
        "groups": {
            "whatsapp": [Group("RAPOSA TECH 1", "RAPOSA TECH 1")],
            "telegram": [Group("RAPOSA TECH", "-1003870991490")],
        },
        "stores": [
            Amazon("7791986011", 40, 15, 100),
            Amazon("16339927011", 50, 15, 100),
            Amazon("16209063011", 20, 15, 100),
        ],
    },
    "kids": {
        "groups": {
            "whatsapp": [Group("RAPOSA KIDS 1", "RAPOSA KIDS 1")],
            "telegram": [Group("RAPOSA KIDS", "-1003740187480")],
        },
        "stores": [
            Amazon("16194300011/16746739011", 10, 15, 100),
            Amazon("16194300011/121856382011", 20, 15, 100),
            Amazon("17242604011", 70, 10, 100),
        ],
    },
    "casa": {
        "groups": {
            "whatsapp": [Group("RAPOSA CASA 1", "RAPOSA CASA 1")],
            "telegram": [Group("RAPOSA CASA", "-1003873620132")],
            "instagram": [Group("PROMO RAPOSA", "promoraposa")]
        },
        "stores": [
            Amazon("16191001011", 50, 15, 100),
            Amazon("16957126011", 10, 15, 100),
            Amazon("16522083011", 40, 10, 100),
        ],
    },
    "beleza": {
        "groups": {
            "whatsapp": [Group("RAPOSA BELEZA 1", "RAPOSA BELEZA 1")],
            "telegram": [Group("RAPOSA BELEZA", "-1003880469938")],
        },
        "stores": [
            Amazon("16194415011/16754346011", 30, 10, 100),
            Amazon("16194415011/16754345011", 30, 10, 100),
            Amazon("16194415011/16754347011", 15, 10, 100),
            Amazon("16194415011/16754350011", 15, 10, 100),
            Amazon("16194415011/16754349011", 5, 10, 100),
            Amazon("16194415011/16754348011", 5, 10, 100),
        ],
    },
}