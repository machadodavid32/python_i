"""
O bloco try/except

Utilizamos o bloco try/except para tratar erros que podem ocorrer no nosso codigo. Previnindo assim que o
programa pare de funcionar e o usuario receba mensagens de erro inesperadas.

A forma geral mais simples é:

try:
    \\exeção problematica
exception:
    \\o que deve ser feito em casa de problema



# Exemplo:
try:
    geek()
except:
    print("Del algum problema")
# Acima, estamos dizendo ao python para, caso encontre erros, mande mensagem
try:
    len(5)
except:
    print('Deu algum problema')

# Respposa: Deu algum problema

# Obs: Tratar erro de formar generica não é a melhor forma de tratamento de erros.....
# ....O ideal é SEMPRE tratar de forma específica

# Exemplo 3 - Tratando um erro específico.

try:
    geek()
except NameError:
    print('Você está utilizando uma função inexistente')

# Resposta: Você está utilizando uma função inexistente

try:
    len(5)  # Aqui vai dar erro, pois trata-se de um objeto tipo 'int'.
except NameError:
    print('Você está utilizando uma função inexistente')


# Exemplo

try:
    len(5)
except TypeError: # com typeError o aviso vai funcionar
    print('Você está utilizando uma função inexistente')

# Resposta: Você está utilizando uma função inexistente

# Abaixo, uma situação melhor:

try:
    len(5)
except TypeError as err:
    print(f'A aplicação seguinte gerou erro {err}')

# Resposta: A aplicação seguinte gerou erro object of type 'int' has no len()



# Podemos efetuar diversos tratamentos de erro.

try:
    gee()
except NameError as erra:
    print(f'Deu NameError: {erra}')
except TypeError as errb:
    print(f'Deu TypeErros {errb}')
except:
    print('Deu erro diferente')

# Resposta: Deu NameError: name 'gee' is not defined

"""

# Exmplo com uma função criada

def pega_valor(dicionario, chave):
    try:
        return dicionario[chave]
    except KeyError:
        return None


dic = {'nome': 'geek'}

print(pega_valor(dic, 'game'))  # Aqui se eu colocar 'nome' o resultado deve sair 'geek' 

# Resposta: None


