"""

Criando sua própria versão de loop


"""


def meu_for(interavel):
    it = iter(interavel)
    while True:
        try:
            print(next(it))
        except StopIteration:
            break


meu_for('David')


numeros = [1, 2, 3, 4]
meu_for(numeros)
