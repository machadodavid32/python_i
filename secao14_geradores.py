"""
Geradores

- Geradores (Generators) são Iterators (Iteradores):
Obs: O contrario não é verdadeiro, ou seja, nem todos os Iteradores são Generators

Outras informações:
-Generators podem ser criados com funções geradoras;
-Funções geradoras utilizam a palavra reservada yield;
-Generators podem ser criados com Expressões Geradouras;


Diferenças entre Funções e Generators function (funções geradoras)

Funções: Utilizam return; retorna somente uma vez; Quando executada, retorna um valor

Generator Functions: Utilizam yield; podem utilizar yield mutiplas vezes; quando executada, retorna um generator

"""

# Exemplo de Função geradora (generator function)


def conta_ate(valor_maximo):
    contador = 1
    while contador <= valor_maximo:
        yield contador  # a função yield é parecida com return, porém, ela não sai do codigo e pode ser utilizada + x
        contador = contador + 1

# obs: Um generator function não é um Generator. Ele gera Generator, ok?

"""
gen = conta_ate(5)

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
# Resposta: 1
# 2
# 3
# 4
# 5

"""
"""
gen = conta_ate(10)

for num in gen:
    print(num)
# Resposta: 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
"""


gen = list(conta_ate(10))

print(gen)
# REsposta: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  Transformei em uma lista



