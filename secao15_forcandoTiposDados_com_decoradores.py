"""
Forçando tipo de dados com decoradores

Como funciona o zip, exemplo:
a = (1, 3, 5)
b = (2, 4, 6)
c = zip(a, b)
Resposta: (1, 2), (3, 4), (5, 6)

"""


def forca_tipo(*tipos):
    def decorador(funcao):
        def converte(*args, **kwargs):
            novo_args = []
            for(valor, tipo) in zip(args, tipos):
                novo_args.append(tipo(valor))
            return funcao(*novo_args, **kwargs)
        return converte
    return decorador


@forca_tipo(str, int)
def repete_msg(msg, vezes):
    for vez in range(int(vezes)):
        print(msg)


repete_msg('geek', '3')
# Resposta:
# geek
# geek
# geek



@forca_tipo(float, float)
def dividir(a, b):
    print(a/b)


dividir('1', 5)

# Reposta: 0.2
