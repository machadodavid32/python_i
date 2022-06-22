"""
Modulo random e o que são módulos?

- Em Python, módulos nada mais são do que outros arquivos python

Módulo random - > possui váras funções para geração de números pseudo-aleatórios



# Obs: Existem duas formar de se utilizar um módulo ou função deste.

# Forma 1 - Importar todo o módulo (não recomendado).

import random

# Random gera um número aleatório entre 0 e 1

# Ao realizar o import de todo o módulo, todas as funções, atributos, classes e propriedades que estiverem...
# ...dentro do módulo ficarão disponíveis (ficarão em memória). Caso você saiba quais funções você precisa...
# ...utilizar deste módulo, então esta não seria a forma ideal de utilização. Nós veremos uma forma melhor...
# ...na forma dois

print(random.random())
# Resposta: 0.5919195365317176

# Veja que para utilizar a função randon() do pacote random, nós colocamos o nome do pacote e o nome da função...
# ..separados por ponto.

# Obs: Não confunda a função random com o pacote random. Pode parecer confuso, mas a função random() é apenas...
# ...uma função dentro do módulo random



# Forma dois - importanto uma função específica do módulo (forma recomendada)

from random import random

# No import acima, estamos falando: do módulo random, importe a função random()

for i in range(10):
    print(random())
# Resposta:  0.2992620819946412
# 0.037876620662570804
# 0.9198365487798315
# 0.7437011195838296
# 0.44616237544050286
# 0.9526657558585098
# 0.1618560692439167
# 0.19330938470439907
# 0.10729406008720155
# 0.41584943652672823

# Acima foi gerado dez números aleatórios de 0 a 9



# uniform -> Gerar um número real pseudo-aleatório entre valores estabelecidos

from random import uniform

for i in range(10):
    print(uniform(3, 7))
# Resposta: 4.575823385548861
# 6.757699452804678
# 4.609307289323812
# 3.6440212236813005
# 3.805724738909013
# 6.054480022260335
# 5.757646770332825
# 3.1627265469758075
# 3.964939052723185
# 6.912133635309164

# Acima, ele gera números aleatórios entre 3 e 7 (7 não entra), conforme estabelecido na função uniform()



# randint() -> Gera valores (aqui gera inteiros) pseudo-aleatórios entre os valores estabelecidos

# Gerador de apostas para megasena

from random import randint

for i in range(6):
    print(randint(1, 61), end=', ')  # Começa em 1 e vai até 60
# end= (', ') para que o print() não pule linha e coloque os numeros na mesma linha separados por virgula.

# Resposta: 16, 12, 15, 2, 12, 40,



# choice() - Mostra um valor aleatório entre um iterável.

from random import choice

jogadas = ['pedra', 'papel', 'tesoura']
print(choice(jogadas))
# resposta: pedra - vai variando a resposta conforme a gente vai clicando.


print(choice('geek university'))
# Resposta: s
"""

# função shuffle -> tem a função de embaralhar dados

from random import shuffle

cartas = ['K', 'Q', 'J', 'A', '2', '3', '4', '5', '6', '7']
print(cartas)
shuffle(cartas)
print(cartas.pop())  # o pop() elimina o ultimo numero nesse jogo de cartas que eu não entendo.

# Resposta: ['K', 'Q', 'J', 'A', '2', '3', '4', '5', '6', '7']
# A




