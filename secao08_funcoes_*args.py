"""
Entendendo o *args

- O *args é um parâmetro como outro qualquer. Isso significa que você poderá chamar de qualquer coisa, desde que
comece com *

Exemplo:

*xis

Mas por convenção, utilizamos *args para definí-lo.

Mas o que é *args?

O parâmetro *args utilizado em uma função, coloca os valores extras informados como entrada em uma tupla.
Então desde já lembre-se que tuplas são imutáveis.


#Exemplo

def soma_todos_numeros(num1, num2, num3):
    return num1, num2, num3

print(soma_todos_numeros(4, 6, 9))

#print(soma_todos_numeros(4, 6)) Aqui da typeError pois tem uma função a menos(podemos resolver ao colocar valores
# dentro dos parâmetros como num1=1, num2=1, num3=1.)

#print(soma_todos_numeros(4, 6, 9, 5))Aqui da typeError pois tem uma função a mais



#Entendendo o *args

def soma_todos_numeros(*args):
    print(args)

soma_todos_numeros()
soma_todos_numeros(1)
soma_todos_numeros(2, 3)
soma_todos_numeros(4, 5, 6)
soma_todos_numeros(7, 8, 9, 10)

#Resposta:
# ()
# (1,)
# (2, 3)
# (4, 5, 6)
# (7, 8, 9, 10)

#Abaixo, vamos somar os numeros:

def soma_todos_numeros(*args):
    total = 0
    for numero in args:
        total = total + numero
    return total

print(soma_todos_numeros())
print(soma_todos_numeros(1))
print(soma_todos_numeros(2, 3))
print(soma_todos_numeros(4, 5, 6))
print(soma_todos_numeros(7, 8, 9, 10))

#Resposta:
# 0
# 1
# 5
# 15
# 34

#Mas poderia ficar melhor. Função acima refatorada com sum

def soma_todos_numeros(*args):
    return sum(args)

print(soma_todos_numeros())
print(soma_todos_numeros(1))
print(soma_todos_numeros(2, 3))
print(soma_todos_numeros(4, 5, 6))
print(soma_todos_numeros(7, 8, 9, 10))

#Resposta:
# 0
# 1
# 5
# 15
# 34



#Outro exemplo de utilização do *args

def veerifica_info(*args):
    if 'Geek' in args and 'University' in args:
        return 'Bem-vindo Geek'
    return 'Eu não tenho certeza quem você é .....'

print(veerifica_info())
print(veerifica_info(1, True, 'University', 'Geek'))
print(veerifica_info(1, 'University', 3.145))

#Resposta: Eu não tenho certeza quem você é .....
# Bem-vindo Geek
# Eu não tenho certeza quem você é .....


def soma_todos_numeros(*args):
    return sum(args)

print(soma_todos_numeros())
print(soma_todos_numeros(3, 4, 5, 6))

numeros = [1, 2, 3, 4, 5, 6, 7]

print(soma_todos_numeros(numeros, 4, 5, 6))
#Resposta: TypeError - Ele considera a lista 'numeros' como se fosse um elemento apenas. Não da pra somar


"""
#Mas como resolver o problema acima? Usando o desempacotador


def soma_todos_numeros(*args):
    return sum(args)

#print(soma_todos_numeros())
#print(soma_todos_numeros(3, 4, 5, 6))

numeros = [1, 2, 3, 4, 5, 6, 7]

#Desempacotando
print(soma_todos_numeros(*numeros))

#Resposta: 28 - Apenas colocando * em 'numeros'


#OBS: O * serve para que informemos ao Python que estamos passando como argumento uma coleção de dados.
#Desta forma ele saberá que precisará antes desempacotar esses dados.