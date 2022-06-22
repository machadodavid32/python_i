"""  LISTAS
print(lista1)
lista1.append(55)
print(lista1)
print(lista1.index(3))
print(lista1.index(5))
print(lista1.index(55))
lista1.append("Superior")
print(lista1)



lista1 = [1, 2, 3, 4, 5]

lista1.append("Superior")
print(lista1[:])  # Pega todos os elementos
print(lista1[1:])  # Pega a partir do segundo elemento
print(lista1[:4])  # Aqui pega os primeiros 4 elementos
print(lista1)
print(lista1[2::2])  # Começa em dois e vai até o final de 2 em 2
print(lista1[2:5])  # Começa no indice dois e vai até o indice 5

lista1.reverse()
print(lista1)  # inverte os valores

lista1.pop()
print(lista1)
lista1.reverse()
print(lista1)
lista1.pop()
print(lista1)
print(sum(lista1))
print(len(lista1))
print(min(lista1))
print(f'o maior numero é {max(lista1)}')


lista1 = [1, 2, 3, 4, 5]
tupla = tuple(lista1)
print(lista1)
lista1 = list(lista1)
print(lista1)
print(tupla)

num1, num2, num3, num4, num5 = lista1
print(num1, num2, num3)  # Aqui desempacotei uma parte da lista

nova = lista1.copy()  # Deep copy
print(lista1)
print(nova)

nova2 = nova
print(f'A nova lista é {nova2}')
"""

"""  TUPLAS
tupla = ('Geek University', 'Programação em Python: Essencial')
print(tupla)
escola, curso = tupla
print(f'A escola é {escola} e o curso é {curso}')

tupla2 = (2, 4, 6, 8, 10, 12)
print(sum(tupla2))
print(len(tupla2))
print(max(tupla2))
print(min(tupla2))

print(tupla + tupla2)  # Mostrando as duas juntas
print(tupla)
print(tupla2)

tupla2 = tupla + tupla2  # juntando as duas na tupla2
print(tupla2)

print(5 in tupla)  # Aqui mostra se o elemento está contido na tupla. Neste caso, false

print(8 in tupla2)  # Aqui está presente, deu True

for n in tupla:
    print(n)



tupla = ('Geek University', 'Programação em Python: Essencial')
tupla2 = (2, 4, 6, 8, 10, 12)

for indice, valor in enumerate(tupla):
    print(indice, valor)

for a, b in enumerate(tupla2):  # mostra o indice de cada objeto na tupla
    print(a, b)

tupla3 = ("Tkinter is not a thin wrapper, but adds a fair amount of its own logic to make the experience more pythonic. This documentation will concentrate on these additions and changes, and refer to the official Tcl/Tk documentation for details that are unchanged.")
print(tupla3.count('p'))  # Aqui podemos contar quantas letras tem num texto, por exemplo.

print(tupla3.count('e'))
print(f'O total de letras "m" é {tupla3.count("m")}')

print(f'O numero 6 está no index {tupla2.index(6)}')
print(tupla2)
print(tupla2[2:4])  # Aqui ele pega a partir do indice 2 e vai até o 3
print(tupla2[0:5:2])  # começa em 0, vai de 2 em 2 até o indice 5

nova_tupla = tupla
print(tupla)
print(nova_tupla)

"""

""" SET - CONJUNTOS 
s = {1, 3, 5, 5, 7, True, 'b'}  # numeros repetidos não aparecem e não guarda a mesma ordem
print(s)

print(3 in s)

if 10 in s:
    print('ok')
else:
    print('Não ok')

for valor in s:
    print(valor)


s.add("David")
print(s)

s.add('Aline')
print(s)

s.remove(3)
print(s)

novo = s  # Shallow copy, ao adicionar um novo elemento ao 'novo', o conjunto 's' também muda
novo.add('IngLes')
print(novo)
print(s)

print(len(novo))  # Aqui só o len funciona pois contém strings no conjunto

estudantes_pythom = {'Marcos', 'Patricia', 'Ellen', 'Pedro', 'Julia', 'Guilherme'}
estudantes_java = {'Fernando', 'Gustavo', 'Julia', 'Patricia'}
estudantes_c = {'Paula', 'Dona Maria', 'David', 'Aline'}
juncao1 = estudantes_java.union(estudantes_pythom)
print(estudantes_java)
print(estudantes_pythom)
print(juncao1)

juncao3 = juncao1 | estudantes_c
print(juncao3)


estudantes_pythom = {'Marcos', 'Patricia', 'Ellen', 'Pedro', 'Julia', 'Guilherme'}
estudantes_java = {'Fernando', 'Gustavo', 'Julia', 'Patricia'}

novo = estudantes_pythom.intersection(estudantes_java)  # pega dois elementos iguais de cada conjunto
print(novo)
# Resposta: {'Julia', 'Patricia'}

novo2 = estudantes_java & estudantes_pythom  # Faz a mesma coisa acima
print(novo2)

# Adicionando elementos em um conjunto
estudantes_java.add(4)
print(estudantes_java)
estudantes_java.add('o comando add adiciona elementos')
print(estudantes_java)

# Remover elementos em um conjunto
estudantes_java.remove(4)
print(estudantes_java)

estudantes_java.remove('Fernando')
print(estudantes_java)

# Outra forma de remover elementos é o comando discard
print(estudantes_pythom)
estudantes_pythom.discard('Pedro')
print(estudantes_pythom)
# Resposta: {'Patricia', 'Pedro', 'Ellen', 'Julia', 'Guilherme', 'Marcos'}
# {'Patricia', 'Ellen', 'Julia', 'Guilherme', 'Marcos'}

estudantes_pythom.add('David')
print(estudantes_pythom)

# Copiando um conjunto para o outro com o comando copy
terceira = estudantes_pythom.copy()
print(terceira)
# REsposta: {'Guilherme', 'Marcos', 'Patricia', 'Julia', 'Ellen', 'David'}

quarta = estudantes_java.copy()
print(f'Conjunto copiado {quarta}')
# REsposta: Conjunto copiado {'Julia', 'o comando add adiciona elementos', 'Patricia', 'Gustavo'}

# Copiando via shallow copy

quarta = terceira
print(quarta)
print(terceira)
# REsposta: {'Patricia', 'Guilherme', 'Ellen', 'David', 'Julia', 'Marcos'}
# {'Patricia', 'Guilherme', 'Ellen', 'David', 'Julia', 'Marcos'}

"""

# FUNÇÃO *ARGS


def soma_todos_numeros(*args):
    return min(args)


numeros = [10, 20, 30, 40,]

print(soma_todos_numeros(2, 5, 7, 1, -3, 45))
print(soma_todos_numeros(*numeros))


