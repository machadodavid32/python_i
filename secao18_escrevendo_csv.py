"""
Escrevendo em arquivos CSV

writer() - escritor
writerow() - Escreve uma linha


# writer() -> Gera um objeto para que possamos escrever um arquivo CSV.
# Writerow() -> é utilizado para escrever cada linha. Este método recebe uma lista

from csv import writer

with open('filmes.csv', 'w') as arquivo:  # o 'w' diz ao sistema que vai criar o arquivo filmes.csv
    escritor_csv = writer(arquivo)
    filme = None  # Coloca None para a variavel não sair do loop enquanto não digitar sair
    escritor_csv.writerow(['titulo', 'Gênero', 'Duração'])
    while filme != 'sair':
        filme = input('Informe o nome do filme: ')
        if filme != 'sair':
            genero = input('Informe o gênero: ')
            duracao = input('Informe a duração: ')
            escritor_csv.writerow([filme, genero, duracao])

"""

# DictWriter - Aqui trabalhamos com dicionários

# OBS: As chaves do dicionário devem ser as mesmas utilizadas como cabeçalho

from csv import DictWriter

with open('filmes3.csv', 'w') as arquivo:
    cabecalho = ['Titulo', 'Gênero', 'Duração']
    escritor_csv = DictWriter(arquivo, fieldnames=cabecalho)
    escritor_csv.writeheader()
    filme = None
    while filme != 'sair':
        filme = input('Informe o nome do Filme: ')
        if filme != 'sair':
            genero = input('Informe o genero: ')
            duracao = input('Informe a duração: ')
            escritor_csv.writerow({"Titulo": filme, "Gênero": genero, "Duração": duracao})


