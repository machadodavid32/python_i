"""
Leitura de arquivos

Para o conteúdo de um arquivo em Python, utilizamos a função integrada open(), que significa 'abrir'.
open() -> Na forma mais simples de utilização nós passamos apenas um parâmetro de entrada que, neste caso,
é o caminho para o arquivo ser lido. Essa função retorna um _io.TextIOWrapper e é com ele que trabalhamos então.

https://docs.python.org/3/library/functions.html#open

obs: Por padrão, o open() abre o arquivo para leitura. Este arquivo deve existir, caso não exista, teremos um erro
chamado FileNotFoundError

<_io.TextIOWrapper name='texto.txt' mode='r' encoding='UTF-8'>

mode='r' -> 'r' vem de read, que significa ler. Aqui é o modo leitura
encoding='UTF-8' -> todos a acentuação será aceita

"""

# Exemplo
arquivo = open('texto.txt')  # Arquivo que criei chamado texto.txt abaixo de guppe
print(arquivo)
print(type(arquivo))

# Resposta: <_io.TextIOWrapper name='texto.txt' mode='r' encoding='UTF-8'>
# <class '_io.TextIOWrapper'>

# Para ler o conteúdo de um arquivo, utilizar a função read()

print(arquivo.read())
# Resposta: Este é um arquivo teste para a seção 13 - leitura de arquivos.

# obs: O python utiliza um recurso chamado 'cursor'para trabalhar com arquivos. Este cursor funciona como ...
# ...cursor quando estamos escrevendo.

# obs: A função read() le todo o conteúdo do arquivo.
