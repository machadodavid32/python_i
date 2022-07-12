"""
**kwargs
Poderíamos chamar este parâmetro de **xis, mas por convenção chamamos de **kwargs

Este é só mais um parâmetro, mas, diferentes do *args que coloca os valores extras em um tupla, o **kargs exige
que utilizemos parâmetros nomeados, e transforma esses parâmetros extras em dicionários.
"""

"""
#exemplo

def cores_favoritas(**kwargs):
    print(kwargs)

cores_favoritas(marcos='verde', julia='amarelo', fernanda='azul', vanessa='branco')

#Resposta: {'marcos': 'verde', 'julia': 'amarelo', 'fernanda': 'azul', 'vanessa': 'branco'}
#criou um dicionário


#exemplo

def cores_favoritas(**kwargs):
    for pessoa, cor in kwargs.items():
        print(f'A cor favorita da {pessoa.title()} é {cor}')

cores_favoritas(marcos='verde', julia='amarelo', fernanda='azul', vanessa='branco')


#OBS: Os parâmetros *args ou **kwargs não são obrigatórios
cores_favoritas()
cores_favoritas(geek='navy')

#Resposta: A cor favorita da Marcos é verde
# A cor favorita da Julia é amarelo
# A cor favorita da Fernanda é azul
# A cor favorita da Vanessa é branco



# Exemplo mais complexo


def cumprimento_especial(**kwargs):
    if 'geek' in kwargs and kwargs['geek'] == 'Python':
        return 'Você recebeu um cumprimento Pythônico Geek!'
    elif 'geek' in kwargs:
        return f"{kwargs['geek']} Geek"
    return 'Não tenho certeza quem você é ...'


print(cumprimento_especial())
print(cumprimento_especial(geek='Ṕython'))
print(cumprimento_especial(geek='Oi'))
print(cumprimento_especial(geek='especial'))



# Nas nossas funções podemos ter NESTA ORDEM:
# parâmetros obrigatorios
# *args
# Parâmetros default (não obrigátorios)
# **kwargs

def minha_funcao(idade, nome, *args, solteiro=False, **kwargs):
    print(f'{nome} tem {idade} anos')
    print(args)
    if solteiro:
        print('solteiro')
    else:
        print('casado')
    print(kwargs)


minha_funcao(8, 'Julia')
minha_funcao(18, 'Felicity', 4, 5, 3, solteiro=True)
minha_funcao(34, 'Felipe', eu='Não', voce='Vai')
minha_funcao(19, 'Carla', 9, 4, 3, java=False, python=True)

#Resposta: Julia tem 8 anos
# ()
# casado
# {}
# Felicity tem 18 anos
# (4, 5, 3)
# solteiro
# {}
# Felipe tem 34 anos
# ()
# casado
# {'eu': 'Não', 'voce': 'Vai'}
# Carla tem 19 anos
# (9, 4, 3)
# casado
# {'java': False, 'python': True}



# Entendo porque é importante obedecer a ordem dos parâmetros
# Abaixo, função com a ordem correta
def mostra_info(a, b, *args, instrutor='Geek', **kwargs):
    return [a, b, args, instrutor, kwargs]

#Aqui, cada parâmetro vai receber um valor:
#a = 1
#b = 2
#args = (3,)
#instrutor = 'Geek'
#kwargs = {'sobrenome': 'university', 'cargo': 'instrutor'}

print(mostra_info(1, 2, 3, sobrenome='university', cargo='instrutor'))

# Resposta: [1, 2, (3,), 'Geek', {'sobrenome': 'university', 'cargo': 'instrutor'}]

# Abaixo, a função com ordem incorreta

def mostra_info(a, b, instrutor='Geek', *args, **kwargs):
    return [a, b, args, instrutor, kwargs]

print(mostra_info(1, 2, 3, sobrenome='university', cargo='instrutor'))

# Resposta: [1, 2, (), 3, {'sobrenome': 'university', 'cargo': 'instrutor'}]
# Veja que o sistema gerou uma resposta, mas o args não está recebendo a tupla 3 e o 'instrutor', em vez de receber 'Geek', está recebendo o numero 3. Está incorreto.



# Desempacotar com **kwargs

def mostra_nomes(**kwargs):
    return f"{kwargs['nome']} {kwargs['sobrenome']}"


nomes = {'nome': 'Felicity', 'sobrenome': 'Jones'}

print(mostra_nomes(**nomes))

#Resposta: Felicity Jones  > Usando apenas **

"""


def soma_multiplos_numeros(a, b, c):
    print(a+b+c)


lista = [1, 2, 3]
tupla = (1, 2, 3)
conjunto = {1, 2, 3,}
soma_multiplos_numeros(*lista) # nestes usa-se apenas 1 *
soma_multiplos_numeros(*tupla)
soma_multiplos_numeros(*conjunto)

dicionario = dict(a=1, b=2, c=3)
soma_multiplos_numeros(**dicionario) # Aqui usa-se dois **

# Resposta: 6
# 6
# 6
# 6

# OBS: Os nomes da chave em um dicionário devem ser os mesmos dos parâmetros da função

