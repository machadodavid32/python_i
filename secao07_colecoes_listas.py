""""
Listas em Python funcionam como vetores e matrizes (arrays) em outras linguagens, com a diferença de
serem dinamicos e também podermos colocar qualqyuer tipo de dado

Lignguagens C e java - Arrays possuem o tamanho e o tipo de dados fixos. Ou seja, nestas linguagens
se você criar um array do tipo int com tamanho 5, este array será sempre do mesmo tipo inteiro e sempre
será de no máximo 5 valores.

Ja em Python:

- dinamico: Não possui tamanho fixo, ou seja, podemos criar a lista e simplesmente ir colocando elementos.
- Qualquer tipo de dado: As listas não possuem tipo de dado fixo, ou seja, podemos colocar qualquer tipo de dado.

As listas em Python são representadas por colchetes: []



lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]

lista2 = ['G', 'e', 'e', 'k', ' ', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']

lista3 = []

lista4 = list(range(11))

lista5 = list('Geek University')

#Podemos facilmente checar se determinado valor está contido na lista
num = 7
if num in lista4:
    print(f"Encontrei o numero {num}")
else:
    print(f"Não encontrei o numero {num}")

#Podemos facilmente ordenar uma lista, conforme abaixo, com o comando 'sort'

lista1.sort()
print(lista1)

# Podemos facilmente contar o numero de ocorrências de um valor em uma lista, com o comando 'count', coforme abaixo

#Existem varios comandos para ordenar listas, eu encontro em dir(list) no terminal

para adicionar elementos na lista, utilizamos a função 'append'


print(lista1)
lista1.append(42)
print(lista1)

#OBS: Com append, só conseguimos colocar um elemento por vez, no caso acima, somente o numero 42.
#Porém é possivel incluir uma outra lista dentro da lista, conforme abaixo

lista1.append([8, 3, 1])
print(lista1)

if [8, 3, 1] in lista1:
    print("Encontrei a lista")
else:
    print("Não encontrei a lista")

lista1.extend([123, 44, 67]) #o comando extend adiciona uma lista igual ao append, porém, de forma individual e não como um elemento unico igual o append
print(lista1)

#O extend é usado somente para incluir varios valores. Se usar para incluir um valor somente, ele dá erro.
"""

"""
lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]

lista2 = ['G', 'e', 'e', 'k', ' ', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']

lista3 = []

lista4 = list(range(11))

lista5 = list('Geek University')

#Podemos adicionar um novo elemento na lista informando a posição da lista, segue abaixo.

lista1.insert(2, 'novo valor')
print(lista1)

#resultado: [1, 99, 'novo valor', 4, 27, 15, 22, 3, 1, 44, 42, 27] - inserido outro valor na posição 2, sem substituir o anterior
#o outro valor foi deslocado para a direita da lista

"""

"""
#Podemos facilmente juntar as listas

lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]

lista2 = ['G', 'e', 'e', 'k', ' ', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']

lista3 = []

lista4 = list(range(11))

lista5 = list('Geek University')

lista6 = lista1 + lista2
print(lista6)

#resultado: [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27, 'G', 'e', 'e', 'k', ' ', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']

#O comando extend faz a mesma coisa da seguinte forma

lista1.extend(lista5)
print(lista1)

#Resultado: [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27, 'G', 'e', 'e', 'k', ' ', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']
#Porém não foi criado uma nova lista

"""


""""
lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]

lista2 = ['G', 'e', 'e', 'k', ' ', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']

lista3 = []

lista4 = list(range(11))

lista5 = list('Geek University')

#Imprimir a lista de forma inversa
lista1.reverse()
lista2.reverse()

print(lista1)
print(lista2)

#Resultado: [27, 42, 44, 1, 3, 22, 15, 27, 4, 99, 1]
['y', 't', 'i', 's', 'r', 'e', 'v', 'i', 'n', 'U', ' ', 'k', 'e', 'e', 'G']

#Existe outra forma de fazer isso, com o 'slice'
print(lista1[::-1])
print(lista2[::-1])

#Resultado: [27, 42, 44, 1, 3, 22, 15, 27, 4, 99, 1]
['y', 't', 'i', 's', 'r', 'e', 'v', 'i', 'n', 'U', ' ', 'k', 'e', 'e', 'G']

"""

"""
lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]

lista2 = ['G', 'e', 'e', 'k', ' ', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']

lista3 = []

lista4 = list(range(11))

lista5 = list('Geek University')

#Copiar uma lista

lista6 = lista2.copy()
print(lista6)

#resultado: ['G', 'e', 'e', 'k', ' ', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']

"""

"""
lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]

lista2 = ['G', 'e', 'e', 'k', ' ', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']

lista3 = []

lista4 = list(range(11))

lista5 = list('Geek University')

#Para saber o tamanho de uma lista, para contar quantos elementos temos dentro de uma lista

print(len(lista1))
#resultado: 11 - a lista1 tem 11 elementos

print(len(lista2))
#resultado: 15

"""

"""
lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]

lista2 = ['G', 'e', 'e', 'k', ' ', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']

lista3 = []

lista4 = list(range(11))

lista5 = list('Geek University')

#Podemos facilmente remover o ultimo elemento de uma lista, com o comando 'pop'
#OBS: O 'pop' não somente remove o elemento, mas também o retorna

print(lista5)
lista5.pop()
print(lista5)
#Resultado: ['G', 'e', 'e', 'k', ' ', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']
['G', 'e', 'e', 'k', ' ', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't']

#Podemos remover o elemento pelo indice
print(lista5)
lista5.pop(2)
print(lista5)
#Resultado: ['G', 'e', 'e', 'k', ' ', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't']
['G', 'e', 'k', ' ', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't']
#OBS: Os elementos da direita deste indice serão deslocados para a esquerda
#OBS: Se não houve elemento no indice informado, da erro de IndexError

"""

"""
lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]

lista2 = ['G', 'e', 'e', 'k', ' ', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']

lista3 = []

lista4 = list(range(11))

lista5 = list('Geek University')

#Podemos facilmente remover os dados de uma lista (zerar a lista)

print(lista5)
lista5.clear()
print(lista5)
#Resultado:
# ['G', 'e', 'e', 'k', ' ', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']
# []

#da pra replicar os elementos dentro da lista

lista1 = lista1 * 3
print(lista1)
#Resultado:
[1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27, 1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27, 1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]

"""

"""

lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]

lista2 = ['G', 'e', 'e', 'k', ' ', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']

lista3 = []

lista4 = list(range(11))

lista5 = list('Geek University')

#Podemos facilmente converter uma string em uma lista

#exemplo1

curso = 'programação em python: Essencial'
print(curso)
curso = curso.split()
print(curso)

#Resultado:
#programação em python: Essencial
#['programação', 'em', 'python:', 'Essencial']

#OBS: Por padrão, o split separa os elementos da lista pelo espaço entre elas

#Exemplo 2

curso = 'programação, em, python:, Essencial'
print(curso)
curso = curso.split(',')
print(curso)
#Resultado:
#programação, em, python:, Essencial
#['programação', ' em', ' python:', ' Essencial']

"""


"""
#Converter uma lista em uma string
lista6 = ['programação', 'em', 'python:', 'essencial']
print(lista6)
#Abaixo estamos falando: pega a lista, coloca espaço entre cada elemento e transforma em uma string
curso = ' '.join(lista6)
print(curso)
#REsultado:
#'programação', 'em', 'python:', 'essencial']
# programação em python: essencial

curso = "$".join(lista6)
print(curso)
#Resultado:
#programação$em$python:$essencial
"""

"""
lista6 = [1, 2, 34, True, 'david', [1,2,3], 46516516]
print(lista6)
#Resposta:
#[1, 2, 34, True, 'david', [1, 2, 3], 46516516]
#Podemos colocar qualquer tipo de dados em uma lista, inclusive misturando os dados
"""

lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]

lista2 = ['G', 'e', 'e', 'k', ' ', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']

lista3 = []

lista4 = list(range(11))

lista5 = list('Geek University')



"""
#Iterando sobre listas


#Exemplo1
for elemento in lista1:
    print(elemento)
#Resposta:
1
99
4
27
15
22
3
1
44
42
27
"""
"""
soma = 0
for elemento in lista1:
    print(elemento)
    soma = soma + elemento
print(soma)
#Resposta:
4
27
15
22
3
1
44
42
27
285

#Soma de strings
soma = ' '
for elemento in lista2:
    print(elemento)
    soma = soma + elemento
print(soma)
#Resposta:
G
e
e
k

U
n
i
v
e
r
s
i
t
y
Geek
University

"""
"""
#EXEMPLO2

carrinho = []
produto = ' '

while produto != 'sair':
    print("Adicione um produto na lista ou digite 'sair' para sair")
    produto = input()
    if produto != 'sair':
        carrinho.append(produto)
for produto in carrinho:
    print(produto)

#Resposta:
Adicione um produto na lista ou digite 'sair' para sair
switch
Adicione um produto na lista ou digite 'sair' para sair
zelda
Adicione um produto na lista ou digite 'sair' para sair
controle switch
Adicione um produto na lista ou digite 'sair' para sair
sair
switch
zelda
controle switch
"""

"""
lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]

lista2 = ['G', 'e', 'e', 'k', ' ', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']

lista3 = []

lista4 = list(range(11))

lista5 = list('Geek University')

#Utilizando variaaveis em uma lista

numeros = [1, 2, 3, 4, 5]
print(numeros)

num1 = 1
num2 = 2
num3 = 3
num4 = 4
num5 = 5

numeros = [num1, num2, num3, num4, num5]
print(numeros)
#Resposta
#[1, 2, 3, 4, 5]
#[1, 2, 3, 4, 5]



lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]

lista2 = ['G', 'e', 'e', 'k', ' ', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']

lista3 = []

lista4 = list(range(11))

lista5 = list('Geek University')


#Em listas fazemos acessos ao elementos de forma indexada

#          0       1      2      3
cores = ['verde', 'amarelo', 'azul', 'branco']
print(cores[0])
print(cores[1])
print(cores[2])
print(cores[3])
#Resposta:
verde
amarelo
azul
branco
"""
"""
#Fazer acesso aos elementos de forma indexada ao reverso

cores = ['verde', 'amarelo', 'azul', 'branco']
print(cores[-1])
#Resposta: branco



cores = ['verde', 'amarelo', 'azul', 'branco']

for cor in cores:
    print(cor)
Resposta:
#verde
#amarelo
#azul
#branco
#indice = 0


indice = 0
while indice < len(cores):
    print(cores[indice])
    indice = indice + 1
Resposta:
verde
amarelo
azul
branco
verde
amarelo
azul
branco


cores = ['verde', 'amarelo', 'azul', 'branco']

#gerar indice em um for
indice = 0
for indice, cor in enumerate(cores):
    print(indice, cor) #estamos gerando indice e elemento lado a lado
Resposta
0 verde
1 amarelo
2 azul
3 branco

#Ou seja, ele pega o 0 e coloca no indice e o elemento verde coloca em cor, pega o 1 e coloca no indice e o
#amarelo em cores, e por ai vai.

cores = list (enumerate(cores)) #Estamos listando os elementos de forma enumerada
Resposta
0 verde
1 amarelo
2 azul
3 branco

#Ou seja, ele pega o 0 e coloca no indice e o elemento verde coloca em cor, pega o 1 e coloca no indice e o
#amarelo em cores, e por ai vai.



#Listas aceitam valores repetidos
lista = []
lista.append(42)
lista.append(42)
lista.append(33)
lista.append(33)
lista.append(42)

print(lista)
#resposta: [42, 42, 33, 33, 42]


#Metodos não tão importantes, mas uteis

#Encontrar um indice de um elemento na lista

numero = [5, 6, 7, 5, 8, 9, 10]

#Em qual indice está o valor 6
print(numero.index(6))
#Em qual indice está o valor 9
print(numero.index(9))

#resposta:
#1
#4

#OBs: Caso não tenha o elemento na lista, dara erro de ValueError

print(numero.index(5)) #Caso tenha dois elementos iguais, ele retorna o indice do primeiro elemento encontrado.
#1
#5
#0 - zero é o primeiro indice onde o numero 5 está


#Podemos fazer buscas dentro de um range, ou seja, qual indice começar a buscar

print(numero.index(5, 1)) #Aqui ele está pedindo o index do numero 5 a partir do indice 1
#resposta: 3  (ou seja, depois do indice 1 só existe o numero 5 no indice 3
#OBs: Caso não tenha o elemento na lista, dara erro de ValueError

#podemos fazer buscar entre dentro de um range, inicio / fim

print(numero.index(8, 3, 6)) #Busccar o indice do valor 8, entre 3 e 3
#Resposta: 4




#Revisão de slicing

#lista[inicio:fim:passo]
#range[inicio:fim:passo]

#Trbalhando com slice na lista com o parametro 'inicio'

lista = [1, 2, 3, 4]
print(lista[1:]) #Iniciando no indice 1 e pegando todos os elementos restantes
#resposta: [2, 3, 4]

print(lista[::]) #Aqui se pega todos os elementos
#resposta: [1, 2, 3, 4]


#Trbalhando com slice na lista com o parametro 'fim'

print(lista[:2]) #começa em 0 e pede até o indice 2 -1(não pega o indice 2
#Resposta: Elementos [1, 2]

print(lista[:4])
#Resposta: [1, 2, 3, 4]

print(lista[:-1])
#Resposta: [1, 2, 3]

print(lista[:-2])
#Resposta: [1, 2]


#Trbalhando com slice na lista com o parametro 'passo'

print(lista[1::2]) #Começa em 1, vai até o final, de 2 em 2
#Resposta: [2, 4]

print(lista[::2]) #Começa em zero, vai até o final, de 2 em 2
#resposta: [1, 3]

print(lista[1:3]) #Começa em 1, pega até o indice 3 - 1
#resposta: Elementos [2, 3]



#Invertendo valores em uma lista

nomes = ['geek', 'university']
nomes[0], nomes[1] = nomes[1], nomes[0]
print(nomes)
#Resposta: ['university', 'geek']

nomes.reverse() #Faz a mesma coisa que o comando acima
print(nomes)
#['geek', 'university']



#soma*, valor maximo*, valor minimo*, tamanho.
# * Se os valores forem todos inteiros ou reais

lista = [1, 2, 3, 4, 5, 6]
print(sum(lista)) #soma
print(max(lista)) #O maximo valor que tem na lista
print(min(lista)) # O minimo valor que tem na lista
print(len(lista)) #O tamanho da lista

#Resposta:
# 21
# 6
# 1
# 6



#Transformar uma lista em tupla

lista = [1, 2, 3, 4, 5, 6]
print(lista)
print(type(lista))

tupla = tuple(lista)
print(tupla)
print(type(tupla))

#Resposta:
#[1, 2, 3, 4, 5, 6]
#<class 'list'>
#(1, 2, 3, 4, 5, 6)
#<class 'tuple'>



#Desempacotamento de listas

lista = [1, 2, 3]
num1, num2, num3 = lista
print(num1)
print(num2)
print(num3)

#Resposta
# 1
# 2
# 3

#OBS: Se tivermos mais elementos para desempacotar do que variavies para receber os valores teremos ValueError
#vale o contrario também


#Copiando uma lista para outra (Shallow Copy e Deep Copy)

#Forma 1 - Deep Copy
lista = [1, 2, 3]
print(lista)

nova = lista.copy()
print(nova)

nova.append(4)
print(lista)
print(nova)

#Resposta:
# #[1, 2, 3]
#[1, 2, 3]
#[1, 2, 3]
#[1, 2, 3, 4]

#Obs: Veja que ao utilizarmos o lista.copy(), copiamos o dado de uma lista para outra, mas elas ficaram
#totalmente independentes, ou seja, modificamos uma lista sem afetar a outra. Isso em python é chamado de
#Deep Copy (copia profunda)




#Forma 2 - Shallow Copy

lista = [1, 2, 3]
print(lista)

nova = lista #copiando
print(nova)

nova.append(4)

print(lista)
print(nova)

#Resposta:
# [1, 2, 3]
#[1, 2, 3]
#[1, 2, 3, 4]
#[1, 2, 3, 4]

#Reparar que neste caso as duas listas foram modificadas. Isso em Pyrhon é chamado de Shallow Copy

"""
