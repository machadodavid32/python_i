"""
Decoradores com diferentes assinaturas

A Assinatura de uma função é representada pelo seu retorno, nome e parâmetro de entrada



def gritar(funcao):
    def aumentar(nome):
        return funcao(nome).upper()
    return aumentar


@gritar
def saudacao(nome):
    return f'Olá, eu sou sou o {nome}'


def ordenar(principal, acompanhamento):
    return f'Olá, eu gostaria de {principal}, acompanhado de {acompanhamento}, por favor'


# Testando

print(saudacao('Angelina'))

# Resposta: OLÁ, EU SOU SOU O ANGELINA



# Abaixo, vamos refatorar a função acima para que possa receber mais de um argumento.


def gritar(funcao):
    def aumentar(*args, **kwargs):
        return funcao(*args, **kwargs).upper()
    return aumentar


@gritar
def saudacao(nome):
    return f'Olá, eu sou o {nome}'


@gritar
def ordenar(principal, acompanhamento):
    return f'Olá, eu gostaria de {principal} acompanhado de {acompanhamento}, por favor. '


print(saudacao('David'))

print(ordenar('Picanha', 'Batata frita'))  # Agora essa função, que tem mais de um parâmetro, vai funcionar
# O fato de adicionar o *args e o **kwargs é chamado de Decorator Pattern

# Resposta:
# OLÁ, EU SOU O DAVID
# OLÁ, EU GOSTARIA DE PICANHA ACOMPANHADO DE BATATA FRITA, POR FAVOR.


@gritar
def lol():
    return 'lol'


print(lol())
# Resposta: LOL

# Reparar que cada função acima tem diferentes numeros de parâmetro, neste caso, caracteriza-se uma diferente assinatura

# Vale lembrar que podemos utilizar parâmetros nomeados.
# Exemplo:
print(ordenar(acompanhamento='batata frita', principal='picanha'))
# Resposta: OLÁ, EU GOSTARIA DE PICANHA ACOMPANHADO DE BATATA FRITA, POR FAVOR.

"""

# Decorator com argumentos


def verifica_primeiro_argumento(valor):
    def interna(funcao):
        def outra(*args, **kwargs):
            if args and args[0] != valor:
                return f'Valor incorreto, o primeiro argumento precisa ser {valor}'
            return funcao(*args, **kwargs)
        return outra
    return interna


@verifica_primeiro_argumento('pizza')
def comida_favorita(*args):
    print(args)


@verifica_primeiro_argumento(10)
def soma_dez(num1, num2):
    return num1 + num2


# Testando

print(soma_dez(10, 12))
# Resposta: 22
print(soma_dez(1, 22))
# Resposta: Valor incorreto, o primeiro argumento precisa ser 10 - pois o primeiro valor não é 10

print(comida_favorita('pizza', 'churrasco'))
# Resposta: ('pizza', 'churrasco')

print(comida_favorita('churrasco', 'pizza'))
# Resposta: Valor incorreto, o primeiro argumento precisa ser pizza




