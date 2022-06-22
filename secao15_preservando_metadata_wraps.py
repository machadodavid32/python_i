"""
Preservando Metadatas com Wraps

Metadados - São dados intrísecos em arquivos. Exemplo, uma imagem tem um nome, ao verificar as propriedades, ...
... veremos outros dados como tamanho, data, tamanho dos pixels; Isto são os metadados

Wraps - São funções que envolvem elementos com diversas finalidades


# Problema


def ver_log(funcao):
    def logar(*args, **kwargs):
        Eu sou uma função dentro de outra função
        print(f'Você está chamando a função {funcao.__name__}')
        print(f'Aqui chama a documentação: {funcao.__doc__}')
        return funcao(*args, **kwargs)
    return logar


@ver_log
def soma(a, b):
    Soma dois numeros
    return a + b


# print(soma(10, 30))  # Aqui não vai dar erro

# Resposta: Você está chamando a função soma
# Aqui chama a documentação: Soma dois numeros
# 40


# O erro será abaixo

#print(soma.__name__)  # A resposta correta seria 'soma'
print(soma.__doc__)  # A resposta correta seria 'Soma dois numeros'
# resposta: logar
# Eu sou uma função dentro de outra função
# As respostas acima estão incorretas. O que acontece? os metadados das funções acima estão sendo alterados pelo...
# ...decorator (@ever_log). Isso pode dar problema para os programadores entender o codigo.

"""


# Como resolver? Vamos fazer um import

from functools import wraps


def ver_log(funcao):
    @wraps(funcao)  # Resolve o problema de nome e documentação do codigo anterior. Só isso.
    def logar(*args, **kwargs):
        """Eu sou uma função dentro de outra função"""
        print(f'Você está chamando a função {funcao.__name__}')
        print(f'Aqui chama a documentação: {funcao.__doc__}')
        return funcao(*args, **kwargs)
    return logar


@ver_log
def soma(a, b):
    """Soma dois numeros"""
    return a + b


print(soma.__name__)  # A resposta correta seria 'soma'
print(soma.__doc__)  # A resposta correta seria 'Soma dois numeros'
# resposta: soma
# Soma dois numeros

print(help(soma))
# Resposta: Help on function soma in module __main__:
#
# soma(a, b)
#     Soma dois numeros


