"""

list comprehension - Utilizando list comprehension nós podemos gerar novas listas com dados processados a partir
de outro iteŕavel.

Sintaxe da lista comprehension - [ dado for dado iterável ]



#Exemplos

numeros = [1, 2, 3, 4, 5]

res = [numero * 10 for numero in numeros]

print(res)
#Resposta: [10, 20, 30, 40, 50]

# Para entender melhor o que está acontencendo acima, devemos dividir a expressão em duas partes:

# - A primeira parte, for numero in numeros
# - A segunda parte, numero * 10



res = [numero / 2 for numero in numeros]
print(res)
#Resposta: [0.5, 1.0, 1.5, 2.0, 2.5]

def funcao(valor):
    return valor * valor


res = [funcao(numero) for numero in numeros]

print(res)

# Resposta: [1, 4, 9, 16, 25]




# Lista comprehensions vs loop


# loop
numeros = [1, 2, 3, 4, 5,]
numeros_dobrados = []

for numero in numeros:
    numero_dobrado = numero * 2
    numeros_dobrados.append(numero_dobrado)

print(numeros_dobrados)
# Resposta: [2, 4, 6, 8, 10]

# List Comprehensions
print([numero * 2 for numero in numeros])  # O resultado é o mesmo do comando acima, porém, em uma linha.
# Resposta: [2, 4, 6, 8, 10]


# Outro modo de fazer é eliminando a lista numeros e recolocando direto no print, conforme abaixo:
print([numero * 2 for numero in [1, 2, 3, 4, 5]])
# Resposta: [2, 4, 6, 8, 10]

"""

# Outros Exemplos:

# Primeiro:
nome = 'Geek Univeristy'

print([letra.upper() for letra in nome])
# Resposta: ['G', 'E', 'E', 'K', ' ', 'U', 'N', 'I', 'V', 'E', 'R', 'I', 'S', 'T', 'Y']

# Segundo:
amigos = ['maria', 'julia', 'pedro', 'guilherme', 'vanessa']
print([amigo[0].upper() for amigo in amigos])
# Resposta: ['M', 'J', 'P', 'G', 'V']


# Terceiro:
def caixa_alta(nome):
    nome = nome.replace(nome[0], nome[0].upper())
    return nome


amigos = ['maria', 'julia', 'pedro', 'guilherme', 'vanessa']
print([caixa_alta(amigo) for amigo in amigos])
# Resposta: ['Maria', 'Julia', 'Pedro', 'Guilherme', 'Vanessa']


# Quarto:
print([numero * 3 for numero in range(1, 10)])
# Resposta: [3, 6, 9, 12, 15, 18, 21, 24, 27]


# Quinto:
print([bool(valor) for valor in [0, [], '', True, 1, 3, 14]])
# Aqui estamos transformando todos os objetos da lista em booleanos (True e False)
# Resposta: [False, False, False, True, True, True, True]

# Sexto
print([str(numero) for numero in [1, 2, 3, 4, 5]]) # Transforma os numeros dentro da lista em strings
# Resposta: ['1', '2', '3', '4', '5']
