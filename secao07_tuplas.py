"""
tuplas - tuple

Tuplas são parecidas com listas. Existem basicamente duas diferenças:
As tuplas são representadas por parenteses ()
E as Tuplas são imutáveis, ou seja, Isso significa que as tuplas não mudam. Toda operação em uma tupla gera
uma nova tupla



#Cuidado: As Tuplas são representados por parenteses (), mas veja:

tupla1 = (1, 2, 3, 4, 5, 6)
print(tupla1)

print(type(tupla1))

tupla2 = 1, 2, 3, 4, 5, 6
print(tupla2)

print(type(tupla2))

#Resposta
#(1, 2, 3, 4, 5, 6)
#<class 'tuple'>
#(1, 2, 3, 4, 5, 6)
#<class 'tuple'>

#Mesmo sem parenteses, gerou uma tupla

#Cuidado 2: Tuplas com um elemto

tupla3 = (4) #Isso não é uma tupla
print(tupla3)

print(type(tupla3))
#resposta:
#4
#<class 'int'>

tupla4 = (4, ) #isso é uma tupla
print(tupla4)

print(type(tupla4))
#Resposta:
#(4,)
#<class 'tuple'>

#CONCLUSÃO - podemos definir que tuplas são definidas pela virgula e não pelos parenteses

tupla5 = (4, )
print(tupla5)

print(type(tupla5))
#resposta:
#(4,)
#<class 'tuple'>

#Podemos gerar uma tupla dinamicamente com range
tupla = tuple(range(11))
print(tupla)
#Resposta: (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)



#Desempacotamento de tupla

tupla = ('Geek University', 'Programação em Python: Essencial')
escola, curso = tupla
print(escola)
print(curso)

#Resposta:
#Geek University
#Programação em Python: Essencial
#OBS: Vai gerar ValeuError se colocarmos numeros diferentes para desempacotar

# Métodos para adição e remoção de elementos nas tuplas não existem. São imutáveis as tuplas.




# Soma*, valor_maximo*, Valor_minimo* e tamanho
# * Se os valores forem reais, se colocar uma letra, por exemplo, da erro. Só consegue executar ao medir o tamanho
#da tupla, com o comando 'len'

tupla = (1, 2, 3, 4, 5, 6)
print(sum(tupla))
print(max(tupla))
print(min(tupla))
print(len(tupla))
#Resposta: 21   6    1    6




#Concatenação de tuplas (juntar as tuplas)

tupla1 = (1, 2, 3)
print(tupla1)
tupla2 = (4, 5, 6,)
print(tupla2)

print(tupla1 + tupla2)
print(tupla1)
print(tupla2)

#resposta:
# (1, 2, 3)
#(4, 5, 6)
#(1, 2, 3, 4, 5, 6)
#(1, 2, 3)
#(4, 5, 6)
#Resultado é que consigo juntar, mas não consigo mudar. Mas posso criar outra tupla.
tupla3 = tupla1 + tupla2
print(tupla3)
#resposta: (1, 2, 3, 4, 5, 6)

#Mas da pra alterar uma tupla dessa forma:
tupla1 = tupla1 + tupla2
print(tupla1)
#resposta: (1, 2, 3, 4, 5, 6) tupla 1 foi alterada



#Verificar se determinado elemento está contido na tupla

tupla = (1, 2, 3)
print(3 in tupla)
#resposta: True

print(4 in tupla)
#Resposta: False



#Iterando sobre uma tupla

for n in tupla: #Para cada n numa tupla
    print(n)
#Resposta:
# 1
# 2
# 3

for indice, valor in enumerate(tupla):
    print(indice, valor)
#resposta:
#0 1
#1 2
#2 3



# Contando elementos dentro de uma tupla

tupla = ('a', 'b', 'c', 'd', 'e', 'a', 'b')

print(tupla.count('a'))
#Resposta: 2

print(tupla.count('c'))
#resposta: 1

escola = tuple('Geek University')
print(escola)
print(escola.count('e'))
#Resposta:
# ('G', 'e', 'e', 'k', ' ', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y')
# 3



#Dicas para utilização de tuplas

#Devemos utilizar tuplas sempre que não precisarmos modificar os dados contidos numa coleção:

#Exemplo 1

meses = ('janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro')
print(meses)
#Resposta: ('janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro')

#O acesso a elementos de uma tupla também é semelhante a de uma lista

print(meses[5])
#resposta: junho

#Iterar com while
i = 0
while i < len(meses):
    print(meses[i])
    i = i + 1

#Resposta:
# junho
# janeiro
# fevereiro
# março
# abril
# maio
# junho
# julho
# agosto
# setembro
# outubro
# novembro
# dezembro



meses = ('janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro')

#Verificamos em qual indice um elemento está na tupla

print(meses.index('junho'))
#resposta: 5

#OBS: Caso o elemento não exista, será gerado um erro.



#Slicing

#tupla(inicio:fim:passo)
meses = ('janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro')

print(meses[5:9])
#Resposta: ('junho', 'julho', 'agosto', 'setembro')

print(meses[0:10])
#Resposta: ('janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro')




#Porque utilizar tuplas?
# - Tuplas são mais rapidas do que listas. Melhora a performance no seu codigo
# - Tuplas deixam seu cogido mais seguro (pq elas trabalham com imutáveis)

"""

#Copiando uma tupla para outra

tupla = (1, 2, 3)
print(tupla)
nova = tupla
print(nova)
print(tupla)
#Resposta:
# (1, 2, 3)
# (1, 2, 3)
# (1, 2, 3)

outra = (4, 5, 6)
nova = nova + outra  # Na tupla não temos o Shallow copy

