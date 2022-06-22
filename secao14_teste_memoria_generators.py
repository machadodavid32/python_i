"""
Teste de memória com generators


"""


# sequencia de Fibonacci > 1, 1, 2, 3, 5, 8, 13, 21...

def fib_lista(max):
    nums = []
    a, b = 0, 1
    while len(nums) < max:
        nums.append(b)
        a, b = b, a+b
    return nums


# for n in fib_lista(100000):  # o teste aqui deu 449mb quando coloquei 100000
#   print(n)

# Resposta: Uma sequencia grande de numeros


# Agora um segundo teste utilizando generators

def fib_gen(max):
    a, b, contador = 0, 1, 0
    while contador < max:
        a, b = b, a + b
        yield a
        contador = contador + 1

# Teste 2, mesmo teste anterior, porém, com generatros

for n in fib_gen(100000):  # Aqui o resultado da utilização de memoria no monitor do sistema deu 3,9mb.
    print(n)

