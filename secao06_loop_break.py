"""
Saindo de loop com break

Funciona na mesma forma que na linguagem c ou java. Utilizamos o break para sair de loops de maneira projetada.

"""

#Exemplo

for numero in range(1, 11):
    if numero == 6:
        break
    else:
        print(numero)
print("Saiu do loop")


#exemplo 2

while True:   #nesta linha criamos um loop infinito
    comando = input("Digite 'sair' para sair ")
    if comando == 'sair':
        break

