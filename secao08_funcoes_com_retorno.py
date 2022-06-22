"""
Funções com Retorno



"""


"""
numero = [1, 2, 3]
ret_pop = numero.pop()
print(f'Retorno de pop: {ret_pop}')

ret_pr = print(numero)
print(f'O retorno de print: {ret_pr}')

#Resposta:
# Retorno de pop: 3   > a função pop() da retorno
# [1, 2]
# O retorno de print: None  >> Pois a função print() não da retorno

OBS: Em Python quando uma função não retorna nenhum valor o retorno é None

"""

#Vamos refatorar(mudar o codigo) esta função para que ela retorna o valor

"""
def quadrado_de_7():  #Esta função não tem retorno. Na proxima função vamos refatorar o codigo
    print(7 * 7)
ret = quadrado_de_7()

print(f'Retorno {ret}')

def quadrado_de_7():  #Esta função não tem retorno. Na proxima função vamos refatorar o codigo
    return 7 * 7
ret = quadrado_de_7()

print(f'Retorno {ret}')
#Resposta Retorno 49




OBS: Não precisamos necessariamente criar uma variavel para receber o retorno de uma função. 
Podemos passar a execução da função para outras funções


#Refatorando a primeira função
def diz_oi():
    return 'oi ' #Aqui, se eu colocar o 'print', vai dar erro, pois não há retorno para função 'diz_oi()'
alguem = 'Pedro !'
print(diz_oi() + alguem)
#REsposta: oi Pedro!

"""

"""OBS: Sobre a palavra reservada 'return'
1 - Ela finaliza a função, ou seja, ela sai da execução da função
2 - Podemos ter, em função, diferentes returns
3 - Podemos, em uma função, retornar qualquer tipo de dados e até mesmo múltiplos valores


#Exemplo 1
def diz_oi():
    print("Estou sendo executado antes do retorno") #Aqui a frase vai ser printada
    return 'oi!'
    print("Não estou sendo executado após o retorno") #Aqui o retorno fechou a função

print(diz_oi())

#resposta:
# Estou sendo executado antes do retorno
# oi!


#Exemplo 2  == Diferentes Returns
def nova_funcao():
    variavel = True
    if variavel:
        return 4
    elif variavel is None:
        return 3.2
    return 'b'
print(nova_funcao())
#REsposta: 4 > Ou seja, tudo que esta abaixo do return, não foi executado

def nova_funcao():
    variavel = None
    if variavel:
        return 4
    elif variavel is None:
        return 3.2
    return 'b'
print(nova_funcao())
#Resposta: 3.2 > Ele ignorou a 'variavel' por ser none e pegou a proxima

def nova_funcao():
    variavel = False
    if variavel:
        return 4
    elif variavel is None:
        return 3.2
    return 'b'
print(nova_funcao())
#Resposta: b  >>Aqui ele ignora as duas 'variavel' pois a primeira é False, a segundo é None



#Exemplo 3 - Podemos em uma função retornar qualquer tipo de dados ou multiplos valores

def outra_funcao():
    return 2, 3, 4, 5

num1, num2, num3, num4= outra_funcao()

print(num1 ,num2, num3, num4)
print(outra_funcao())

#Resposta:
# 2 3 4 5
#(2, 3, 4, 5)  >>Formato de tupla devido ao return 2, 3, 4, 5



#Vamos criar uma função para jogar a moeda

from random import random

def joga_moeda():
    #gera um numero pseudo-randomico entre 0 e 1
    valor = random()
    if valor > 0.5:
        return 'cara'
    return 'coroa'
print(joga_moeda())
#Resposta: cara >Vai ficar variando entre cara e coroa

#Vamos refatorar o codigo acima

def joga_moeda():
    #gera um numero pseudo-randomico entre 0 e 1
    if random() > 0.5:
        return 'cara'
    return 'coroa'
print(joga_moeda())

"""

#Erros comuns na utilização do retorno de uma função, que na verdade não é erro, mas sim codificação desnecessária

def eh_impar():
    numero = 5
    if numero % 2 != 0:
        return True
    else:
        return False
print(eh_impar())
#Resposta: True   >> Se colocar o 6, vai dar false

#Agora o mesmo codigo acima refatorado

def eh_impar():
    numero = 5
    if numero % 2 != 0:
        return True
    return False
print(eh_impar())
#Resposta: True  > Veja que está mais limpo o codigo