"""
Funções com parametros (de entrada)

- Funções que recebem dados para serem processados dentro da mesma

Se a gente pensar em um programa qualquer, geralmente temos:

entrada > processamento > saida

Se a gente pensar em uma função, ja sabemos que temos funções que:
- Não possuem entrada
- Não possuem saida
- Possuem entrada mas não possuem saida
- Não possuem entrada mas possuem saida
- Possuem entrada e saida



#Refatorando uma função

def quadrado(numero):
   # return numero * numero
    return numero ** 2 #outro modo de fazer a conta da linha de cima (pode ser feiro outras contas também)
print(quadrado(7))
print(quadrado(2))
print(quadrado(5))

#resposta:
#49
#4
#25





#Refatorando a função abaixo
def cantar_parabens():
    print('Parabéns para você')
    print('Nesta data querida')
    print('Muitas felicidades')
    print('Muitos anos de vida')
    print('Viva o aniversariante!')

#Refatorando...

def cantar_parabens(aniversariante):
    print('Parabéns para você')
    print('Nesta data querida')
    print('Muitas felicidades')
    print('Muitos anos de vida')
    print(f'Viva o aniversariante! {aniversariante}')
cantar_parabens('Marcos')

#Resposta:
# Parabéns para você
# Nesta data querida
# Muitas felicidades
# Muitos anos de vida
# Viva o aniversariante! Marcos



#Funçoes podem ter N parâmetros de entrada, ou seja, podemos receber como entrada em uma função
#quantos parâmentros são necessários. Eles são separados por virgula.

#Exemplo

def soma(a, b):
    return a + b

def multiplica(num1, num2):
    return num1 * num2

def outra(num1, b, msg):
    return (num1 + b) * msg

print(soma(2, 5))
print(soma(10, 20))
#Resposta: 7
#Resposta: 30

print(multiplica(4, 5))
print(multiplica(2, 8))
#REspostA: 20
#Resposta: 16

print(outra(3, 2, 'geek '))
print(outra(5, 4, 'Python '))
#Resposta: geek geek geek geek geek
#Resposta: Python Python Python Python Python Python Python Python Python



#Nomeando parâmetros -

#Modo 'incorreto'
def nome_completo(string1, string2):
    return f'Seu nome completo é {string1} {string2}'
print(nome_completo('Angelina', 'Jolie'))
#Resposta: Seu nome completo é Angelina Jolie

#modo correto > para melhor entendimento do codigo, os parametros 'string1' e string2' foram alterados para os
#parâmetros 'nome' e 'sobrenome'
def nome_completo(nome, sobrenome):
    return f'Seu nome completo é {nome} {sobrenome}'
print(nome_completo('Angelina', 'Jolie'))
#Resposta: Seu nome completo é Angelina Jolie


#Diferença entre parâmetros e argumentos

#Parametros são variáveis declaradas na definição de uma função

#Argumentos são dados passados durante uma execução de uma função

#A ordem dos parâmetros importa!

nome = 'Felicity'
sobrenome = 'Jones'

print(f'Seu nome completo é {nome} {sobrenome}')
#Resposta: Seu nome completo é Felicity Jones >> Se inverter as variaveis nome e sobrenome, o resultado seria
#Jones Felicity. Portanto, a ordem dos parâmetros importam.

#Argumentos nomeados > Keyword Arguments
#Caso utilizemos  nomes dos parâmetros nos argumentos para informa-los, podemos utilizar qualquer ordem

print(nome_completo(nome='Angelina', sobrenome='Jolie'))
print(nome_completo(nome=nome, sobrenome=sobrenome))
print(nome_completo(sobrenome='Marques', nome='Marcia'))
#Resposta:
# Seu nome completo é Angelina Jolie
# Seu nome completo é Felicity Jones
# Seu nome completo é Marcia Marques

"""


# Erro comum na utilização do 'return'

def soma_impares(numeros):
    total = 0
    for num in numeros:
        if num % 2 != 0:  # > Se o modulo de num por 2 for zero (traduzindo > se for impar)
            total = total + num
    return total   # O erro seria aqui, quando o comando 'return' é colocado abaixo do 'if'. Neste caso esta certo


if __name__ == '__main__':  # Aqui foi uma alteração feita posteriormente referente a seção12 (dunder name e dunderMain)
    lista = [1, 2, 3, 4, 5, 6, 7]  # A partir daqui não houve altrações
    print(soma_impares(lista))

    tupla = (11, 21, 33, 41, 53)
    print(soma_impares(tupla))
    # Resposta: 16






