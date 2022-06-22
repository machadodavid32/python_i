"""
Range
- precisamos conhecer o loop para usar o range
- precisamos conhecer o range para trabalhar melhor com loops for

Ranges são utilizados para gerar sequencias numericas, não de forma aleatoria, mas sim especificada

Formas gerais:

FORMA 1
range(valor_de_parada)

obs: valor_de_parada não inclusive (inicio padrão 0 e passo de um em um)



# forma 1 Exemplo
for num in range(11):
    print(num)


FORMA 2
range(valor_de_inicio, valor_de_parada)

obs: valor_de_parada não inclusive (inicio especificado pelo usuario e passo de um em um)

# forma 2 exemplo
for num in range(3, 11):
    print(num)

"""
"""
FORMA 3
range(valor_de_inicio, valor_de_parada, passo)

obs: valor_de_parada não inclusive (inicio especificado pelo usuario e passo especificado pelo usuario)


# forma 3 exemplo
for num in range(1, 10, 2):
    print(num)

"""

"""FORMA 4
range(valor_de_inicio, valor_de_parada, passo)
obs: valor_de_parada não inclusive (inicio especificado pelo usuario e passo especificado pelo usuario)
"""

# forma 3 exemplo
for num in range (10, 0, -1):
    print(num)