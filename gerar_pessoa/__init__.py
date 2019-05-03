from random import choice, randint

nomes_masculinos = [
    "Miguel",
    "Arthur",
    "Bernardo",
    "Heitor",
    "Davi",
    "Lorenzo",
    "Théo",
    "Pedro",
    "Gabriel",
    "Enzo",
    "Matheus",
    "Lucas",
    "Benjamin",
    "Nicolas",
    "Guilherme",
    "Joaquim",
    "Rafael",
    "Samuel",
    "Enzo Gabriel",
    "João Miguel",
    "Henrique",
    "Gustavo",
    "Murilo",
    "Pedro Henrique",
    "Pietro",
    "Lucca",
    "Felipe",
    "João Pedro",
    "Isaac",
    "Benício",
    "Daniel",
    "Anthony",
    "Leonardo",
    "Davi Lucca",
    "Bryan",
    "Eduardo",
    "João Lucas",
    "Victor",
    "João",
    "Cauã",
    "Antônio",
    "Vicente",
    "Caleb",
    "Gael",
    "Bento",
    "Caio",
    "Emanuel",
    "Vinícius",
    "João Guilherme",
    "Davi Lucas",
    "Noah",
    "João Gabriel",
    "João Victor",
    "Luiz Miguel",
    "Francisco",
    "Kaique",
    "Martin",
    "Otávio",
    "Miguel Henrique",
    "Oliver",
    "Augusto",
    "Levi",
    "Yuri",
    "Enrico",
    "Thiago",
    "Ian",
    "Ruan",
    "Anthony Gabriel",
    "Danilo",
    "Yago",
    "José",
    "André",
    "Lucas Gabriel",
    "Tomás",
    "Carlos Eduardo",
    "Luiz Otávio",
    "Hugo",
    "Thomas",
    "Victor ",
    "Henry",
    "Luiz Felipe",
    "Arthur Miguel",
    "Ryan",
    "Arthur Henrique",
    "Fernando",
    "Enzo Miguel",
    "Kauê",
    "Breno",
    "Arthur Gabriel",
    "Davi Luiz",
    "Nathan",
    "Pedro Lucas",
    "Davi Miguel",
    "Luiz Gustavo",
    "Henrique",
    "Luan",
    "Raul",
    "Pedro Miguel",
    "Rodrigo",
    "Bruno",
    "Luiz" 
]

nomes_femininos = [
    "Alice",	
    "Sophia",	
    "Helena",	
    "Valentina",	
    "Laura",
    "Isabella",	
    "Manuela",	
    "Júlia",	
    "Heloísa",	
    "Luiza",	
    "Maria Luiza",
    "Lorena",	
    "Lívia",	
    "Giovanna",	
    "Maria Eduarda",	
    "Beatriz",	
    "Maria Clara",
    "Cecília",
    "Eloá",	
    "Lara",	
    "Maria Júlia",	
    "Isadora",
    "Mariana",
    "Emanuelly",	
    "Ana Júlia",	
    "Ana Luiza",	
    "Ana Clara",	
    "Melissa",
    "Yasmin",	
    "Maria Alice",
    "Isabelly",	
    "Lavínia",	
    "Esther",	
    "Sarah",	
    "Elisa",	
    "Antonella",
    "Rafaela",
    "Maria Cecília",	
    "Liz",	
    "Marina",	
    "Nicole",	
    "Maitê",	
    "Isis",	
    "Alícia",	
    "Luna",	
    "Rebeca",	
    "Agatha",	
    "Letícia",	
    "Maria",	
    "Gabriela",	
    "Ana Laura",	
    "Catarina",	
    "Clara",	
    "Ana Beatriz",	
    "Vitória",
    "Olívia",	
    "Maria Fernanda",
    "Emilly",	
    "Maria Valentina",
    "Milena",	
    "Maria Helena",	
    "Bianca",	
    "Larissa",	
    "Mirella	",
    "Maria Flor",
    "Allana",	
    "Ana Sophia",	
    "Clarice",	
    "Pietra",	
    "Maria Vitória",	
    "Maya",	
    "Laís",	
    "Ayla",	
    "Ana Lívia",	
    "Eduarda",
    "Mariah",	
    "Stella",	
    "Ana Erick",
    "Gabrielly",	
    "Sophie",	
    "Carolina",	
    "Maria Laura",	
    "Maria Heloísa",	
    "Maria Sophia",	
    "Fernanda",	
    "Malu",	
    "Analu",	
    "Amanda",	
    "Aurora",	
    "Maria Isis",	
    "Louise",	
    "Heloise",
    "Ana Vitória",
    "Ana Cecília",
    "Ana Liz",	
    "Joana",	
    "Luana",	
    "Antônia",	
    "Isabel",	
    "Bruna"	
]


nomes = [
    "Miguel",
    "Arthur",
    "Bernardo",
    "Heitor",
    "Davi",
    "Lorenzo",
    "Théo",
    "Pedro",
    "Gabriel",
    "Enzo",
    "Matheus",
    "Lucas",
    "Benjamin",
    "Nicolas",
    "Guilherme",
    "Joaquim",
    "Rafael",
    "Samuel",
    "Enzo Gabriel",
    "João Miguel",
    "Henrique",
    "Gustavo",
    "Murilo",
    "Pedro Henrique",
    "Pietro",
    "Lucca",
    "Felipe",
    "João Pedro",
    "Isaac",
    "Benício",
    "Daniel",
    "Anthony",
    "Leonardo",
    "Davi Lucca",
    "Bryan",
    "Eduardo",
    "João Lucas",
    "Victor",
    "João",
    "Cauã",
    "Antônio",
    "Vicente",
    "Caleb",
    "Gael",
    "Bento",
    "Caio",
    "Emanuel",
    "Vinícius",
    "João Guilherme",
    "Davi Lucas",
    "Noah",
    "João Gabriel",
    "João Victor",
    "Luiz Miguel",
    "Francisco",
    "Kaique",
    "Martin",
    "Otávio",
    "Miguel Henrique",
    "Oliver",
    "Augusto",
    "Levi",
    "Yuri",
    "Enrico",
    "Thiago",
    "Ian",
    "Ruan",
    "Anthony Gabriel",
    "Danilo",
    "Yago",
    "José",
    "André",
    "Lucas Gabriel",
    "Tomás",
    "Carlos Eduardo",
    "Luiz Otávio",
    "Hugo",
    "Thomas",
    "Victor ",
    "Henry",
    "Luiz Felipe",
    "Arthur Miguel",
    "Ryan",
    "Arthur Henrique",
    "Fernando",
    "Enzo Miguel",
    "Kauê",
    "Breno",
    "Arthur Gabriel",
    "Davi Luiz",
    "Nathan",
    "Pedro Lucas",
    "Davi Miguel",
    "Luiz Gustavo",
    "Henrique",
    "Luan",
    "Raul",
    "Pedro Miguel",
    "Rodrigo",
    "Bruno",
    "Luiz",
    "Alice",	
    "Sophia",	
    "Helena",	
    "Valentina",	
    "Laura",
    "Isabella",	
    "Manuela",	
    "Júlia",	
    "Heloísa",	
    "Luiza",	
    "Maria Luiza",
    "Lorena",	
    "Lívia",	
    "Giovanna",	
    "Maria Eduarda",	
    "Beatriz",	
    "Maria Clara",
    "Cecília",
    "Eloá",	
    "Lara",	
    "Maria Júlia",	
    "Isadora",
    "Mariana",
    "Emanuelly",	
    "Ana Júlia",	
    "Ana Luiza",	
    "Ana Clara",	
    "Melissa",
    "Yasmin",	
    "Maria Alice",
    "Isabelly",	
    "Lavínia",	
    "Esther",	
    "Sarah",	
    "Elisa",	
    "Antonella",
    "Rafaela",
    "Maria Cecília",	
    "Liz",	
    "Marina",	
    "Nicole",	
    "Maitê",	
    "Isis",	
    "Alícia",	
    "Luna",	
    "Rebeca",	
    "Agatha",	
    "Letícia",	
    "Maria",	
    "Gabriela",	
    "Ana Laura",	
    "Catarina",	
    "Clara",	
    "Ana Beatriz",	
    "Vitória",
    "Olívia",	
    "Maria Fernanda",
    "Emilly",	
    "Maria Valentina",
    "Milena",	
    "Maria Helena",	
    "Bianca",	
    "Larissa",	
    "Mirella	",
    "Maria Flor",
    "Allana",	
    "Ana Sophia",	
    "Clarice",	
    "Pietra",	
    "Maria Vitória",	
    "Maya",	
    "Laís",	
    "Ayla",	
    "Ana Lívia",	
    "Eduarda",
    "Mariah",	
    "Stella",	
    "Ana Erick",
    "Gabrielly",	
    "Sophie",	
    "Carolina",	
    "Maria Laura",	
    "Maria Heloísa",	
    "Maria Sophia",	
    "Fernanda",	
    "Malu",	
    "Analu",	
    "Amanda",	
    "Aurora",	
    "Maria Isis",	
    "Louise",	
    "Heloise",
    "Ana Vitória",
    "Ana Cecília",
    "Ana Liz",	
    "Joana",	
    "Luana",	
    "Antônia",	
    "Isabel",	
    "Bruna"	
]

    
sobrenomes = [
    "Agostinho",
    "Aguiar",
    "Albuquerque",
    "Alegria",
    "Alencastro",
    "Almada",
    "Alves",
    "Alvim",
    "Amorim",
    "Andrade",
    "Antunes",
    "Aparício",
    "Apolinário",
    "Araújo",
    "Arruda",
    "Assis",
    "Assunção",
    "Ávila",
    "Azambuja",
    "Baptista",
    "Barreto",
    "Barros",
    "Beira-Mar",
    "Belchior",
    "Belém",
    "Bernardes",
    "Bittencourt",
    "Boaventura",
    "Bonfim",
    "Botelho",
    "Brites",
    "Brito",
    "Caetano",
    "Calixto",
    "Camacho",
    "Camilo",
    "Capelo",
    "Castro",
    "Cavalcante",
    "Chaves",
    "Conceição",
    "Corte Real",
    "Cortês",
    "Coutinho",
    "Crespo",
    "Cunha",
    "Curado",
    "Custódio",
    "Córdoba",
    "Damásio",
    "Dantas",
    "Dias",
    "Dinís",
    "Domingues",
    "Dorneles",
    "dos Reis",
    "Drumond",
    "D’Ávila",
    "Escobar",
    "Espinosa",
    "Esteves",
    "Evangelista",
    "Farias",
    "Ferrari",
    "Figueiredo",
    "Figueiroa",
    "Flores",
    "Fogaça",
    "Freitas",
    "Frutuoso",
    "Furtado",
    "Félix",
    "Galvão",
    "Garcia",
    "Gaspar",
    "Gentil",
    "Geraldes",
    "Gil",
    "Godinho",
    "Gomes",
    "Gonzaga",
    "Goulart",
    "Gouveia",
    "Guedes",
    "Guimarães",
    "Guterres",
    "Góis",
    "Hernandes",
    "Hilário",
    "Hipólito",
    "Ibrahim",
    "Ilha",
    "Infante",
    "Jaques",
    "Jesus",
    "Jordão",
    "Lacerda",
    "Lancastre",
    "Leiria",
    "Lessa",
    "Machado",
    "Maciel",
    "Magalhães",
    "Maia",
    "Maldonado",
    "Marinho",
    "Marques",
    "Martins",
    "Medeiros",
    "Meireles",
    "Mello",
    "Mendes",
    "Menezes",
    "Mesquita",
    "Modesto",
    "Monteiro",
    "Morais",
    "Moreira",
    "Morgado",
    "Moura",
    "Muniz",
    "Neves",
    "Nogueira",
    "Novais",
    "Nóbrega",
    "Ornélas",
    "Oliveira",
    "Ourique",
    "Pacheco",
    "Padilha",
    "Paiva",
    "Paraíso",
    "Paris",
    "Peixoto",
    "Peralta",
    "Peres",
    "Pilar",
    "Pimenta",
    "Pinheiro",
    "Portela",
    "Quaresma",
    "Quarteira",
    "Queiroz",
    "Ramires",
    "Ramos",
    "Rebelo",
    "Resende",
    "Ribeiro",
    "Salazar",
    "Sales",
    "Salgado",
    "Salgueiro",
    "Sampaio",
    "Sanches",
    "Santana",
    "Siqueira",
    "Soares",
    "Subtil",
    "Tavares",
    "Taveira",
    "Teixeira",
    "Teles",
    "Torres",
    "Trindade",
    "Varela",
    "Vargas",
    "Vasconcelos",
    "Vasques",
    "Veiga",
    "Veloso",
    "Vidal",
    "Vieira",
    "Vilela",
    "Xavier",
    "Ximenes",
    "Xisco",
    "Zagalo",
    "Zanette",
    "Zaganelli"
]

def gerar_nome():
    return f"{choice(nomes)} {choice(sobrenomes)} {choice(sobrenomes)}"

def gerar_data():
    ano = randint(1900, 2100)
    mes = randint(1, 12)

    if  mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
        dia = randint(1, 31) 
    elif mes == 2:
        dia = randint(1, randint(28, 29))
    else:
        dia = randint(1, 30)

    return f"{ano}-{mes}-{dia}"

def gerar_matricula():
    return randint(1, 999999)

def gerar_telefone():
    return f"({randint(10, 99)}) {randint(10000, 99999)}-{randint(1000, 9999)}"