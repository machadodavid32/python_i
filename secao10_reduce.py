"""
Reduce -
Obs: A partir do Python versão 3 pra cima, a função reduce não é mais uma função integrada (built-in). Agora
temos que importar ela através do modulo 'functools'

Guido Van Rossum: utilize a função reduce() se você realmente precisa dela. Em todo caso, 99% das vezes
um loop for é mais legivel.

Para entender o reduce()
# Imagine que você tenha ua coleção de dados:

dados = [a1, a2, a3, .....an]

E você tem uma função que receba dois parâmetros

def funcao(x, y):
    return y * x

Assim como no map() e filter(), a função reduce() recebe dois parâmetros: a função e o iterável.

reduce(função, dados)

A Função reduce() funciona da seguinte forma:
passo 1: res1 = f(a1, a2) # Aplica a função dos dois primeiros elementos da coleção e guarda o resultado.
passo 2: res2 = f(res1, a3) # Aplica a função passando o resultado do passo 1 mais o terceiro elemento e guarda o resul.

isso é repetido até o final.
passo 3: res3 = f(res2, a4)
.
.
.
passo n: resn = f(resn, an)

Ou seja, em cada passo ela aplica a função passando como primeiro argumento o resultado da aplicação anterior.
No final, reduce() irá retornar o resultado final.

Alternativamente, poderiamos ver a função reduce() como:
funcao(funcao(funcao(a1, a2), a3), a4), ...), an)

"""

# Como funciona na pratica
# Vamos utilizar a função reduce() para multiplicar todos os numeros de uma lista

from functools import reduce

dados = [2, 3, 4, 5, 7, 11, 13, 17, 18, 19, 23, 26]

# Para utilizarmos o reduce, nós precisamos de uma função que receba dois parâmetros
multi = lambda x, y: x * y
res = reduce(multi, dados)
print(res)

# Resposta: 417629852640  - funciona assim, ele pega 2*3, o resultado multiplica pelo proximo, que é 4, e por ai vai

# Utilizando um loop normal

res = 1
for n in dados:
    res = res * n
print(res)
# Resposta: 417629852640


