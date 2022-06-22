"""
set comprehension

lista = [1, 2, 3, 4, 5, 6 7]
set = {1, 2, 3, 4, 5, 6, 7}

"""

# Exemplos:

numeros = {num for num in range(1, 7)}
print(numeros)
# Resposta: {1, 2, 3, 4, 5, 6}

numeros = {x ** 2 for x in range(10)}
print(numeros)
# Resposta: {0, 1, 64, 4, 36, 9, 16, 49, 81, 25}

# DESAFIO: Faça uma alteração na estrutura acima para gerar um dicionário ao invés de set:
numeros = {x: x ** 2 for x in range(10)}
print(numeros)
# Resposta: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}

# Pra finalizar
letras = {letra for letra in 'Geek University'}
print(letras)

