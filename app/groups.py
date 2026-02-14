from webdriver.amazon import Amazon

groups = [
    {
        "name": "RAPOSA KIDS 1",
        "name_id": "RAPOSA_KIDS_1",
        "stores": [
            Amazon(
                "Brinquedos e Jogos",
                20,
                15,
                "Brinquedos para Bebês e Crianças Pequenas",
            ),
            Amazon("Brinquedos e Jogos", 20, 15, "Esportes e Brincadeiras ao Ar Livre"),
            Amazon("Bebês", 30, 10),
        ],
    },
    {
        "name": "RAPOSA CASA 1",
        "name_id": "RAPOSA_CASA_1",
        "stores": [
            Amazon("Casa", 30, 15),
            Amazon("Cozinha", 30, 15),
            Amazon("Eletrodomésticos", 30, 10),
        ],
    },
    {
        "name": "RAPOSA BELEZA 1",
        "name_id": "RAPOSA_BELEZA_1",
        "stores": [
            Amazon("Beleza", 30, 15, "Cuidados com o Cabelo"),
            Amazon("Beleza", 30, 15, "Manicure e Pedicure"),
            Amazon("Beleza", 30, 15, "Maquiagem"),
            Amazon("Beleza", 30, 15, "Pele"),
            Amazon("Beleza", 30, 15, "Perfumes"),
            Amazon("Beleza", 30, 15, "Utensílios e Acessórios"),
        ],
    },
]
