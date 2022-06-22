"""
O bloco with

Passos para se trabalhar com arquivos
1 - abrimos arquivos
2 - maninipulando os arquivos
3 - fechando os arquivos

O bloco with é utilizado para criar um contexto de trabalho onde os recursos utilizados são fechados após o ...
bloco with

"""

# o bloco with

with open('texto.txt') as arquivo:
    print(arquivo.readlines())
    print(arquivo.closed)
# Resposta: ['Este é um arquivo teste para a seção 13 - leitura de arquivos.\n', 'Mas é assim mesmo.
# \n', 'As coisas são como elas são.\n', 'Quero mudar logo de emprego.\n', 'Vou lutar muito para isso.']
# False  -> pois o arquivo, dentro do bloco with, está aberto

# Após a utilização, o arquivo será fechado. Essa é a forma pytonica de fechar os arquivos.

print(arquivo.closed)
# Reposta: True -> pois, fora do block with, o arquivo está fechado