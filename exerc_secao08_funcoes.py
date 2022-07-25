"""Crie uma função que receba como parâmetro um número inteiro e devolva seu dobro"""


def dobro(numero):
    return numero * 2


print(dobro(2))
# Resposta: 4


def triplo(numero):
    return numero * 3


print(triplo(3))
# Resposta: 9


def dividir(numero):
    return numero / 2


print(dividir(4))
# Resposta: 2.0


"""Faça uma função que receba a data atual (dia, mes e ano) e exiba na tela em formato por extenso,
 ex.: data 01/01/2000 imprimir 1 de janeiro de 2000"""


def dt(dia, mes, ano):
    print(f'{dia} de {mes} de {ano}')


dt(23, 'julho', 2022)


def data(decada, seculo):
    print(f'Estamos na década de {decada}, no século {seculo}')


data(20, 21)


"""Faça uma função para verificar se um número é positivo ou negativo. Sendo que o valor de retorno 
será 1 se positivo, -1 se negativo ou zero se igual a zero"""


def positivo_negativo(num1, num2):
    if num1 > 0:
        print("positivo")
    if num2 < 0:
        print('negativo')
    else:
        print('zero')


positivo_negativo(1, 0)


"""Faça uma função e um programa de teste  para o calculo do volume de uma esfera, sendo que o raio é passado
por parâmetro"""


def esfera(radio):
    import math
    volumen = 4.0 * math.pi * radio * radio * radio / 3
    print(f'O valor do volume .{volumen}')
    print()


esfera(50)


"""  Exercicio aleatorio """

print("Qual a sua idade? ")
idade = input()
print(f"A sua idade é {idade}")

