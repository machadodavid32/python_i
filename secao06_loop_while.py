"""
loop while

forma geral

while expressão_booleana:
    //execucação do loop

O bloco do while será repetida enquando a expressão booleana for verdadeira

expressão booleana é toda a expressão onde o resultado é verdadeiro ou falso.

exemplo:
num = 5
num < 5
falso

num < 10
verdadeiro
"""

"""EXEMPLO 1
numero = 1

while numero < 10:
    print(numero)
    numero = numero + 1

#Em um loop while é importante que cuidemos do criterio de parada (neste caso acima > numero = numero + 1)
"""

#EXEMPLO 2

resposta = ' '
while resposta != 'sim':
    resposta = input('Já acabou Jéssica? ')
