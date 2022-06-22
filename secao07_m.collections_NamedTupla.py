"""
Modulo Collections - Named Tuple

Relembrando tupla
tupla = (1, 2, 3)

print(tupla[1})

Named Tuple > São tuplas diferenciadas onde especificamos um nome para a mesma e também parametros


"""

#Importanto
from collections import namedtuple

#Precisamos definir  o nome e parametros

#FORMA1 - Declaração Named Tuple

cachorro = namedtuple('cachorro', 'idade raça nome')

#FORMA2 - Declaração Named Tuple também

cachorro = namedtuple('cachorro', 'idade, raça, nome')

#FORMA3 -Declaração de Named Tuple

cachorro = namedtuple('cachorro', ['idade', 'raça', 'nome'])

#Usando

ray = cachorro(idade=2, raça='chow', nome="Ray")
print(ray)

#Resposta: cachorro(idade=2, raça='chow', nome='Ray')


#Acessando os dados

#FORMA1
print(ray[0]) #Como ja explicado, aqui vamos pegar o elemento zero, no caso, idade
print(ray[1]) #Aqui pegaremos raça
print(ray[2]) #aqui pegaremos nome.
#Rsposta:
# 2
# chow
# Ray

#FORMA2
print(ray.idade)
print(ray.raça)
print(ray.nome)
#Resposta:
# 2
# chow
# Ray

#Descobrindo o index(Ja eplicado em tuplas

print(ray.index('chow'))
#Resposa: 1  > chow está no indice 1

print(ray.count('chow')) # Quantas ocorrências a este termo?
#Reposta: 1  > Ou seja, apenas uma ocorrência