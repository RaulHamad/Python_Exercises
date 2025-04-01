musicas = [
    {"titulo": 'Amigo', "tocou": 4},
    {"titulo": 'ai se eu te pego', "tocou": 45},
    {"titulo": 'para sempre', "tocou": 12},
    {"titulo": 'nuvem de lagrimas', "tocou": 23},
    {"titulo": 'papel mache', "tocou": 14}
]

qut_musicas =(min(musicas, key=lambda x : x["tocou"]))
print(qut_musicas)
