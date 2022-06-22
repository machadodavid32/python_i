"""1 - Faça uma tupla nos dois jeitos"""
mouse = (1, 3, 2, 2, 5, 7,)
print(mouse)
print(type(mouse))
#Resposta:
# (1, 3, 5, 7, 4, 5)
# <class 'tuple'>


galo = 1, 3, 5, 7, 4, 5
print(galo)
print(type(galo))
#Resposta:
# (1, 3, 5, 7, 4, 5)
# <class 'tuple'>


"""2 - Faça uma tupla com um elemento"""
garrafa = (9, )
print(garrafa)
#Resposta: (9,)


"""3 - Gerar 3 tuplas com range"""
teclado = tuple(range(11))
print(teclado)
#Resposta: (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

placa = tuple(range(18))
print(placa)
#Resposta: (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17)

tela = tuple(range(5))
print(tela)
#resposta: (0, 1, 2, 3, 4)


"""4 - Faça uma tupla com 3 elementos e desempacote"""
pc = ('processador', 'memoria', 'hd')
gabinete, tela, cd = pc
print(gabinete)
print(tela)
print(cd)
#Resposta:
# processador
# memoria
# hd


"""5 - Faça mais uma tupla e desempacote"""
moto = ('roda', 'motor')
preco, valor = moto
print(preco)
print(valor)
#Resposta:
# roda
# motor


"""5 - Crie duas tuplas de inteiros e faça a soma"""
moto = (1, 34, 55, 78)
print(sum(moto))
#Resposta: 168

motor = (5, 5, 5, 1874, 54)
print(sum(motor))
#resposta: 1943


"""6 - Faça duas tuplas e mostre o valor maximo de cada uma"""
motor = (5, 5, 5, 1874, 54)
print(max(motor))
#Resposta: 1874

moto = (1, 34, 55, 78)
print(max(moto))
#Resposta: 78


"""7 - Faça duas tuplas e mostre o valor minimo"""
motor = (5, 5, 5, 1874, 54)
print(min(motor))
#Resposta: 5

moto = (1, 34, 55, 78)
print(min(moto))
#Resposta: 1


"""8 -Faça duas tuplas e mostre o tamanho delas"""
gas = ('r-22', '141-b', 'gas de cozinha')
print(len(gas))
#Resposta: 3

switch = (1, 5, 5, 5,8, 7, 7, 8, 'david')
print(len(switch))
#Resposta: 9


"""9 - Faça a concatenação de duas tuplas"""
moto = (1, 34, 55, 78)
motor = (5, 5, 5, 1874, 54)
print(motor + moto)
#Resposta: (5, 5, 5, 1874, 54, 1, 34, 55, 78)


"""10 - Crie um tupla da junção de outras duas"""
factor = moto + motor
print(factor)
#Resposta: (1, 34, 55, 78, 5, 5, 5, 1874, 54)


"""11 - altere uma tupla """
motor = moto + motor
print(motor)
#Resposta: (1, 34, 55, 78, 5, 5, 5, 1874, 54)


"""12 - Verique se tal elemento esteja presente na tupla """
print(3 in motor)
#Resposta: False

print(5 in motor)
#Resposta: True

print(1874 in motor)
#Resposta: True


"""13 - Itinere sobre uma tupla"""
for n in motor:
    print(n)
#Resposta:
# 1
# 34
# 55
# 78
# 5
# 5
# 5
# 1874
# 54

"""14 - Mostre um indice de uma tupla"""
for indice, valor in enumerate(motor):
    print(indice, valor)
#Resposta:
# 0 1
# 1 34
# 2 55
# 3 78
# 4 5
# 5 5
# 6 5
# 7 1874
# 8 54

"""15 - Como contar quantos elementos repetidos em  tem em uma tupla?"""
print(motor.count(34))
#Resposta: 1

som = ('rock', 'Reggae', 'samba', 'forro', 'polca', 'rock', 'rock')
print(som.count('rock'))
#resposta: 3


"""16 - Acesse um dos elementos via indice da tupla abaixo"""
meses = ('janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro')
print(meses[6])
#Resposta: julho

print(meses[4])
#Resposta: maio

print(meses[7])
#Resposta: agosto


"""17 - Como localizar um indice da tupla abaixo"""
meses = ('janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro')
print(meses.index('agosto'))
#Resposta: 7

print(motor.index(34))
#Resposta: 1
