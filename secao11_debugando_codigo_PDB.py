"""
Debugando com PDB
PDB: Python Debbugger




# obs: a utilização do print() para debbugar erros é uma prática ruim. Existem métodos melhores.

def dividir(a, b):
    print(f'a={a}, b={b}')
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err:
        return f'Ocorreu um problema: {err}'


print(dividir(4, 7))

# Resposta: a=4, b=7
# 0.5714285714285714



# Existem formas mais profissionais de se fazer um 'debug' utilizando o debbuger
# Em Python, podemos fazer isso em diferentes IDE´s, como o pycharm ou o PDM - Python Debbuger

# Exemplo com o Pycharm

# Abaixo, ao clicarmos na coluna lateral, do lado do numero da linha, definimos o breakpoint (ponto de parada)...
# ...este 'breaking point' no codigo abaixo está sendo colocado na linha 33, inicio da função e...
# ..linha 36, retorno da função
# Para executar o debug desta forma, agora vc clica com o botão direito em 'debug' em vez de 'run....
# ...ou clicar na Joaninha
# Caso existam erros no codigo, ele vai mostrando linha a linha. Basta clicar na Joaninha pra debbugar...
# .... e ir apertando f8

def dividir(a, b):
    print(f'a={a}, b={b}')
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err:
        return f'Ocorreu um problema: {err}'


print(dividir(4, 7))


# Exemplo com o PDB - Exemplo 1

# Para utilizar o python dubbuger, precisamos importar a biblioteca PDB e então a função set_trcar()
# Comando básicos do PDB:
# l - lista onde estamos no codigo
# n - proxima linha
# p - imprime variavel
# c - continua a execução (finaliza o debbuging)
import pdb

nome = 'Angelina'
sobrenome = 'Jolie'
pdb.set_trace()
nome_completo = nome + ' ' + sobrenome
curso = 'Programação em Python: Essencial'
final = nome_completo + ' faz o curso ' + curso
print(final)



# Exemplo com o PDB - Exemplo 2

# Para utilizar o python dubbuger, precisamos importar a biblioteca PDB e então a função set_trcar()
# Comando básicos do PDB:
# l - lista onde estamos no codigo
# n - proxima linha
# p - imprime variavel
# c - continua a execução (finaliza o debbuging)

nome = 'Angelina'
sobrenome = 'Jolie'
import pdb; pdb.set_trace()  # O import se encontra aqui agora.
nome_completo = nome + ' ' + sobrenome
curso = 'Programação em Python: Essencial'
final = nome_completo + ' faz o curso ' + curso
print(final)


# Porque utilizar o formato acima? O Debug é utilizado durante o desenvolvimento.
# Costumamos realizar todos os imports das bibliotecas no início do arquivo. Por isso, ao invés de colocarmos...
# ... o import do pdb no início do arquivo, nós colocamos somente onde vamos debugar e, ao finalizar, ...
# ... ja fazemos a remoção.




# Exemplo 3

# Para utilizar o python dubbuger, precisamos* importar a biblioteca PDB e então a função set_trcar()
# Comando básicos do PDB:
# l - lista onde estamos no codigo
# n - proxima linha
# p - imprime variavel
# c - continua a execução (finaliza o debbuging)


# - A partir do python 3.7, não e mais necessário importar a biblioteca pdb, pois o comando debug ....
# ... foi incorporado como função built-in (integrada) chamada breakpoint()

nome = 'Angelina'
sobrenome = 'Jolie'
breakpoint()
nome_completo = nome + ' ' + sobrenome
curso = 'Programação em Python: Essencial'
final = nome_completo + ' faz o curso ' + curso
print(final)

"""

# obs: Cuidado com conflitos entre nomes de variáveis e os do comandos do pdb

# Exemplo:


def soma(l, n, p, c):
    breakpoint()
    return l + n + p + c


print(soma(1, 3, 5, 7))

# Aqui as variaveis estão com o mesmo nome dos comandos do debug (l, n, p, c), para não dar conflitos entre os ....
# ....comandos e variaveis, devemos utilizar o comando ´p'(imprime variavel) + nome da variavel

# Evitar colocar nomes não representativos em variáveis. Sempre colocar nomes significativos
