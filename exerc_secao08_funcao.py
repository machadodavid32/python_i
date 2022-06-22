# 1 - Crie uma função utilizando def e chame a função
#Resposta:

def celular():
    teclado = int(input("Informe um numero de 0 até 10: "))
    if teclado > 0 or teclado < 10:
        print("Xiaomi")
    else:
        print("Informe um numero entre 0 e 10")
celular()



"""
nota1 = float(input("Informe a primeira nota, de 0 a 10: "))

if nota1 < 0 or nota1 > 10:
    print("Nota invalida: ")
else:
    nota2 = float(input("Informe a segunda nota, de 0 a 10: "))

if nota2 < 0 or nota2 > 10:
    print("Nota invalida: ")
else:
    print("O resultado da média é: ", (nota1 + nota2) / 2)
"""