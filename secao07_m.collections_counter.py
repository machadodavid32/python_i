"""
Modulo Collections - Counter (contador)

Colletcions - High-Performance Container Datetypes

counter - recebe um interável como parametro e cria um objeto do tipo collections counter que é parecido com um
dicionário, contendo como chave um elemento da lista passada como parametro e como valor a quantidade de ocorrências deste elemento.


#utilizando o Counter


#Exemplo 1

#Realizando o import
from collections import Counter

#Podemos utilizar qualquer iterável. Aqui abaixo utilizamos lista
lista = [1, 1, 1, 2, 2, 3, 3, 3, 3, 1, 1, 2, 2, 4, 4, 4, 5, 5, 5, 3, 45, 45, 45, 66, 66, 43, 34]

#Realizando o counter
res = Counter(lista)

print(type(res))
print(res)
#Resposta: <class 'collections.Counter'>
# Counter({1: 5, 3: 5, 2: 4, 4: 3, 5: 3, 45: 3, 66: 2, 43: 1, 34: 1})  >Resultou num dicionário
#Traduzindo acima, para o elemento 1, nos temos 5 ocorrências, para o elemento 3, nós temos 5 ocorrência
#para o elemento 2, nó temos 4 ocorrências e por ai vai




#Exemplo 3

from collections import Counter

print(Counter('Geek University'))
#Resposta: Counter({'e': 3, 'i': 2, 'G': 1, 'k': 1, ' ': 1, 'U': 1, 'n': 1, 'v': 1, 'r': 1, 's': 1, 't': 1, 'y': 1})

"""

from collections import Counter

texto = """Hoje a Games Industry liberou os dados oficiais de vendas no território 
britânico durante o último mês de 2021, Dezembro. Como reportado antes, os Xbox Series X|S tiveram um mês bastante
 forte com aumento de 108% nas vendas, e graças a isso, o console foi o segundo mais vendido em Dezembro na região, 
 batendo o seu  recorde no lançamento e ultrapassando a marca de 1 milhão de unidades vendidas no Reino Unido."""

palavras = texto.split()
print(palavras)
#Resposta: ['Hoje', 'a', 'Games', 'Industry', 'liberou', 'os', 'dados', 'oficiais', 'de', 'vendas', 'no', 'território', 'britânico', 'durante', 'o', 'último', 'mês', 'de', '2021...
#Acima ele destaca cada palavra do texto acima

res = Counter(palavras)
print(res)
#Resposta: Counter({'de': 5, 'o': 4, 'a': 3, 'no': 3, 'os': 2, 'mês': 2, 'e': 2, 'Hoje': 1, 'Games': 1, 'Industry': 1, 'liberou': 1, 'dados': 1, 'oficiais': 1, 'vendas
#Acima, ele conta as ocorrências para cada palavra em um texto.

print(res.most_common(5)) #Encontrar as 5 palavras que mais aparecem no texto.
#[('de', 5), ('o', 4), ('a', 3), ('no', 3), ('os', 2)]


