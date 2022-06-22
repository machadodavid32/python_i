"""
Módulos customizados -

Como módulos python nada mais são que arquivos Python, então TODOS os arquivos que criamos
neste curso são módulos Python prontos para serem utilizados.


# Exemplo de uma função criada na seção 8, funções com parametros

from secao08_funcoes_parametros import soma_impares

print(soma_impares([1, 2, 3, 4, 5, 6, 8, 9]))

# Reposta: 16
# 18




import secao08_funcoes_parametros as fcp  # Aqui estamos importando todos as funções do modulo
print(fcp.lista)
# Resposta: 16
# [1, 2, 3, 4, 5, 6, 7]  Importou a variável da seção08

print(fcp.tupla)
# Resposta: 159

"""

from secao10_map import cidades, c_para_f
print(list(map(c_para_f, cidades)))

# Resposta: 12.566370614359172
# 88.24733763933729
# [12.566370614359172, 78.53981633974483, 158.36768566746147, 0.2827433388230814, 314.1592653589793, 6082.12337734984]
# <map object at 0x7fe50c36fdc0>
# <class 'map'>
# [12.566370614359172, 78.53981633974483, 158.36768566746147, 0.2827433388230814, 314.1592653589793, 6082.12337734984]
# [12.566370614359172, 78.53981633974483, 158.36768566746147, 0.2827433388230814, 314.1592653589793, 6082.12337734984]
# [('Berlim', 29), ('Cairo', 36), ('Buenos Aires', 19), ('Los Angeles', 26), ('Tokio', 27), ('Nova York', 28), ('Londres', 22)]
# [('Berlim', 84.2), ('Cairo', 96.8), ('Buenos Aires', 66.2), ('Los Angeles', 78.80000000000001), ('Tokio', 80.6), ('Nova York', 82.4), ('Londres', 71.6)]
# [('Berlim', 84.2), ('Cairo', 96.8), ('Buenos Aires', 66.2), ('Los Angeles', 78.80000000000001), ('Tokio', 80.6), ('Nova York', 82.4), ('Londres', 71.6)]
#
# Process finished with exit code 0
