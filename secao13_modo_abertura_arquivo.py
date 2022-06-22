"""
Modo de abertura de arquivos
r -> Abre para leitura - padrão
w -> Abre para escrita - Sobrescreve caso o arquivo já exista
x -> Abre para escrita somente se o arquivo não existir

a -> Abre para escrita adicionando conteúdo ao final do arquivo
obs: Abrindo no modo 'a' -> append, se o arquivo não existir, será criado. Caso exista, o novo conteúdo será ....
...adicionado ao final do arquivo.

+ -> Abre para o modo de atualização - leitura e escrita - usar com 'r', 'w'. Com 'a' ele adiciona conteúdo no final


Mais modos em :
http://docs.python.org/3/library/functions.html#open

# Exemplo 'x'
with open('university.txt', 'x') as arquivo:  # O 'x' cria um arquivo e permite escrita sobre ele e caso o arquivo...
    arquivo.write('Teste de conteúdo. \n')  # ..já exista, vai dar erro se usar o 'x'.

# Exemplo 'x' funcionando utilizando o tratamento de erro

try:
    with open('university.txt', 'x') as arquivo:
        arquivo.write('Teste de conteúdo 2 \n')
except FileExistsError:
    print('Arquivo já existe')

# Resposta: Arquivo já existe



# Exemplo 'a'

with open('frutas.txt', 'a') as arquivo:
    while True:
        fruta = input('Informe uma fruta ou sair: ')
        if fruta != 'sair':
            arquivo.write(fruta)
            arquivo.write('\n')
        else:
            break



# Exemplo +
with open('outro.txt', 'r+') as arquivo:  # Ele atualiza o arquivo
    arquivo.write('no topo!\n')
    arquivo.write('Nova linha\n')
    arquivo.write('Ultima linha')

# Resposta: no topo!
# Nova linha
# Ultima linha
"""

# Exemplo +
with open('outro.txt', 'a+') as arquivo:  # Ele atualiza o arquivo ao final dele.
    arquivo.write('Novo topo!\n')
    arquivo.write('Nova linha2\n')
    arquivo.write('Ultima linha2')

# Resposta: no topo!
# Nova linha
# Ultima linhaNovo topo!
# Nova linha2
# Ultima linha2


