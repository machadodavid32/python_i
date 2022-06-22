"""
Seek e cursors

seek() é utilizada para movimentar o cursor pelo arquivo.



arquivo = open('texto.txt')
print(arquivo.read())

# A função seek() é utlizada para movimentação do cursor pelo arquivo. Ele recebe um parâmetro que avisa ...
# ...onde queremos colocar o cursos.

# Movimentando o cursor pelo arquivo com a função seek()

arquivo.seek(0)

print(arquivo.read())
# Resposta: Este é um arquivo teste para a seção 13 - leitura de arquivos.
# Mas é assim mesmo.
# Este é um arquivo teste para a seção 13 - leitura de arquivos.
# Mas é assim mesmo.

# Veja, agora conseguimos imprimir o texto duas vezes pois, com o seek na posição 0, o cursor retornou ao começo...
# ... após a execução do primeiro read

# O seek() pode ser usado em qualquer posição.


arquivo = open('texto.txt')

# readline() -> Função que le o arquivo linha a linha
print(arquivo.readline())  # Imprime a primeira linha.
# Resposta: Este é um arquivo teste para a seção 13 - leitura de arquivos.
print(arquivo.readline())  # ao repetir, ele imprime a segunda linha
# Resposta: Mas é assim mesmo.

print(arquivo.readlines())  # O comando readlines, com s no final, devolve uma lista com as linhas do arquivo
# Resposta: ['As coisas são como elas são.\n', 'Quero mudar logo de emprego.\n', 'Vou lutar muito para isso.']
x
linhas = arquivo.readlines()
print(len(linhas))  # Criei uma variavel para saber quantas linhas tem o texto utilizando o comando len
# Resposta: 3


['As coisas são como elas são.\n', 'Quero mudar logo de emprego.\n', 'Vou lutar muito para isso.']
# Obs: Quando abrimos uma arquivo com a função open() é criado uma conexão entre o arquivo no disco dp computador...
# ... e o nosso programa. Essa conexão é chamada de streaming. Ao finalizar os trabalhos com o arquivo, devemos...
# ...fechar essa conexão. Para isso utilizamos a função close()

# Passos para se trabalhar com um arquivo.

# 1 - Abrir o arquivo
arquivo = open('texto.txt')

# 2 - Trabalhar o arquivo
print(arquivo.read())
print(arquivo.closed)  # Verifica se o arquivo está aberto ou fechado. False para aberto
# 3 - Fechar o arquivo
arquivo.close()
print(arquivo.closed)  # Aqui deve dar True para arquivo fechado

# Se tentarmos manipular um arquivo após seu fechamento, teremos um ValueError

"""

arquivo = open('texto.txt')
print(arquivo.read(50))  # Aqui nós limitados a quantidade de caracteres a ser lido no arquivo, começando do começo.


