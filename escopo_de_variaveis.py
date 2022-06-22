"""Escopo de variaveis
   Dois casos de Escopo:
1 - Variaveis globais - Variaveis globais são reconhecidas, ou seja, seu espaço compreende todo o programa.

2 - Variaǘeis Locais - Variaveis locais são reconhecidas apenas no bloco onde foram declaradas, ou seja, compreende
apenas uma parte especifica do programa.

Para  declarar variavel em Python fazemos:
nome_da_variavel = valor_da_variavel.
EXEMPLO ABAIXO

"""

numero = 42
print(numero)
print(type(numero)) ###Type verifica o tipo da variavel. O resultado é "int" a variavel numero é global.

if numero > 10:
    novo = numero + 10
    print(novo)    ###novo é uma variavel local, esta declarada dentro de "if"

