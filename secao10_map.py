"""
map - Com map fazemos mapeamento de uma função


"""

import math


def area(r):
    """Calcula a área de um circulo com raio 'r'."""
    return math.pi * (r ** 2)


print(area(2))
print(area(5.3))
# REsposta: 12.566370614359172
# 88.24733763933729

raios = [2, 5, 7.1, 0.3, 10, 44]  # Aqui estamos lançando varios valores para calcular o PI.

# forma comum de um codigo para cálcular os valores acima.
areas = []
for r in raios:
    areas.append((area(r)))

print(areas)
# Resposta:
# [12.566370614359172, 78.53981633974483, 158.36768566746147, 0.2827433388230814, 314.1592653589793, 6082.12337734984]

# Forma 2: Map é uma função que recebe dois parâmetros: O primeiro a função, o segundo um iterável. Retorna um object
areas = map(area, raios)
print(areas)
print(type(areas))
print(list(areas))  # Aqui estamos convertendo para lista, mas podemos, por exemplo, converter para tuplas ou outras
# Resposta: <map object at 0x7f3026609ba0>
# <class 'map'>
# [12.566370614359172, 78.53981633974483, 158.36768566746147, 0.2827433388230814, 314.1592653589793, 6082.12337734984]


# Forma 3 - Map com lambda
print(list(map(lambda r: math.pi * (r ** 2), raios)))
# Resposta:
# [12.566370614359172, 78.53981633974483, 158.36768566746147, 0.2827433388230814, 314.1592653589793, 6082.12337734984]

# Obs: Após utilizar a função map, depois da primeira visualização do resultado (dando list), ele zera.


# Para fixar - Map:

# Temos dados iteráveis:

# dados: a1, a2, ......an

# Temos una função:

# Função: f(x)

# Utilizamos a função Map(f, dados) inde Map irá 'mapear' cada elemento dos dados e aplicar a função.

# O Map Object: f(a1), f(a2), f(....), f(an)


# Mais um exemplo - De Grasus Celsius para fireghnt

cidades = [('Berlim', 29), ('Cairo', 36), ('Buenos Aires', 19), ('Los Angeles', 26), ('Tokio', 27), ('Nova York', 28),
           ('Londres', 22)]

print(cidades)
# f = 9/5 * c + 32 formula do firegitn

# Abaixo vamos fazer uma lambda


c_para_f = lambda dado: (dado[0], (9/5) * dado[1] + 32)
# Aqui, dado na posição [0] é o nome e dado posição [1] é temperatura
print(list(map(c_para_f, cidades)))

# Resposta:
# [('Berlim', 29), ('Cairo', 36), ('Buenos Aires', 19), ('Los Angeles', 26), ('Tokio', 27), ('Nova York', 28), ('Londres', 22)]
# [('Berlim', 84.2), ('Cairo', 96.8), ('Buenos Aires', 66.2), ('Los Angeles', 78.80000000000001), ('Tokio', 80.6), ('Nova York', 82.4), ('Londres', 71.6)]




