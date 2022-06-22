"""
Sistema de arquivos - manipulação



# Descobrindo se um arquivo ou diretório existe

import os

print(os.path.exists('arquivo.txt'))
# Resposta: False - não existe

print(os.path.exists('frutas.txt'))
# Resposta: True

# Diretórios caminhos relativos (path relativos)

print(os.path.exists('geek'))
# Resposta: True

print(os.path.exists('geek/university'))  # Aqui é um path absolute
# Resposta: True

print(os.path.exists('outro'))
# Resposta: False


# Criando arquivos - Abaixo não são as melhores formas

# Forma 1
open('arquivo-teste.txt)', 'w').close()

# Forma 2
open('arquivo-teste2.txt', 'a').close()

# Forma 3
with open('arquivo-teste3.txt', 'w') as arquivo:
    pass  # Aqui não vai se colocar nada, por isso coloca-se o pass, pois a linha obriga identação.


import os

# Melhor forma para se criar arquivos
os.mknod('arquivo-teste4.txt')

os.mknod('/david/university.txt')

# Se o arquivo já existir, teremos o erro FileExist



# Criando diretórios

import os

os.mkdir('templates')  # path relativo

# A Função mkdir() cria um diretório, caso esse diretório já exista, vai dar erro FileExistError

os.mkdir('/home/David/teste')  # path absoluto


# obs: Se não tivermos permissão para criar um diretório, teremos um PermissionError



import os


# Não é possivel criar varios diretórios, só um por vez. Porém, da pra fazer conforme abaixo na sequência
os.mkdir('templates')
os.mkdir('templates/geek')
os.mkdir('templates/geek/university')

# Resposta: Deu certo, foi criado.



# Porém, estamos trabalhando com Python, e sempre existe uma saída mais fácil.

import os

os.makedirs('templates/geek/university')

# Resposta: Criado diretórios dentro de diretórios.


# Obs: Se os diretórios já existirem, vai dar FileExistsError


import os

# tratar um erro
os.makedirs('templates2/geek2/university', exist_ok=True)  # Aqui ele vai repetir a criação sem dar erros.
# Resposta: Ele vai criar, recriar, sem dar erro.



import os

# Renomear arquivos e diretórios

# os.rename('templates', 'templates3')
# Resposta: Renomeado

# os.rename('templates2/geek2', 'teste')
# Resposta: alterado o nome do diretório dentro do diretório templates2

# obs: Se o diretório não existir, teremos um FileNotFoundError

# obs: Se o diretório que queremos renomear não estiver vazio, teremos um OSError


# Renomear aquivos

# os.rename('teste/university/arquivo-teste.txt)', 'arquivo-teste.txt')
# Renomeou arquivo acima

os.rename('geek2/outro2/teste.txt', 'geek2/outro2/geek.txt')  # Aqui temos que passar o caminho para mudarmos o nome...
# ... do arquivo para não correr o risco de sumir com o arquivo




import os

# Deletar arquivos

# Atenção. Tome cuidado com os comandos de deletar. Ao deletar um arquivo ou diretório, eles não vão para a lixeira.]

os.remove('geek2/outro2/geek.txt')

# obs: Se vc estiver no windows, se o arquivo estiver aberto, dará erro.

# obs: Caso o arquivo não exista, teremos um FileNotFoundError

# obs: Se você informar um diretório ao invés de um arquivo, teremos um IsADirectoryError



# Remover diretórios

import os

os.rmdir('templates2')
# Apagou diretório

# obs: Caso o diretório não estiver vazio, teremos um OSError

# Obs: Se o diretório não existir, teremos um FileNotFoundError



import os

# Removendo uma arvore de diretórios

os.removedirs('geek2/outro2')
# Removido.

# obs: para remover diretórios, é necessário que eles estejam vazios


# Existe uma maneira de mandar para a lixeira, é necessário instalar o pacote externo 'send2trash' indo no terminal...
# ... e executando pip install send2trash
import os
from  send2trash import send2trash

os.remove('frutas.txt')  # removendo permanentemente
send2trash('frutas2.txt')  # neste caso, vai para a lixeira. Pode ser reatauado

# send2trash apaga arquivos e diretórios, direto para a lixeira




# Trabalhando com arquivos e diretórios temporários

import os
import tempfile

with tempfile.TemporaryDirectory() as tmp:
    print(f'Criei um diretório temporário em {tmp}')
    with open(os.path.join(tmp, 'arquivo_temporario.txt'), 'w') as arquivo:
        arquivo.write('geek univeristy\n')
    input()
# Resposta: Criei um diretório temporário em /tmp/tmpygzms__j

# após a resposta acima, se der mais um enter no console, o arquivo e diretório temporários somem. a função input()...
# ... serve apenas para manter os diretórios e arquivos 'vivos' temporariamente.

# possivelmente esse codigo acima não funcionará no windows.



# Trabalhando com arquivos e diretórios temporários

import os
import tempfile

# Criando um arquivo temporário

with tempfile.TemporaryFile() as tmp:
    tmp.write(b'Geek Univeristy\n')  # Aqui se converte uma string em binário
    tmp.seek(0)
    print(tmp.read())  # Aqui é um comando para ESCREVER
# Resposta:
# Connected to pydev debugger (build 221.5080.212)
# b'Geek Univeristy\n'

# obs: Em arquivos temporários só conseguimos escrever bits. Por isso usamos o b''


"""

import os
import tempfile

# outra forma de fazer a mesma coisa acima, sem o bloco with

arquivo = tempfile.TemporaryFile()
arquivo.write(b'Geek Univeristy')
arquivo.seek(0)
print(arquivo.read())
arquivo.close()


# https://docs.python.org/3/library/os.html?highlight=os#module-os