"""
Erros mais comuns em python

Atenção - É importante prestar atenção e aprender a ler as saídas de erro geradas pela execução do nosso codigo


Sintaxerror - Ocorre quando o python encontra um erro de sintaxe. Ou seja, você escreveu algo que python
não reconhece como parte da linguagem
que o python


# Exemplo de sintaxerror

# def funcao:
#    print('Geek University')

# A correta

#def funcao():
#    print('Geek University')


None = 1 #  SintaxError
return # sozinha da SintaxError



# NameError - Ocorre quando uma variável ou função não foi definida

# Exemplos

print(geek) # name 'geek' is not defined
gee()

a = 18
if a < 10:
    msg = 'É menor que dez'

print(msg)  # Erro  name 'msg' is not defined

# TypeError - ocorre quando uma função/operação/ação é aplicada a um tipo errado

# Exemplos de TypeError

print(len('geek'))
#  Resposta: 4

print(len(5))  # TypeError: object of type 'int' has no len()

print('geek' + [])  # - typeError


# IndexError - Ocorre quando tentamos acessar um elemento em uma lista ou outro tipo de dado indexidado
# utilizando um indice inválido

lista = ['geek']
print(lista[0])
# Resposta: geek

lista = ['geek']
print(lista[0][2])
# Resposta: e

lista = ['geek']
print(lista[0][10])  # IndexError: string index out of range


lista = ['geek']
print(lista[10]) # IndexError: list index out of range


# ValueError - Ocorre quando uma função/operação  built-in (integrada) recebe um argumento com tipo correto ...
# ...mas valor inapropriado

# Exemplo de ValueError

print(int('geek'))  # - ValueError: invalid literal for int() with base 10: 'geek' - não consegue transformar a..
# ..string 'geek' em inteiro



# KeyError - Ocorre quando tentamos acessar um dicionário com uma chave que não existe

# Exemplos de KeyError

dic = {'python': 'univerisity'}
print(dic['geek']) # KeyError: 'geek'


Exception e error são sinonimos na programação

Importante ler a saída de erro
"""

