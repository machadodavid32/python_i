"""
Filter

filter() -> serve para filtrar dados de uma determinada coleção.

valores = 1, 2, 3, 4, 5, 6
media = (sum(valores) / len(valores))
print(media)
# Resposta: 3.5


import statistics  # Biblioteca para trabalhar com dados estatísticos


# coletar dados de algum sensor

dados = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]

# Calculando a media dos dados utilizados utilizando a função mean()

media = statistics.mean(dados)
print(f'a média é {media} ')

# Obs: Assim como a função map(), a filter() recebe dois parâmetros, sendo uma função e um iterável.

res = filter(lambda x: x > media, dados)  # Aqui vamos filtrar valores maiores que a media.
print(list(res))

# Resposta: a média é 2.183333333333333
# [2.7, 4.1, 4.3]


# Obs: Assim como na função map(), após serem utilizados os dados de filter(), serão excluídos da memoria.


paises = ['', 'Argentina', '', 'Brasil', 'Chile', '', 'Colombia', '', 'Equador', '', '', 'Venezuela']
print(paises)
# Resposta: ['', 'Argentina', '', 'Brasil', 'Chile', '', 'Colombia', '', 'Equador', '', '', 'Venezuela']
res = filter(None, paises)
print(list(res))
# Resposta:  ['Argentina', 'Brasil', 'Chile', 'Colombia', 'Equador', 'Venezuela'] Aqui sem espaços em branco.



paises = ['', 'Argentina', '', 'Brasil', 'Chile', '', 'Colombia', '', 'Equador', '', '', 'Venezuela']
res = filter(lambda pais: len(pais) > 0, paises)
print(list(res))
# Resposta: ['Argentina', 'Brasil', 'Chile', 'Colombia', 'Equador', 'Venezuela'] Aqui outro modo de fazer o mesmo acima.

# A diferença entre map() e filter() é:
# Na map() recebe dois parâmetros, uma função e um iterável e retorna um objeto mapeando a função para cada elemento do iterável
# Na filter() recebe dois parâmetros, uma função e um iterável e retorna um objeto filtrando apenas os elementos de acordo com a função.



# Exemplo mais complexo

usuarios = [
    {"Usarname": "Samuel", "tweets": ["Eu adoro bolos", "Eu adoro pizzas"]},
    {"Usarname": "Carla", "tweets": ["Eu amo meu gato"]},
    {"Usarname": "Jeff", "tweets": []},
    {"Usarname": "bob123", "tweets": []},
    {"Usarname": "dogoo", "tweets": ["Eu gosto de cachorro", "Vou sair hoje"]},
    {"Usarname": "gal", "tweets": []}
    ]

print(usuarios)
# Resposta: [{'Usarname': 'Samuel', 'tweets': ['Eu adoro bolos', 'Eu adoro pizzas']}, {'Usarname': 'Carla', 'tweets': ['Eu amo meu gato']},
# {'Usarname': 'Jeff', 'tweets': []}, {'Usarname': 'bob123', 'tweets': []},
# {'Usarname': 'dogoo', 'tweets': ['Eu gosto de cachorro', 'Vou sair hoje']}, {'Usarname': 'gal', 'tweets': []}]

# Filtrar os usuarios que estão inativos no Twetter (abaixo)
inativos = list(filter(lambda u: len(u['tweets']) == 0, usuarios))
print(inativos)
# Resposta:
# [{'Usarname': 'Jeff', 'tweets': []}, {'Usarname': 'bob123', 'tweets': []}, {'Usarname': 'gal', 'tweets': []}]
# Ele vai pegar todos os tweets zerados da lista

# Refatorando - forma 2
inativos = list(filter(lambda u: not u['tweets'], usuarios))
print(inativos)
# Resposta:
# [{'Usarname': 'Jeff', 'tweets': []}, {'Usarname': 'bob123', 'tweets': []}, {'Usarname': 'gal', 'tweets': []}]


"""

# Combinar filter e map

nomes = ['Vanessa', 'Ana', 'Maria']
# Devemos criar uma lista contendo 'Sua instruttora é' + nome, desde cada tenha menos de 5 caracteres

lista = list(map(lambda nome: f'Sua instrutora é {nome}', filter(lambda  nome: len(nome) < 5, nomes)))
print(lista)
# Resposta: ['Sua instrutora é Ana']


