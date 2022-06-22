"""
Any e All
All - retorna True se todos os elementos do iterável são verdadeiros ou ainda se o iterável está vazio


# Exemplo all
print(all([0, 1, 2, 3, 4]))  # Todos os números são verdadeiros?
# Resposta: False

print(all([1, 2, 3, 4]))
# Resposta: True -> pois todos os numeros são verdadeiros

# Obs: Os exemplos aima são listas, mas podem ser tuplas, conjuntos, etc

nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina']
print(all([nome[0] == 'C' for nome in nomes]))
# Resposta: True


# Obs: Um iterável vazio convertido em boolean é false, mas o all compreende como True
print(all(letra for letra in 'eiof' if letra in 'aeiou'))
# Resposta: True

print(all(numero for numero in [4, 2, 10, 6, 8] if numero % 2 == 0))
# Resposta: True

"""

# Any - Retorna True se qualquer elemento do iterável for verdadeiro. Se o iterável estiver vazio, se torna false.

print(any([1, 2, 3, 4]))
# Resposta: True  -> pois todos são verdadeiros

print(all([0, False, {}, {}]))
# False - > pois TODOS são False

nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina', 'Vanessa']
print(any([nome[0] == 'C' for nome in nomes]))
# Resposta: True

