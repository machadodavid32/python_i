
""" 1 - Crie uma lista com até 8 numeros e mostre na tela"""
lista = [1, 10, 3, 11, 5, 6, 99, 8]
print(lista)
#resposta: [1, 10, 3, 11, 5, 6, 99, 8]

"""" 2 - Crie duas listas e mostre na tela"""
lista1 = [5, 100, 3, 98, 5]
lista2 = [5, 41, 55, 210, 8]
print(lista1, lista2)
#Resposta: [5, 100, 3, 98, 5] [5, 41, 55, 210, 8]

"""3 - procure um valor na lista1"""
num = 7
if num in lista1:
    print("Encontrei o numero")
else:
    print("Não encontrei o numero")
#Resposta: Não encontrei o numero


"""4 - Ordene as listas e mostre """
lista.sort()
lista1.sort()
lista2.sort()
print(lista1, lista, lista2)
#Resposta: [3, 5, 5, 98, 100] [1, 3, 5, 6, 8, 10, 11, 99] [5, 8, 41, 55, 210]

"""5 - Adicione um numero na lista2"""
lista2.append(980)
print(lista2)
#Resposta: [5, 8, 41, 55, 210, 980]

"""6 - Adicione uma lista dentro de outra lista"""
lista1.append([320, 330])
print(lista1)
#Resposta: [3, 5, 5, 98, 100, [320, 330]]

"""7 - Adicione 3 numeros na lista"""
lista.extend([750, 450, 550])
print(lista)
#Resposta: [1, 3, 5, 6, 8, 10, 11, 99, 750, 450, 550]

"""8 - Adcione um novo elemento na lista2, na posição 3"""
lista2.insert(3, 'novo valor')
print(lista2)
#Resposta: [5, 8, 41, 'novo valor', 55, 210, 980]

"""9 - Crie uma lista com strings"""
listaS = ['d', 'a', 'v', 'i', 'd']
print(listaS)
#Resposta: ['d', 'a', 'v', 'i', 'd']

"""10 - Junte duas listas de duas formas diferentes"""
listaj = (listaS + lista2)
print(listaj)
#Resposta: ['d', 'a', 'v', 'i', 'd', 5, 8, 41, 'novo valor', 55, 210, 980] #precisou criar outra lista

lista1.extend(lista)
print(lista1)
#Resposta: [3, 5, 5, 98, 100, [320, 330], 1, 3, 5, 6, 8, 10, 11, 99, 750, 450, 550]


"""11 - Imprima uma lista de forma inversa"""
lista1.reverse()
print(lista1)
#Resposta: [550, 450, 750, 99, 11, 10, 8, 6, 5, 3, 1, [320, 330], 100, 98, 5, 5, 3]

"""12 - Faça a inversão utilizando o Slice"""
print(listaS[::-1])
#resposta: ['d', 'i', 'v', 'a', 'd']

"""13 - Inverta outra lista usando Slice"""
print(lista2[::-1])
#Resposta: [980, 210, 55, 'novo valor', 41, 8, 5]

"""14 - Copiar uma lista """
lista_copia = listaS.copy()
print(lista_copia)
#Resposta: ['d', 'a', 'v', 'i', 'd']

"""15 - Como fazer para contar um tamanho de uma lista? """
print(len(listaS))
#Resposta: 5

"""16 - Tamanho de outra lista """
print(len(lista1))
#Resposta: 17

"""17 - Remova o ultimo elemento de uma lista """
lista_copia.pop()
print(lista_copia)
#Resposta: ['d', 'a', 'v', 'i']

"""18 - Remova o primeiro elemento de uma lista"""
lista_copia.pop(0)
print(lista_copia)
#Resposta: ['a', 'v', 'i']  Neste caso removemos pelo indice

"""19 - Limpe uma lista, deixando zerada"""
lista_copia.clear()
print(lista_copia)
#Resposta: []

"""20 - Adicione elementos para a lista zerada"""
lista_copia = ['David é programador']
print(lista_copia)

"""21 - Replicar os dados dentro de uma lista em 2"""
listaS = listaS * 2
print(listaS)
#resposta: ['d', 'a', 'v', 'i', 'd', 'd', 'a', 'v', 'i', 'd']

"""22 - Crie uma string e Converta uma string em uma lista"""
curso = "curso de python"
print(curso)
curso = curso.split()
print(curso)
#Resposta: curso de python
# ['curso', 'de', 'python']

""" 23 - Crie outra string e converta em uma lista"""
gabriela = "Não dê corda"
print(gabriela)
gabriela = gabriela.split()
print(gabriela)
#Resposta: Não dê corda
# ['Não', 'dê', 'corda']

"""24 - Faça uma lista com elementos misturados """
lista_misturada = ["David é gato", 55, 87, 1001, 48, ['david']]
print(lista_misturada)
#Resposta: ['David é gato', 55, 87, 1001, 48, ['david']]


"""25 - Soma os elementos de uma lista"""
listadesoma = [10, 20, 30, 50]
soma = 0
for elemento in listadesoma:
    print(elemento)
    soma = soma + elemento
print(f'A soma da lista é {soma}')
#Resposta:
# 10
# 20
# 30
# 50
# A soma da lista é 110

"""26 - Crie uma lista com strings e faça a soma"""
listastring = ['David', 'ama', 'Aline']
print(listastring)
soma = ' '
for elemento in listastring:
    print(elemento)
    soma = soma + elemento
print(soma)
#Resposta: ['David', 'ama', 'Aline']
# David
# ama
# Aline
# DavidamaAline

"""27 - Adicionando produtos na lista
carrinho = []
produto = ' '
while produto != 'sair':
    print("Informe o produto ou digite 'sair':")
    produto = input()
    if produto != 'sair':
        carrinho.append(produto)
for produto in carrinho:
        print(produto)
#Resposta: Informe o produto ou digite 'sair':
# playsta
# playsta
# Informe o produto ou digite 'sair':
# corrida
# playsta
# corrida
# Informe o produto ou digite 'sair':
# baeado
# playsta
# corrida
# baeado
"""

"""28 - Acessar os elementos das listas pelos indices """
print(listaj[5])
print(lista2[3])
#Resposta: 5
#novo valor

"""29 - Criar uma lista com algumas strings e gerar visualização de indice e elemento"""
animais = ['cachorro', 'gato', 'pato', 'elefante']
indice = 0
for indice, pet in enumerate(animais):
    print(indice, pet)
#Resposta:
# 0 cachorro
# 1 gato
# 2 pato
# 3 elefante

"""30 - Encontrar o indice pelo elemento"""
nomes = ['david', 'aline', 'miguel', 'luana']
print(nomes.index('luana'))
#Resposta: 3


