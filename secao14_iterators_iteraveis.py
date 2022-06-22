"""
Entendendo iterators e (iterables) iteráveis

iterator - >
    - Um objeto que pode ser iterado
    - Um objeto que retorna um dado, sendo um elemento por vez quando uma função next() for chamada.

iterable - >
    - Um objeto que irá retornar um iterator quando a função ite() for chamada




nome = 'geek'  # É um iterable mas não é um iterator
numeros = [1, 2, 3, 4, 5, 6]  # É um iterable mas não é um iterator

# ao colocarmos o comando print(next(nome)) ou print(next(numeros)) vai dar um erro, pois as variáveis acima ...
# ... não são iterators, porém, da pra torna-las iterators da seguinte forma:

it1 = iter(nome)
it2 = iter(numeros)

# Após fazer isso, podemos iterar da seguinte forma

print(next(it1))
# Resposta: g
# Para cada vez que geramos essa linha de codigo, um dado da string 'geek' vai aparecer
print(next(it1))
# Resposta: e
print(next(it1))
# Resposta: e
print(next(it1))
# Resposta: k

print(next(it2))
# Resposta: 1
print(next(it2))
# Resposta: 2
print(next(it2))
# Resposta: 3
print(next(it2))
# Resposta: 4
print(next(it2))
# Resposta: 5
print(next(it2))
# Resposta: 6

# Caso ultrapassarmos o número dessa sequência, ou seja, se os comandos forem maior do que o numero de dados que...
# ... a string contém, dará erro.

"""

nome = 'geek'

for letra in nome:
    print(letra)
# A sequencia de comando acima, faz, por baixo dos panos, a transformação de 'geek' em iterator. Ele aplica o iter()...
# ... e depois fica chamando a função next() até terminar os dados contidos na variável.



