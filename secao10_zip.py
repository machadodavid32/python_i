"""
Zip - zip -> cria um iterável chamado zip project que agrega elemento de cada um dos iteráveis
passados como entrada em pares

# Exemplos:
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

zip1 = zip(lista1, lista2)

print(zip1)

print(type(zip1))

# Resposta: <zip object at 0x7f22c6f49f00>
# <class 'zip'>

# Sempre podemos iterar uma lista, tupla, set ou dicionário.
print(list(zip1))
print(tuple(zip1))
print(set(zip1))
print(dict(zip1))

# Resposta: [(1, 4), (2, 5), (3, 6)]
# ()
# set()
# {}  -> Repare que sumiu, pois, executado após a primeira vez, ele some.

# Para corrigir o caso acima, podemos fazer o seguinte:

zip1 = zip(lista1, lista2)
print(list(zip1))

zip1 = zip(lista1, lista2)
print(tuple(zip1))

zip1 = zip(lista1, lista2)
print(set(zip1))

zip1 = zip(lista1, lista2)
print(dict(zip1))

# Resposta: [(1, 4), (2, 5), (3, 6)]
# ((1, 4), (2, 5), (3, 6))
# {(2, 5), (1, 4), (3, 6)}
# {1: 4, 2: 5, 3: 6}

lista3 = [7, 8, 9, 10, 11]
zip1 = zip(lista1, lista2, lista3)
print(list(zip1))
# Resposta: [(1, 4, 7), (2, 5, 8), (3, 6, 9)]
# OBS: O zip() utiliza como parâmetro o menor tamanho como iterável.
# Ou seja, no caso acima, ele pega o tamanho da menor lista e ignora o restante da maior...,
# no caso, lista3 numeros 10 e 11. E não importa a posição da lista



# Podemos utilizar diferentes iteráveis no zip()

tupla = (1, 2, 3, 4, 5)
lista = [6, 7, 8, 9, 10]
dicionario = {'a': 11, 'b': 12, 'c': 13, 'd': 14, 'e': 15}

zt = zip(tupla, lista, dicionario.values())
print(list(zt))

# Resposta: [(1, 6, 11), (2, 7, 12), (3, 8, 13), (4, 9, 14), (5, 10, 15)]

# Podemos também lista de tuplas

dados = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)]
print(list(zip(*dados)))  # O * desempacota dados
# Resposta: [(0, 1, 2, 3, 4), (1, 2, 3, 4, 5)]


"""

# Exemplos mais complexos

prova1 = [80, 91, 78]
prova2 = [98, 89, 53]
alunos = ['Maria', 'Pedro', 'Carla']

final = {dado[0]: max(dado[1], dado[2]) for dado in zip(alunos, prova1, prova2)}
print(final)
# Resposta: {'Maria': 98, 'Pedro': 91, 'Carla': 78}
# Acima nós pegamos a maior nota de cada aluno usando o 'max()' e juntamos uzando o 'zip()'


# Podemos utilizar o map() para fazer isso
final = zip(alunos, map(lambda nota: max(nota), zip(prova1, prova2)))
print(dict(final))
# Resposta: {'Maria': 98, 'Pedro': 91, 'Carla': 78}

