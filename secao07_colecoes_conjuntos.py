"""
Conjuntos
- conjuntos em qualquer linguagem de programação, estamos fazendo referências as teorias dos conjuntos da matematica

Aqui no Python, os conjuntos são chamados de Sets.
Dito isto, da mesma forma que na matemática:
- Sets(conjuntos) não possuem valores duplicados
- Sets(conjuntos) não possuem valores ordenados
- elementos não são acessados via indice, ou seja, conjuntos não são indexados

Conjuntos são bons para se utilizar quando precisamos armazenar elementos mas não nos importamos com
a ordenação deles. Quando não precisamos se preocupar com chaves, valores e iténs duplicados.

Os Conjuntos(Sets) são referenciados em python como chaves{}

Diferenças entre conjuntos(Sets) e mapas(Dicionários) em python:
- Um dicionário tem chaves e mapas
- Um conjunto só tem valor



# - Definindo um conjunto

#FORMA 1 -
s = set({1, 2, 3, 4, 5, 6, 7, 2, 3})
print(s)
#Resposta: {1, 2, 3, 4, 5, 6, 7} - Reparar que os numeros repetidos não aparecem


#FORMA 2 - Mais comum

s = {1, 2, 3, 4, 5, 5}
print(s)
print(type(s))
#Resposta:
# {1, 2, 3, 4, 5}
# <class 'set'>

#Podemos verificar se determinado elemento está contido num conjunto

if 3 in s:
    print('Tem o 3')
else:
    print('Não tem o 3')
 #Resposta: Tem o 3



#Importante lembrar que, além de não termos valores duplicados, não temos ordem
from typing import List


lista = [99, 2, 34, 23, 2, 12, 1, 44, 5, 34]
print(f'lista: {lista} com {len(lista)} elementos')

tupla = (99, 2, 34, 23, 2, 12, 1, 44, 5, 34)
print(f'Tupla : {tupla} com {len(tupla)} elementos')
dicionario = {}.fromkeys([99, 2, 34, 23, 2, 12, 1, 44, 5, 34], 'dict')
print(f'Dicionario : {dicionario} com {len(dicionario)} elementos')

conjunto = {99, 2, 34, 23, 2, 12, 1, 44, 5, 34}
print(f'Conjunto : {conjunto} com {len(conjunto)} elementos')

#Resposta
#lista: [99, 2, 34, 23, 2, 12, 1, 44, 5, 34] com 10 elementos
# Tupla : (99, 2, 34, 23, 2, 12, 1, 44, 5, 34) com 10 elementos
# Dicionario : {99: 'dict', 2: 'dict', 34: 'dict', 23: 'dict', 12: 'dict', 1: 'dict', 44: 'dict', 5: 'dict'} com 8 elementos (pois dicionário não repete chaves)
# Conjunto : {1, 2, 99, 34, 5, 12, 44, 23} com 8 elementos (com 8 elementos pois conjunto não repete valores)



#Assim como todo outro conjunto python, podemos colocar tipos de dados misturados em sets

s = {1, 'b', True, 34.22, 44, 5}
print(s)
print(type(s))
#Resposta:
#{1, 34.22, 'b', 44}
#<class 'set'>

#Podemos iterar em um set normalmente
for valor in s:
    print(s)
#{1, 34.22, 5, 'b', 44}
# {1, 34.22, 5, 'b', 44}
# {1, 34.22, 5, 'b', 44}
# {1, 34.22, 5, 'b', 44}
# {1, 34.22, 5, 'b', 44}



#Usos interessantes com Sets

#Imagine que fizemos um formulario de cadastro de visitantes em uma feira ou museu.  Os visitantes informam
#manualmente a cidade de onde vieram. Nós adicionamos cada cidade em uma lista Python, ja que em uma lista podemos
#adicionar novos elementos e ter repetição.

cidades = ['Belo Hozrizonte', 'São Paulo', 'Cuiaba', 'São Paulo', 'Campo Grande', 'Cuiaba', 'Campo Grande']
print(cidades)
print(len(cidades))
#Resposta:
# ['Belo Hozrizonte', 'São Paulo', 'Cuiaba', 'São Paulo', 'Campo Grande', 'Cuiaba', 'Campo Grande']
# 7

#Agora precisamos saber quantas cidades distintas, ou seja, unicas, temos.
#O que você faria? Faria um loop na lista?
#Faria um Set para isso

print(len(set(cidades))) #Lembre-se, o set nao aceita duplicidade de elementos. Por isso deu a resposta 4
#Resposta: 4



#Listas aceitam valores duplicados, então temos 10 elementos. A Lista guarda a ordem que foi informada.
lista = [99, 2, 34, 23, 2, 12, 1, 44, 5, 34]
print(f'lista: {lista} com {len(lista)} elementos')

#Tuplas aceitam valores duplicados, então temos 10 elementos. A tupla guarda a ordem que foi informada
tupla = (99, 2, 34, 23, 2, 12, 1, 44, 5, 34)
print(f'Tupla : {tupla} com {len(tupla)} elementos')

#Dicionários não aceitam valores duplicados, então temos 8 elementos. O dicionário também guarda essa ordem
dicionario = {}.fromkeys([99, 2, 34, 23, 2, 12, 1, 44, 5, 34], 'dict')
print(f'Dicionario : {dicionario} com {len(dicionario)} elementos')

#Conjuntos não aceitam valores duplicados, então temos 8 elementos. O conjunto não guarda a ordem. É aleatório.
conjunto = {99, 2, 34, 23, 2, 12, 1, 44, 5, 34}
print(f'Conjunto : {conjunto} com {len(conjunto)} elementos')

#lista: [99, 2, 34, 23, 2, 12, 1, 44, 5, 34] com 10 elementos
# Tupla : (99, 2, 34, 23, 2, 12, 1, 44, 5, 34) com 10 elementos
# Dicionario : {99: 'dict', 2: 'dict', 34: 'dict', 23: 'dict', 12: 'dict', 1: 'dict', 44: 'dict', 5: 'dict'} com 8 elementos
# Conjunto : {1, 2, 99, 34, 5, 12, 44, 23} com 8 elementos




#Adicionando elementos em um conjunto
s = {1, 2, 3}
s.add(4)
print(s)
#Resposta: {1, 2, 3, 4}


#Remover elementos em um conjunto
s = {1, 2, 3}
print(s)

#FORMA1
s.remove(3)
print(s)
#Resposta: {1, 2}
#Obs: Ao remover um elemento que não exista, da erro.

#FORMA2

s.discard(2)
print(s)
#Resposta: {1}
ObS: Ao tentar remover um valor que não existe, neste caso, não há geração de erro.



#Copiando um conjunto para o outro

s = {1, 2, 3}
print(s)

#FORMA1 - Deep copu

novo = s.copy() #Copia e cria um conjunto totalmente diferente
print(novo)

novo.add(4)

print(novo)
print(s)
#Resposta: {1, 2, 3}
# {1, 2, 3}
# {1, 2, 3, 4}
# {1, 2, 3}


#FORMA2 = Shallow copy
s = {1, 2, 3}
print(s)

novo = s  #no Shallow copy, ao adicionar elementos na copia, o orignal também é modificado.
novo.add(4)

print(novo)
print(s)
#Resposta: {1, 2, 3}
# {1, 2, 3, 4}
# {1, 2, 3, 4}



#Podemos remover todos os elementos de um conjuntod
s = {1, 2, 3}
print(s)
s.clear()
print(s)
#Resposta:
# {1, 2, 3}
# set()



#Métodos matematicos de conjuntos

#Imagine que temos dois conjuntos: Um contendo estudantes do curso Python e outro do curso de Java

estudantes_pythom = {'Marcos', 'Patricia', 'Ellen', 'Pedro', 'Julia', 'Guilherme'}
estudantes_java = {'Fernando', 'Gustavo', 'Julia', 'Patricia'}

#Veja que alguns aluno que estudam Python também estudam Java

#Precisamos gerar um conjunto com nomes de estudantes unicos

#FORMA 1 - Utilizando Union

unicos1 = estudantes_pythom.union(estudantes_java)
print(unicos1)
#Resposta: {'Ellen', 'Fernando', 'Pedro', 'Gustavo', 'Marcos', 'Julia', 'Guilherme', 'Patricia'}

#FORMA2 - Utilizando o caractere pipe |
unicos2 = estudantes_pythom | estudantes_java
print(unicos2)
#resposta: {'Julia', 'Gustavo', 'Fernando', 'Ellen', 'Guilherme', 'Pedro', 'Marcos', 'Patricia'}



#Métodos matematicos de conjuntos

#Imagine que temos dois conjuntos: Um contendo estudantes do curso Python e outro do curso de Java

#Gerar um conjunto de estudantes que estão nem ambos os cursos


estudantes_pythom = {'Marcos', 'Patricia', 'Ellen', 'Pedro', 'Julia', 'Guilherme'}
estudantes_java = {'Fernando', 'Gustavo', 'Julia', 'Patricia'}

#FORMA1 - utilizando o intersection
ambos1 = estudantes_pythom.intersection(estudantes_java)
print(ambos1)
#Resposta: {'Julia', 'Patricia'}

#FORMA2 - UTILIZANDO O &

ambos2 = estudantes_pythom & estudantes_java
print(ambos2)
#Resposta: {'Julia', 'Patricia'}


#Métodos matematicos de conjuntos

#Imagine que temos dois conjuntos: Um contendo estudantes do curso Python e outro do curso de Java

#Gerar um conjunto de estudantes que NÃO estão nem ambos os cursos


estudantes_pythom = {'Marcos', 'Patricia', 'Ellen', 'Pedro', 'Julia', 'Guilherme'}
estudantes_java = {'Fernando', 'Gustavo', 'Julia', 'Patricia'}

so_python = estudantes_pythom.difference(estudantes_java)
print(so_python)
#Resposta: {'Marcos', 'Guilherme', 'Ellen', 'Pedro'} > Só estudam Python

so_java = estudantes_java.difference(estudantes_pythom)
print(f'Só fazem o curso de Java {so_java}')
#Resposta: {'Gustavo', 'Fernando'}  > Só estudam java

"""

# Soma*, maior_valor*, menor_valor*, tamanho
# * Se os valores forem todos inteiros ou reais

s = {1, 2, 3, 4, 5, 6}
print(sum(s))
#Resposta: 21

s = {1, 2, 3, 4, 5, 6}
print(max(s))
#Resposta: 6

s = {1, 2, 3, 4, 5, 6}
print(min(s))
#resposta: 1
s = {1, 2, 3, 4, 5, 6}
print(len(s))
#Resposta: 6



