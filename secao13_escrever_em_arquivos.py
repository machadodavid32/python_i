"""
Escrevendo em arquivos

Obs: Ao abrir um arquivo para leitura, não podemos realizar a escrita dele. Apenas ler. Da mesma forma, se abrirmos
um arquivo para escrita, não podemos lê-lo, somente escrever.



# Exemplo de escrita - modo 'w' - write(escrita)

with open('novo.txt', 'w') as arquivo:
    arquivo.write("Novos dados.\n")
    arquivo.write("outros colocar quantoas linhas quisermos.\n")
    arquivo.write("Mais é a ultima linha")

# obs: Ao abrir um arquivo para escrita, um arquivo é criado no sistema operacional.

# Para escrevermos dados em um arquivo, após abrir o arquivos utilizamos a função write()...
# Esta função recebe uma string como parâmetro, caso contrário, teremos um TypeError

# Abrindo um arquivo para escrita com o modo 'w', se o arquivo não existir, será criado. Caso ele já exista, será...
# ...modificado, perdendo o conteúdo original.


# Forma tradicional de escrita em arquivo (não pythonica)
arquivo = open('mais.txt', 'w')
arquivo.write("Um texto qualquer.\n")
arquivo.write("Mais um texto")
arquivo.close()

# Forma pythonica
with open('novo.txt', 'w') as arquivo:
    arquivo.write("Novos dados.\n")
    arquivo.write("outros colocar quantoas linhas quisermos.\n")
    arquivo.write("Mais é a ultima linha")



with open('Geek', 'w') as arq:
    arq.write('Geek ' * 50)
"""

with open('frutas.txt', 'w') as arquivo:
    while True:
        fruta = input('Informe uma fruta ou digite sair: ')
        if fruta != 'sair':
            arquivo.write(fruta + '\n')
        else:
            break


