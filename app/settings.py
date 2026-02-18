from models import Group
from webdriver.amazon import Amazon

settings = {
    "tech": {
        "groups": {
            "whatsapp": [Group("RAPOSA TECH 1", "RAPOSA TECH 1")],
            "telegram": [Group("RAPOSA TECH", "-1003870991490")],
        },
        "stores": [
            Amazon("Games e Consoles", 40, 15),
            Amazon("Computadores e Informática", 50, 15),
            Amazon("Eletrônicos e Tecnologia", 20, 15),
        ],
    },
    "kids": {
        "groups": {
            "whatsapp": [Group("RAPOSA KIDS 1", "RAPOSA KIDS 1")],
            "telegram": [Group("RAPOSA KIDS", "-1003740187480")],
        },
        "stores": [
            Amazon("Brinquedos e Jogos", 10, 15, "Brinquedos para Bebês e Crianças Pequenas"),
            Amazon("Brinquedos e Jogos", 20, 15, "Esportes e Brincadeiras ao Ar Livre"),
            Amazon("Bebês", 70, 10),
        ],
    },
    "casa": {
        "groups": {
            "whatsapp": [Group("RAPOSA CASA 1", "RAPOSA CASA 1")],
            "telegram": [Group("RAPOSA CASA", "-1003873620132")],
        },
        "stores": [
            Amazon("Casa", 50, 15),
            Amazon("Cozinha", 10, 15),
            Amazon("Eletrodomésticos", 40, 10),
        ],
    },
    "beleza": {
        "groups": {
            "whatsapp": [Group("RAPOSA BELEZA 1", "RAPOSA BELEZA 1")],
            "telegram": [Group("RAPOSA BELEZA", "-1003880469938")],
        },
        "stores": [
            Amazon("Beleza", 30, 10, "Cuidados com o Cabelo"),
            Amazon("Beleza", 30, 10, "Pele"),
            Amazon("Beleza", 15, 10, "Perfumes"),
            Amazon("Beleza", 15, 10, "Maquiagem"),
            Amazon("Beleza", 5, 10, "Manicure e Pedicure"),
            Amazon("Beleza", 5, 10, "Utensílios e Acessórios"),
        ],
    },
}
