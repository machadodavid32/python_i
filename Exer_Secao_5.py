""" 1 - Faça um programa que receba dois numeros e informe qual deles é o maior"""

"""
num1 = int(input("Informe o primeiro numero: "))
num2 = int(input("Informe o segundo numero: "))
if num1>num2:
    print("O primeiro numero é maior")

else:
    print("O segundo numero é maior")
"""

""" 2 - Leia um numero fornecido pelo usuario. Se este numero for positivo, calcule a raiz quadrada deste numero.
Se o número for negativo, informe que o numero é inválido

num = int(input("Informe um numero: "))
if num > 0:
    num = num ** 2
    print("O numero ao quadrado é: ", num)

else:
    print("Numero invalido")
"""

""" 3 - Leia um numero real. Se o numero for positivo, imprima a raiz quadrada. Do contrario, imprima o numero
ao quadro

numero = float(input("Informe um número: "))
if numero > 0:
    numero = numero ** 0.5
    print("A raiz quadrada deste número é: ", numero)

else:
    numero = numero ** 2
    print("Este numero ao quadrado é: ", numero)
"""

""" 4 - Faça um programa que leia um numero e, caso ele seja positivo, calcule e mostre:
O numero digitado ao quadrado
a raiz quadrada do numero digitado


numero = float(input("Informe um numero: "))
if numero > 0:
    numero = numero ** 2
    print("Este numero ao quadrado é: ", numero)
    print("A raiz quadrada deste numero é: ", numero ** 0.5)
"""

""" 5 - Faça um programa que receba um numero inteiro e verifique se este numero é par ou impar"


numero = int(input("Informe um numero: "))
if (numero % 2) == 0:
    print("Numero par")
else:
    print("Numero impar")
"""

""" 6 - Escreva um programa que, dados dois numeros inteiros, mostre na tela o maior deles, assim
como a diferença entre ambos

num1 = int(input("Informe o primeiro numero: "))
num2 = int(input("Informe o segundo numero: "))
if num1 > num2:
    print("O primeiro numero é maior e a diferença entre ele é: ", num1 - num2)
if num1 < num2:
    print("O segundo numero é maior e a diferença entre eles é: ", num2 - num1)
    """

""" 7 - Faça um programa que recebe dois numeros e mostre o maior. Se por acaso os dois numeros serem iguais,
mostre "iguais"

num1 = int(input("Informe o primeiro numero: "))
num2 = int(input("Informe o segundo numero: "))
if num1 > num2:
    print("O primeiro numero é maior: ")
elif num1 == num2:
    print("Iguais")
else:
    print("O segundo numero é maior")

"""

""" 8 - Faça um programa que leia duas notas de um aluno, verifique se as notas são validas e exiba na tela as medias
dessas notas. Uma nota valida deve ser, obrigatoriamente, um valor entre 0 e 10. Onde caso a nota não possua um valor
valido, este fato deve ser informado ao usuario antes do programa fechar"""

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

""" 9 - Leia um salario de um trabalhador e o valor da prestação de um emprestimo. Se a prestação for maior que 20%
do salario, imprima: Emprestimo não concedido. Caso contrario, imprima: Emprestimo concedido"""

"""
salario = float(input("Informe o valor do salario: "))
prestacao = float(input("Informe o valor da prestação: "))
if prestacao > 0.2 * salario:
    print("Emprestimo não concedido")
else:
    print("Emprestimo concedido")
"""

""" 10 - Faça um programa que receba a altura e o sexo de uma pessoa e calcule e mostre seu peso ideal, utilizando
as seguintes formulas, onde h representa a altura. homens (72.7*h) - 58 mulheres (62.1*h) - 44.7"""

altura = float(input("Informe a altura em metros: "))
sexo = input("informe o sexo: ")
if sexo == 'f':
    print("O peso ideal é: ", (62.1*altura)-44.7)
if sexo == 'm':
    print("o peso ideal é: ", (72.7*altura)-58)
else:
    print("Informe apenas f ou m")






