"""
Listas aninhadas (Nested lists)

Algumas linguagens de programação possuem uma estrutura de dados chamadas arrays:
    - Unidimensionais (arrays/vetores)
    - Multidimensionais (vetores)

Em Python temos as listas:
numero = [1, 2, 3, 4, 5, 'b', 3.231, True]



# Exemplos
listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # Matriz 3x3
print(listas)
print(type(listas))
# REsposta: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Como fazemos para acessar os dados
print(listas[0])
# REsposta: [1, 2, 3]

print(listas[0][1]) # Aqui acessaremos o segundo elemento do primeiro elemento da lista (no caso, linha 0 coluna 1)
# Resposta: 2

print(listas[2][1]) # Linha 2 elemento 1 = 8
# REsposta: 8

# Iterando com Loops numa lista aninhada
for lista in listas:
    print(lista)
# REsposta:
# [1, 2, 3]
# [4, 5, 6]
# [7, 8, 9]

for lista in listas:
    for num in lista: # Vai pegar os elementos das listas dentro das listas
        print(num)
# Resposta:
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9


# List comprehension
[[print(valor) for valor in lista] for lista in listas]
# Resposta: Comando refatorado
# 3
# 4
# 5
# 6
# 7
# 8
# 9

"""

# Outros exemplos

# Gerando um tabuleiro/matriz 3x3

tabuleiro = [[numero for numero in range(1, 4)] for valor in range(1, 4)]
print(tabuleiro)
# Resposta: [[1, 2, 3], [1, 2, 3], [1, 2, 3]]

# Gerando jogadas para o jogo da velha
velha = [['X' if numero % 2 == 0 else 'O' for numero in range(1, 4)] for valor in range(1, 4)]
print(velha)
# Resposta: [['O', 'X', 'O'], ['O', 'X', 'O'], ['O', 'X', 'O']]


# Gerando valores inicias
print([['*' for i in range(1, 4)] for j in range(1,4)])
# Resposta: [['*', '*', '*'], ['*', '*', '*'], ['*', '*', '*']]
