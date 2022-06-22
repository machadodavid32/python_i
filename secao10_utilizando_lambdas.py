"""
Utilizando lambdas
Conhecidas por expressões lambdas ou simplesmente lambdas são expressões sem nomes, ou seja, funções anônimas

# Função em python:
def soma (a, b)
    return a + b


# Função em python:
def funcao(x):
    return 3 * x + 1


print(funcao(4))
# Resposta: 13

# Exemplo de expressão lambda
lambda x: 3 * x + 1
# E como utilizar a expressão lambda. Só da um nome a ela

calc = lambda x: 3 * x + 1
print(calc(4))
# REsposta: 13



# Podemos ter expressões lambdas com multiplas entradas

nome_completo = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()
# o comando strip() remove espaços no início e no fim da variável
print(nome_completo(' David', 'Machado'))
print(nome_completo(' Aline Guedes', 'Machado'))
# Resposta:
# David Machado
# Aline Guedes Machado



# Em funções Python podemos ter varias entradas ou nenhuma. Em lambdas também.

amar = lambda: "Como não amar Python?"
uma = lambda x: 3 * x + 1
duas = lambda x, y: (x * y) ** 0.5
tres = lambda x, y, z: 3 / (1 / x + 1 / y + 1 / z)

print(amar())
print(uma(6))
print(duas(5, 7))
print(tres(3, 6, 9))

# Resposta: Como não amar Python?
# 19
# 5.916079783099616
# 4.909090909090908
# obs: Se passarmos mais argumentos do que parâmetros esperados, teremos TypeError



autores = ['Asaac Asimov', 'Ray Bradmore', 'Robert Heilein', 'Arthur C Clarke', 'Frank Herbert', 'Orson S Card',
           'Douglas Adam', 'H. G. Wells', 'Leight Brackett']
print(autores)

# Vamos fazer uma ordenção pelo sobrenome
# Abaixo colocoamos 'key' pra escolher a chave que queremos(no caso, sobrenome)
# depois colocamos 'split' para separar o espaço, e no [-1] pegamos o ultimo elemento da lista (ou seja, sobrenome)
autores.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].lower())
print(autores)

# Resposta: ['Douglas Adam', 'Asaac Asimov', 'Leight Brackett', 'Ray Bradmore',
# 'Orson S Card', 'Arthur C Clarke', 'Robert Heilein', 'Frank Herbert', 'H. G. Wells']

# Acima, a ordenação foi feita pelo sobrenome

"""

# Função quadratica (usada, por exemplo, em games)
# f(x) = a * x **2 + b * x + c

# Definindo a função


def geradora_funcao_quadratica(a, b, c):
    """Retorna a função f(x) = a * x **2 + b * x + c"""
    return lambda x: a * x ** 2 + b * x + c


teste = geradora_funcao_quadratica(2, 3, -5)

print(teste(0))
print(teste(1))
print(teste(2))
# Resposta: -5 0 9

# ou podemos fazer acima sem necessidade de criar uma variável:
print(geradora_funcao_quadratica(3, 0, 1)(2))  # Aqui colocamos os parâmetros da função e o parâmetro da lambda
# Resposta: 13
