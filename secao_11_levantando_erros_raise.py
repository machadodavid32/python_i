"""
Levantando os proprios erros com raise

Raise - lança excessões

obs: O raise não é uma função. É uma palavra reservada, assim como def ou qualquer outra no python.

Para simplificar, pense no raise como sendo util para que possamos criar nossas próprias exceções e mensagens...
..de erro.

A forma geral de utilização é:
raise TipodoErro('mensagem de erro')



raise ValueError('Mensagem incorreta')
# Resposta: Traceback (most recent call last):
#   File "/home/david/PycharmProjects/guppe/secao_11_levantando_erros_raise.py", line 16, in <module>
#     raise ValueError('Mensagem incorreta')
# ValueError: Mensagem incorreta



# Exemplo real:

# Exemplo correto
def colore(texto, cor):
    if type(texto) is not str:
        raise TypeError('Texto precisa ser uma string')
    if type(cor) is not str:
        raise TypeError('Cor precisa ser uma string')
    print(f'O texto {texto} será impresso na cor {cor}')

colore('geelk', 'azul')

# Exemplo que vai dar erro



colore('geelk', 4) # não existe cor 4

# Resposta: Traceback (most recent call last):
#   File "/home/david/PycharmProjects/guppe/secao_11_levantando_erros_raise.py", line 45, in <module>
#     colore('geelk', 4) # não existe cor 4
#   File "/home/david/PycharmProjects/guppe/secao_11_levantando_erros_raise.py", line 42, in colore
#     raise TypeError('Cor precisa ser uma string')
# TypeError: Cor precisa ser uma string




def colore(texto, cor):
    cores = ('verde', 'amarelo', 'azul', 'branco')
    if type(texto) is not str:
        raise TypeError('Texto precisa ser uma string')
    if type(cor) is not str:
        raise TypeError('Cor precisa ser uma string')
    if cor not in cores:
        raise ValueError(f'A cor precisa ser uma entre {cores}')
    print(f'O texto {texto} será impresso na cor {cor}')


colore('geek', 'verde')

# Resposta: O texto geek será impresso na cor verde

# Abaixo, gerando erro

def colore(texto, cor):
    cores = ('verde', 'amarelo', 'azul', 'branco')
    if type(texto) is not str:
        raise TypeError('Texto precisa ser uma string')
    if type(cor) is not str:
        raise TypeError('Cor precisa ser uma string')
    if cor not in cores:
        raise ValueError(f'A cor precisa ser uma entre {cores}')
    print(f'O texto {texto} será impresso na cor {cor}')


colore('geek', 'preto')
 # Resposta : ValueError: A cor precisa ser uma entre ('verde', 'amarelo', 'azul', 'branco')

"""

# Obs: Assim como o return, o raise finaliza a função, ou seja, tudo abaixo dele e ignorado.
