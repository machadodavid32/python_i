"""
Sorted -
Obs: Não confunda, apesar do nome, com a função sort(). Sort() só funciona em lista.

Podemos utilizar o sorted() com qualquer iterável.

Como o proprio nome diz, sorted() serve para ordenar


# Exemplo
numeros = [6, 1, 8, 2]
print(numeros)

print(sorted(numeros))  # Ordena do menor para o maior
print(numeros)

# Resposta -
# [6, 1, 8, 2]
# [1, 2, 6, 8] -> Ele ordena a lista
# [6, 1, 8, 2] -> Mas não altera a lista

numeros = (6, 1, 8, 2)
print(numeros)

print(sorted(numeros))  # Ordena do maior para o menor
print(numeros)
# Resposta:
# (6, 1, 8, 2)
# [1, 2, 6, 8] - Repara que o sorted() sempre retorna uma lista
# (6, 1, 8, 2) - > e nunca altera



# Adicionando parâmetros ao sorted()

numeros = [6, 1, 8, 2]
print(numeros)

print(sorted(numeros))
print(sorted(numeros, reverse=True))
# Resposta:
# [6, 1, 8, 2]
# [1, 2, 6, 8]
# [8, 6, 2, 1] - > aqui ele reverte na ordem



# Podemos utilizar o sorted para coisas mais complexas.

usuarios = [
    {"Username": "Samuel", "tweets": ["Eu adoro bolos", "Eu adoro pizzas"]},
    {"Username": "Carla", "tweets": ["Eu amo meu gato"]},
    {"Username": "Jeff", "tweets": []},
    {"Username": "bob123", "tweets": []},
    {"Username": "dogoo", "tweets": ["Eu gosto de cachorro", "Vou sair hoje"]},
    {"Username": "gal", "tweets": []}
    ]

print(usuarios)
# Ordenando por username - ordem alfabética
print(sorted(usuarios, key=lambda usuario: usuario["Username"]))  # Ele vai ordenar pelo usuario
# Resposta: Resposta grande demais. Ele ordena a lista pelo 'Username'


# Ordenando pelo número de twites
print(sorted(usuarios, key=lambda usuario: len(usuario["tweets"])))
# Resposta: Reposta muito grande, mas ele ordena pelo numero de tweets do usuario

"""
musicas = [
    {"titulo": "thunderstruck", "tocou": 3},
    {"titulo": "one", "tocou": 4},
    {"titulo": "keep the faith", "tocou": 2},
    {"titulo": "Blaze of glory", "tocou": 6}
]
# Ordenar da menos tocada para a mais tocada
print(sorted(musicas, key=lambda musica: musica['tocou']))
# Resposta: [{'titulo': 'keep the faith', 'tocou': 2}, {'titulo': 'thunderstruck', 'tocou': 3}, {'titulo': 'one', 'tocou': 4}, {'titulo': 'Blaze of glory', 'tocou': 6}]

# Ordena da mais tocada para a menos tocada
print(sorted(musicas, key=lambda  musica: musica['tocou'], reverse=True))
# Resposta: [{'titulo': 'Blaze of glory', 'tocou': 6}, {'titulo': 'one', 'tocou': 4}, {'titulo': 'thunderstruck', 'tocou': 3}, {'titulo': 'keep the faith', 'tocou': 2}]



