"""
Generator Expression -
Em aulas anteriores, nós estudamos list comprehension, dicionary comprehension e set comprehension.

Não vimos:
  Tuple comprehension ...pois elas se chamam Generetors
   nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina', 'Vanessa']
print(any([nome[0] == 'C' for nome in nomes]))

No exemplo acima, poderiamos ter feito utilizando Generators

nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina', 'Vanessa']
print(any(nome[0] == 'C' for nome in nomes))
# Resposta: True -> comando acima utilizando o generators

res = [(nome[0] == 'C' for nome in nomes)]
print(type(res))
# Resposta: <class 'list'>

res = (nome[0] == 'C' for nome in nomes)
print(type(res))
# Resposta: <class 'generator'>

# Acima a diferença é que o 'generator' ocupa menos recursos na memoria



# Qual é a utilidade do getsizeof() -> Retorna a quantidade de bytes em memoria dos elementos

from sys import getsizeof

# Gerando uma lista de numeros com List comprehesion
list_comp = getsizeof([x * 10 for x in range(1000)])

# Gerando uma lista de numeros com set comprehesion
set_comp = getsizeof({x * 10 for x in range(1000)})

# Gerando uma lista de numeros com dicionary comprehesion
dic_comp = getsizeof({x: x * 10 for x in range(1000)})

# Gerando uma lista de numeros com generator
gen = getsizeof(x * 10 for x in range(1000))

print('Para fazer a mesma tarefa gastamos em memoria: ')
print(f'List Comprehension: {list_comp} bytes')
print(f'set Comprehension: {set_comp} bytes')
print(f'Dic Comprehension: {dic_comp} bytes')
print(f'Generator Expression: {gen} bytes')

# Resposta: Para fazer a mesma tarefa gastamos em memoria:
# List Comprehension: 8856 bytes
# set Comprehension: 32984 bytes
# Dic Comprehension: 36960 bytes
# Generator Expression: 104 bytes

"""

# Eu posso iterar no generator expression?

gen = (x * 10 for x in range(100))
print(gen)
print(type(gen))

for num in gen:
    print(num)

# Resposta: varios numeros de 10 em 10 até chegar em 990 (10, 20, 30, 40, .....990)
