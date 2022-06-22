"""
Teste de velocidade com expressões geradoras



# Generators (geradores)


def nums():
    for num in range(1, 10):
        yield num


ge1 = nums()
print(ge1)
print(next(ge1))
print(next(ge1))
# REsposta:
# <generator object nums at 0x7f105742a110>   feito através da função nums
# 1
# 2


ge2 = (num for num in range(1, 10))
print(ge2)
print(next(ge2))
print(next(ge2))
# Resposta:  <generator object <genexpr> at 0x7fef344ddbd0>   feito através de uma expressão geradora
# 1
# 2

"""

# Realizando teste de velocidade importanto time

import time

print(sum(num for num in range(1, 40)))  # Exemplo de expressão geradora
# REsposta: 780  soma de todos os numeros de 1 a 39


# Generator expression
gen_inicio = time.time()
print(sum(num for num in range(1, 100000000)))  # 100 milhões
gen_tempo = time.time() - gen_inicio

# list comprehesion
list_inicio = time.time()
print(sum([num for num in range(100000000)]))  # 100 milhões
list_tempo = time.time() - list_inicio

print(f'Generator expression levou {gen_tempo}')
print(f'list expression levou {list_tempo}')

# Resposta: 4999999950000000
# 4999999950000000
# Generator expression levou 3.863361358642578
# list expression levou 4.198683977127075

