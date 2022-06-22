"""
Modulo Collections: Ordered Dict

#Em um dicionario, a ordem de inserção dos elementos não é garantida
dicionario = { 'a': 1, 'b': 2, 'c': 3, '4': 5}

for chave, valor in dicionario.items():
    print(f'chave = {chave}: valor = {valor}')

#REsposta: chave = a: valor = 1
# chave = b: valor = 2
# chave = c: valor = 3
# chave = 4: valor = 5



#Fazendo o import

from collections import OrderedDict

dicionario = OrderedDict({'a': 1, 'b': 2, 'c': 3, 'd': 4})
for chave, valor in dicionario.items():
    print(f'chave={chave}: valor={valor}')

#Resposta:
# chave=a: valor=1
# chave=b: valor=2
# chave=c: valor=3
# chave=d: valor=4

"""

#Entendo a diferença entre Dict e OrderedDict

dicionario1 = {'a':1, 'b': 2}
dicionario2 = {'b': 2, 'a': 1}
print(dicionario1 == dicionario2)
#Resposta: True > Já que a ordem do elementonão importa no dicionario

from collections import OrderedDict
odicionario1 = OrderedDict({'a':1, 'b': 2})
odicionario2 = OrderedDict({'b': 2, 'a': 1})
print(odicionario1 == odicionario2)
#Resposta: False > Já que a ordem dos elementos importa para OrderedDict

