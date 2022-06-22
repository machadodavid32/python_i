"""
Len, ABS, Sum, Round

len() -> Retorna o tamanho (ou seja, o numero de itens) de um itrável.


# Só para revisar

print(len('Geek University'))
print(len([1, 2, 3, 5, 4]))
print(len((1, 2, 3, 4, 5)))
print(len({1, 2, 3, 4, 5}))
print(len({'a': 1, 'b': 2}))
print(len(range(0, 10)))

# Resposta: 15
# 5
# 5
# 5
# 2
# 10

# por debaixo dos panos, quando usamos a função len, o python faz o seguinte:

# dunder(dois underline) len
print('Geek Univeristy'.__len__())
# Resposta: 10



# abs() -> Retorna o valor absoluto inteiro ou real. De forma básica, seria o valor real sem o sinal.

# Exemplos:

print(abs(-5))
print(abs(5))
print(abs(3.14))
print(abs(-3.14))
# Resposta: 5 - sem o sinal de negativo
# 5
# 3.14
# 3.14 - sem o sinal de negativo



# sum -> Recebe como parâmetro um iteŕavel , podendo receber um valor inicial e retorna a soma total dos elementos...
# ..incluindo o valor inicial

# Obs: O valor inicial default é zero

# Exemplos:

print(sum([1, 2, 3, 5, 4]))
print(sum([1, 2, 3, 4, 5,], 5))
# Resposta: 15
# 20

print(sum([3.14, 5.678]))
print(sum((1, 2, 3, 4, 5)))
print(sum({1, 2, 3, 4, 5}))
print(sum({'a': 1, 'b': 2, 'c': 3}.values()))  # Lembrar que .values() é pra somar os valores. Se não ñ da certo
# Resposta: 8.818
# 15
# 15
# 6

"""

# round() retorna um numero arrendodado para n digito  de precisão após decimal.
# Se a precisão não for informada retorna o inteiro mais proximo da entrada.

print(round(10.2))
print(round(10.5))  # Até .5, ele arredonda para baixo
print(round(10.6))  # acima de .6, ele erredonda para cima
print(round(1.121212121, 2))  # Duas casas de precisão
print(round(1.218159999999, 3)) # Duas casas de precição

# Resposta: 10
# 10
# 11
# 1.12
# 1.218

