"""
Funções de maior grandeza - Higher Order Functions (HOF)
O que isso significa?
Quando uma linguagem de programação suporta HOF, indica que podemos ter funções que retorna outras funções...
... como resultado ou mesmo que podemos passar funções como argumentos para outras funções, e até mesmo...
... criar variáveis do tipo de funções nos nossos programas.

obs: Na seção de funções, nós utilizamos isso.
Em Python, as funções são cidadoẽs de primeira classe, ou First Class Citizen



# Exemplos - definindo as funções

def soma(a, b):
    return a + b


def diminuir(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    return a / b


def calcular(num1, num2, funcao):
    return funcao(num1, num2)

# Testando as funções:


print(calcular(4, 3, soma))
print(calcular(4, 3, diminuir))
print(calcular(4,3, multiplicar))
print(calcular(4, 3, dividir))

# Resposta: 7
# 1
# 12
# 1.3333333333333333




# Nested functions - funções aninhadas

# Em python, podemos também ter funções dentro de funções, que são conhecidas por Nested Functions ou ...
# ... também Inner Functions (Funções Internas)

from random import choice


def cumprimento(pessoa):
    def humor():
        return choice(('E ai', 'Suma daqui', 'Gosto muito de você'))
    return humor() + pessoa

# Testando


print(cumprimento(' Angelina'))
print(cumprimento(' Felicity'))



# Retornando funções de outras funções

from random import choice


def faz_me_rir():
    def rir():
        return choice(('hahahah', 'kkkkkkkk', 'kakakakaka'))
    return rir

# Testando


rindo = faz_me_rir()
print(rindo())

"""

# Inner Functions (funções internas) ou Nested Functions podem acessar o escopo de funções mais externas.

from random import choice


def faz_me_rir(pessoa):
    def dando_risada():
        risada = choice(('hhaha', 'lololol', 'kakakaka'))
        return f'{risada} {pessoa}'
    return dando_risada()

# Testando


rindo = faz_me_rir('Aline')
print(rindo)
print(rindo)


