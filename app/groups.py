from webdriver.amazon import Amazon

groups = [
    {
        "name": "RAPOSA KIDS 1",
        "name_id": "RAPOSA_KIDS_1",
        "stores": [
            Amazon("Brinquedos e Jogos", 10, 15, "Brinquedos para Bebês e Crianças Pequenas"),
            Amazon("Brinquedos e Jogos", 20, 15, "Esportes e Brincadeiras ao Ar Livre"),
            Amazon("Bebês", 70, 10),
        ],
    },
    {
        "name": "RAPOSA CASA 1",
        "name_id": "RAPOSA_CASA_1",
        "stores": [
            Amazon("Casa", 50, 15),
            Amazon("Cozinha", 10, 15),
            Amazon("Eletrodomésticos", 40, 10),
        ],
    },
    {
        "name": "RAPOSA BELEZA 1",
        "name_id": "RAPOSA_BELEZA_1",
        "stores": [
            Amazon("Beleza", 30, 10, "Cuidados com o Cabelo"),
            Amazon("Beleza", 30, 10, "Pele"),
            Amazon("Beleza", 15, 10, "Perfumes"),
            Amazon("Beleza", 15, 10, "Maquiagem"),
            Amazon("Beleza", 5, 10, "Manicure e Pedicure"),
            Amazon("Beleza", 5, 10, "Utensílios e Acessórios"),
        ],
    },
    {
        "name": "RAPOSA TECH 1",
        "name_id": "RAPOSA_TECH_1",
        "stores": [
            Amazon("Games e Consoles", 40, 15),
            Amazon("Computadores e Informática", 50, 15),
            Amazon("Eletrônicos e Tecnologia", 20, 15),
        ],
    },
]
