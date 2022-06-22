""""#Faça uma pequena estrutura for
nome = 'Geek University'
for letra in nome:
    print(letra)

#Faça uma iteração com lista e for
numeros = range(1, 10)
lista = [1, 2, 3, 3, 5, 8, 9]
for numero in lista:
    print(numero)


#Faça uma iteração sobre um range

for numero in range(1, 15):
    print(numero)


#Faça um for usando enumerate
nome = 'geek'
for valor in enumerate(nome):
    print(valor)


#Faça um for com enumerate para mostrar somente os indices
nome = 'geek'
for valor in enumerate(nome):
    print(valor[0])  #valor na posição zero só mostra os indices


#Faça um for com enumerate que mostre somente as letras
for valor in enumerate(nome):
    print(valor[1]) #valor na posição 1 mostra somente as letras


#Faça um programa que use um loop e some os numeros informados
qtd = int(input("Quantas vezes este loop deve rodar? "))
soma = 0
for n in range(1, qtd+1):
    num = int(input(f'Informe o {n}/{qtd} valor: '))
    soma = soma + num
print(f'a soma é {soma}')


#Faça um for que imprima a resposta na mesma linha (comando 'end')
nome = 'Geek University'
for letra in nome:
    print(letra, end=' ')



#Faça um programa que use o comando break

for numero in range(1, 11):
    if numero == 6:
        break
    else:
        print(numero)
print("Saiu do loop")

"""

