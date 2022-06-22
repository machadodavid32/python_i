"""
Trabalhando com módulos built-in (módulos integrados que já vem instalado no Python)

# Utilizando alias (apelido) para modulos/funções
import random as rdm

print(rdm.random())  # Aqui era print(random.random()), porém, o modulo random foi renomeado como 'rdm'



# Podemos importar todas as funções de um módulo usando o asterisco *

from random import *
print(random())  # Reparar que aqui, neste caso do asterisco, não precisamos colocar random.random()
# Resposta: 0.45105912674111104 (a numeração vai variando)



# Importanto todo o modulo

import random
print(random.random())
# Resposta: 0.6285809711619422



# Utilizando alias (apelido) para modulos / funções
from random import randint as rdi  # Aqui apelidamos a função randint
print(rdi(5, 89))
# Reposta: 5 (vai variando)


from random import randint as rdi, random as rdm  # Aqui estamos renomeando módulo e função.
print(rdm())
# Resposta: 0.6234527597509147

"""

# Costumamos utilizar tuple para colocar multiplos imports de um mesmo modulo

from random import (
    random,
    randint,
    shuffle,
    choice
)
# E colocamos na mesma forma acima

print(random())
# reposta: 0.15400572483956665
print(randint(8, 115))
# Resposta: 14
lista = ['geek', 'univerisity', 'python']
shuffle(lista)
# Resposta: ['python', 'univerisity', 'geek']

print(lista)
# Reposta: ['python', 'univerisity', 'geek']
print(choice('univerisity'))
# Resposta: r


