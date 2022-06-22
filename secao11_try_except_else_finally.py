"""
Try / Except / Else / Finally

Dica de quanto e onde tratar codigo.:
Toda entrada deve ser tratada.

obs: A função do usuario é destruir seu sistema


num = 'errado'

try:
    num = int(input('Informe um numero: '))
except ValueError:
    print('Valor incorreto')
print(f'Você digitou {num}')


# ou:

try:
    num = int(input('Informe um numero: '))
except ValueError:
    print('Valor incorreto')
else:
    print(f'Você digitou {num}')

# Else será executado somente se não entrar o erro.



# Finally

try:
    num = int(input('Informe um numero: '))
except ValueError:
    print('Você não digitou um valor valido')
else:
    print(f'Você digitou o numero {num}')
finally:
    print('Executando o finally')

# Resposta: Informe um numero: david
# Você não digitou um valor valido
# Executando o finally

# obs: O bloco finally sempre é executado. Independente se houve excessão ou não.

# O Finally geralmente é utilizado para fechar ou deslocar recursos.


# Exemplo mais complexo ERRADO

def dividir(a, b):
    return a / b

num1 = int(input("Informe o primeiro numero: "))
try:
    num2 =  int(input("Informe o segundo numero: "))
except ValueError:
    print('O valor precisa ser numerico')
try:
    print(dividir(num1, num2))
except NameError:
    print('Valor incorreto')


# FORMA CORRETA ABAIXO
# Obs: Você é responsável pelas entradas de suas funções.


def dividir(a, b):
    try:
        return int(a) / int(b)
    except ValueError:
        return 'Valor incorreto'
    except ZeroDivisionError:
        return 'Não é possivel realizar esta operação por zero'


num1 = input('Informe o primeiro numero: ')
num2 = input('Informe o segundo numero: ')
print(dividir(num1, num2))




# Exemplo mais complexo: SEMI GENERICO
# OBS:


def dividir(a, b):
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError):
        return 'Ocorreu um problema'


num1 = input('Informe o primeiro numero: ')
num2 = input('Informe o segundo numero: ')
print(dividir(num1, num2))

# Resposta: Informe o primeiro numero: 0
# Informe o segundo numero: 0
# Ocorreu um problema

"""
# Ou podemos incluir o as err


def dividir(a, b):
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err:
        return f'Ocorreu um problema: {err}'


num1 = input('Informe o primeiro numero: ')
num2 = input('Informe o segundo numero: ')
print(dividir(num1, num2))

# Resposta: Informe o primeiro numero: 1
# Informe o segundo numero: 0
# Ocorreu um problema: division by zero
#
# Process finished with exit code 0
