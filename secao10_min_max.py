"""
Min e Max

max() -> Retorna o maior valor em um interável ou maior de dois ou mais elemento


# Exemplo max()
lista = [1, 8, 4, 99, 34, 129]
print(max(lista))
# Resposta: 129
tupla = (1, 8, 4, 99, 34, 129)
print(max(tupla))
# Resposta: 129
conjunto = {1, 8, 4, 99, 34, 129}
print(max(conjunto))
# Resposta: 129
dicionario = {'a': 1, 'b': 8, 'c': 4, 'd': 99, 'e': 34, 'f': 129}
print(max(dicionario))
# Resposta: f
dicionario = {'a': 1, 'b': 8, 'c': 4, 'd': 99, 'e': 34, 'f': 129}
print(max(dicionario.values()))
# Resposta: 129



# Faça um programa que receba dois valores do usuario e imprima o maior

val1 = int(input("Informe o valor 1: "))
val2 = int(input("Informe o valor 2: "))
maior = (max(val1, val2))
print(f'O valor maior é: {maior}')


print(max('a', 'b', 'c', 'dsd'))
# Resposta: dsd

print(max('a', 'd', 'f', 'g'))
# Resposta: g



# min() -> Retorna o menor valor em um iterável ou o menor de dois ou mais elementos:

# Exemplo min()
lista = [1, 8, 4, 99, 34, 129]
print(min(lista))
# Resposta:1
tupla = (1, 8, 4, 99, 34, 129)
print(min(tupla))
# Resposta: 1
conjunto = {1, 8, 4, 99, 34, 129}
print(min(conjunto))
# Resposta: 1
dicionario = {'a': 1, 'b': 8, 'c': 4, 'd': 99, 'e': 34, 'f': 129}
print(min(dicionario))
# Resposta: a
dicionario = {'a': 1, 'b': 8, 'c': 4, 'd': 99, 'e': 34, 'f': 129}
print(min(dicionario.values()))
# Resposta: 1



# Faça um programa que receba dois valores do usuario e imprima o menor

val1 = int(input("Informe o valor 1: "))
val2 = int(input("Informe o valor 2: "))
menor = (min(val1, val2))
print(f'O valor menor é {menor}')


print(min('a', 'b', 'c', 'dsd'))
# Resposta: a

print(min('a', 'd', 'f', 'g'))
# Resposta: a



# Outros exemplos

nomes = ['Arya', 'Samson', 'Dora', 'Tim', 'Ollivander']
print(max(nomes))
# Resposta: Tim
print(min(nomes))
# Resposta: Arya  - > O min e max levam em consideração a ordem alfabetica

print(max(nomes, key=lambda nome: len(nome)))
# Resposta: Ollivander
print(min(nomes, key=lambda nome: len(nome)))
# Resposta: Tim  -> Aqui vai receber o menor pelo numero de letras utilizando a lambda len

"""

musicas = [
    {"titulo": "thunderstruck", "tocou": 3},
    {"titulo": "one", "tocou": 4},
    {"titulo": "keep the faith", "tocou": 2},
    {"titulo": "Blaze of glory", "tocou": 6}
]
print(max(musicas, key=lambda musica: musica['tocou']))
# Resposta: {'titulo': 'Blaze of glory', 'tocou': 6}

print(min(musicas, key=lambda musica: musica['tocou']))
# Resposta: {'titulo': 'keep the faith', 'tocou': 2}

# Desafio - > Imprima somente o titulo da musica mais e menos tocada
mais = (max(musicas, key=lambda musica: musica['tocou'])['titulo'])
print(f"A musica mais tocada é {mais}")
# Resposta: A musica mais tocada é Blaze of glory
menos = (min(musicas, key=lambda musica: musica['tocou'])['titulo'])
print(f"A musica menos tocada é {menos}")
# Resposta: A música menos tocada é keep the faith


# Desafio -> Como encontrar a musica mais tocada e menos tocada sem usar max, min e lambda:

max = 0
for musica in musicas:
    if musica['tocou'] > max:
        max = musica['tocou']

for musica in musicas:
    if musica['tocou'] == max:
        print(musica['titulo'])
# Resposta: Blaze of glory

min = 9999
for musica in musicas:
    if musica['tocou'] < min:
        min = musica['tocou']

for musica in musicas:
    if musica['tocou'] == min:
        print(musica['titulo'])
# Resposta: keep the faith

# Acima, veja como é mais trabalhoso

