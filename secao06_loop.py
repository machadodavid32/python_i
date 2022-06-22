"""
loop for
loop > Estruturas de repetição
for > uma dessas estruturas

Utilizamos loop para iterar sobre sequencias ou sobre valores iteráveis

Exemplo de iteráveis:
- string
   nome = 'Geek University'
- lista
   lista = [1, 3, 5, 7, 9]
-range
   numeros = range(1, 10)
"""

"""
nome = 'Geek University'
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10) #temos que transformar em uma lista

#exemlo de for 1 (iterando em uma string)
for letra in nome:
    print(letra)

#Exemplo de for 2   (iterando em uma lista)
for numero in lista:
    print(numero)

#Exemplo de for 3 (iterando sobre um range)
for numero in range(1, 10):
    print(numero)

#enumerate:
((0, G), (1, e), (2, e), (3, k) ....."""
"""for indice, letra in enumerate(nome):
    print(nome[indice])

for _, letra in enumerate(nome):   #o underline desconsidera o indice
    print(letra)

for valor in enumerate(nome):
    print(valor)

for valor in enumerate(nome):
    print(valor[0])  #valor na posição zero só mostra os indices

for valor in enumerate(nome):
    print(valor[1]) #valor na posição 1 mostra somente as letras

"""
"""
qtd = int(input("Quantas vezes este loop deve rodar? "))

for n in range(1, qtd+1):
    print(f'Imprimindo {n}') """

#para incrementar o valor acima, podemos fazer o seguinte
"""
qtd = int(input("Quantas vezes este loop deve rodar? "))
soma = 0
for n in range(1, qtd+1):
    num = int(input(f'Informe o {n}/{qtd} valor: '))
    soma = soma + num
print(f'a soma é {soma}') """


nome = 'Geek University'
for letra in nome:
    print(letra, end=' ') #por padrão, no python sempre vai pular linha. Com o comando 'end', vai na mesma linha


"""https://apps.timwhitlock.info/emoji/tables/unicode

um emoji original: U+1F628
o mesmo emoji modificado para o python U0001F628

"""

for _ in range(3):
    for num in range(1, 11):
        print('\U0001F628' * num)

