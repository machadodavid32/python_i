""""#None - tipo de dado que representa o tipo sem tipo, ou poderia ser conhecido também como tipo vazio, porém,
#falar que é um tipo sem tipo é mais apropriado.

 OBS: O tipo None é sempre especificado com a primeira letra Maiuscula. None certo e none errado.

Quando utilizamos?
- Podemos utilizar None quando queremos criar uma variavel e queremos inicializar com um tipo sem tipo antes de
recebermos um valor final
OBS: O tipo None em Python é sempre considerado falso
"""


#- Podemos utilizar None quando queremos criar uma variavel e queremos inicializar com um tipo sem tipo antes de
#recebermos um valor final. Exemplo abaixo numeros

numeros = None
print(numeros)
print(type(numeros))
#Resposta:
# None
#<class 'NoneType'>

numeros = 1.44, 1.34, 5.67
print(numeros)
print(type(numeros))
#Resposta:
# None
# <class 'NoneType'>
# (1.44, 1.34, 5.67)
# <class 'tuple'>   Virou uma tupla