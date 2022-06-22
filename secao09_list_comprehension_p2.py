"""
List Comprehension

Nós podemos adicionar estruturas condicionais lógicas as nossas list comprehension
"""

# Exemplo 1
numeros = [1, 2, 3, 4, 5, 6]

pares = [numero for numero in numeros if numero % 2 == 0]  # Só vai pegar números pares
impares = [numero for numero in numeros if numero % 2 != 0]  #Só vai pegar os numeros impares

print(pares)
print(impares)
# Resposta:
# [2, 4, 6]
# [1, 3, 5]

# REfatorando o codigo acima

# Qualquer número par por modulo de 2 é 0 e 0 em python é False. not False = True
pares = [numero for numero in numeros if not numero % 2]

# Qualquer número ímpar módulo de 2 é 1, e 1 em python é True
impares = [numero for numero in numeros if numero % 2]

print(pares)
print(impares)

# Resposta:
# [2, 4, 6]
# [1, 3, 5]


# Exemplo 2
res = [numero * 2 if numero % 2 == 0 else numero / 2 for numero in numeros]
print(res)
# REsposta: [0.5, 4, 1.5, 8, 2.5, 12]   > Ele divide os impares e multipla os pares por 2


