"""
Reversed

obs: Não confunda com a função reverse() que estudamos na lista. A Função reverse() só funciona nas listas.
Já a função reversed() função com qualquer iterável.

Sua função é inverter o iterável

A Função reversed() retorna um iteŕavel chamado List Reverse iterator
"""

# Exemplos

lista = [1, 2, 3, 4, 5]
res = reversed(lista)
print(res)
print(type(res))

# Resposta: <list_reverseiterator object at 0x7fb2f7da5f60>
# <class 'list_reverseiterator'>


# Podemos converter o elemento retornado para uma lista, tupla ou conjunto.

# Lista
print(list(reversed(lista)))
# Resposta: [5, 4, 3, 2, 1]

# Tupla
print(tuple(reversed(lista)))
# Resposta: (5, 4, 3, 2, 1)

# Conjunto (set)
print(set(reversed(lista)))
# Resposta: {1, 2, 3, 4, 5}  Obs: Aqui não reverte pois o Set não guarda a ordem dele

# Podemos iterar sobre o reversed
for letra in reversed("Geek University"):
    print(letra, end='')  # O comando 'end' serve para ficar tudo na mesma linha
# Resposta: ytisrevinU keeG

print('\n')
# Podemos fazer o mesmo sem o uso do for
print('Geek University'[::-1])
# Resposta: ytisrevinU keeG


# Podemos também utilizar o reversed() para fazer um loop reverso
for n in reversed(range(0, 10)):
    print(n)
# Resposta:9
# 8
# 7
# 6
# 5
# 4
# 3
# 2
# 1
# 0


# Apesar que também ja vimos como fazer isso utlizando o proprio range
for n in range(9, -1, -1):
    print(n)
# Resposta:9
# 8
# 7
# 6
# 5
# 4
# 3
# 2
# 1
# 0


