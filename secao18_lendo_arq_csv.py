"""
Lendo arquivos CSV

CSV - Comma Separeted Values - Valores separados por virgula

# Separador por virgula, 1, 2, 3, 4, 5, 'ggek', 'university', 'David'

# Separador por ponto e virgula, 1; 2; 3; 4; ....

# Separador por espaço, 1 2 3 4 5



# Forma não ideal (trabalhoso)
with open('lutadores.csv') as arquivo:
    dados = arquivo.read()
    print((type(dados)))
    dados = dados.split(',')
    print(dados)

# Resposta: <class 'str'>
# Nome,País,Altura (em cm)
# Ryu,Japão,175
# Ken,EUA,175
# Chun-Li,China,165
# Guile,EUA,185
# E. Honda,Japão,185
# Dhalsim,Índia,176
# Blanka,Brasil,192
# Zangief,Rússia,214
# ['Nome', 'País', 'Altura (em cm)\nRyu', 'Japão', '175\nKen', 'EUA', '175\nChun-Li', 'China', '165\n
# Guile', 'EUA', '185\nE. Honda', 'Japão', '185\nDhalsim', 'Índia', '176\n
# Blanka', 'Brasil', '192\nZangief', 'Rússia', '214']

# Reparar que, ao colocarmos o comando split, ele lança uma lista

A Linguagem Python possui duas formas diferentes para ler arquivos CSV:
Reader - Permite que iteremos sobre as linhas do arquivo CSV como listas;
Dictreader - Permite que iteremos sobre as linhas do arquivo CSV como OrderedDict.



# Exemplo:

from csv import  reader

with open('lutadores.csv') as arquivo:
    leitor_csv = reader(arquivo)
    next(leitor_csv)  # Pula o cabeçalho
    for linha in leitor_csv:
        # Cada linha é uma lista
        print(f'{linha[0]} nasceu no(a)(s) {linha[1]} e mede {linha[2]} centímetros')

# Resposta:
# Ryu nasceu no(a)(s) Japão e mede 175 centímetros
# Ken nasceu no(a)(s) EUA e mede 175 centímetros
# Chun-Li nasceu no(a)(s) China e mede 165 centímetros
# Guile nasceu no(a)(s) EUA e mede 185 centímetros
# E. Honda nasceu no(a)(s) Japão e mede 185 centímetros
# Dhalsim nasceu no(a)(s) Índia e mede 176 centímetros
# Blanka nasceu no(a)(s) Brasil e mede 192 centímetros
# Zangief nasceu no(a)(s) Rússia e mede 214 centímetros



# DictReader

from csv import DictReader

with open('lutadores.csv') as arquivo:
    leitor_csv = DictReader(arquivo)
    for linha in leitor_csv:
        # Para cada linha é um orderdict
        print(f"{linha['Nome']} nasceu no(a)(s) {linha['País']} e mede {linha['Altura (em cm)']} ")

# Resposta: Ryu nasceu no(a)(s) Japão e mede 175
# Ken nasceu no(a)(s) EUA e mede 175
# Chun-Li nasceu no(a)(s) China e mede 165
# Guile nasceu no(a)(s) EUA e mede 185
# E. Honda nasceu no(a)(s) Japão e mede 185
# Dhalsim nasceu no(a)(s) Índia e mede 176
# Blanka nasceu no(a)(s) Brasil e mede 192
# Zangief nasceu no(a)(s) Rússia e mede 214

"""

# Com outro separador
from csv import DictReader

with open('lutadores.csv') as arquivo:
    leitor_csv = DictReader(arquivo, delimiter=';')  # Neste caso, se o delimitador fosse ;(ponto e virgula) e não virgula
    for linha in leitor_csv:
        # Para cada linha é um orderdict
        print(f"{linha['Nome']} nasceu no(a)(s) {linha['País']} e mede {linha['Altura (em cm)']} ")