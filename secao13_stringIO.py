"""
StringIO

Atenção - para ler ou escrever dados em arquivos do sistema operacional, o software precisa de permissão para:
 - Permissão leitura -> para ler o arquivo
 - Permissão de escrita -> para escrever o arquivo

StringIO -> Utilizado para ler e criar arquivos em memória.
"""

# Para utilizar o stringIO, primeiro precisamos fazer o import

from io import StringIO

mensagem = "Está é apenas uma string normal"

# Podemos criar um arquivo em memória já com uma string inserida ou mesmo vazio para inserirmos texto depois.
arquivo = StringIO(mensagem) # esta linha de comando é a mesma que arquivo = open('arquivo.txt', 'w')

# Agora tendo o arquivo, podemos utilizar tudo que já sabemos.
print(arquivo.read())

# Resposta: Está é apenas uma string normal
# Veja que não foi criado um arquivo, apenas ficou na memória.

# Escrevendo outros textos
arquivo.write('Mais um texto')

# Movimentando o cursor para o inicio
arquivo.seek(0)

print(arquivo.read())
# Resposta: Está é apenas uma string normal
# Está é apenas uma string normalMais um texto




