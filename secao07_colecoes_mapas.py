"""Mapas sõ conhecidos em mapas como Dicionários
Dicionários em mapas são representados por chaves {}



receita = {'jan': 100, 'fev': 250, 'mar': 400}
print(receita)

for chave in receita:
    print(chave)

for chave in receita:
    print(receita[chave])

#Resposta:
# {'jan': 100, 'fev': 250, 'mar': 400}
# jan
# fev
# mar
# 100
# 250
# 400

for chave in receita:
    print(f'{chave} : {receita[chave]}')
#Resposta:
# jan : 100
# fev : 250
# mar : 400

#pode ser feito como abaixo para uma melhor formação.
for chave in receita:
    print(f'em {chave} recebi R$ {receita[chave]}')
#Resposta:
# em jan recebi R$ 100
# em fev recebi R$ 250
# em mar recebi R$ 400


#Acessando as chaves

receita = {'jan': 100, 'fev': 250, 'mar': 400}
print(receita)
print(receita.keys())
#Resposta: dict_keys(['jan', 'fev', 'mar'])

for chave in receita.keys():
    print(receita[chave])
#Resposta: 100
# 250
# 400



  #Acessando os valores:

receita = {'jan': 100, 'fev': 250, 'mar': 400}
print(receita)
print(receita.values())
#Resposta:
# {'jan': 100, 'fev': 250, 'mar': 400}
# dict_values([100, 250, 400])

for valor in receita.values():
    print(valor)
#Resposta:
# 100
# 250
# 400



receita = {'jan': 100, 'fev': 250, 'mar': 400}
print(receita)

#Desempacotamento de dicionários

for chave, valor in receita.items():
    print(f'chave={chave} e valor={valor}')
#Resposta: {'jan': 100, 'fev': 250, 'mar': 400}
# chave=jan e valor=100
# chave=fev e valor=250
# chave=mar e valor=400

print(receita.items())
#Resposta: dict_items([('jan', 100), ('fev', 250), ('mar', 400)])

"""

#Soma*, valor_maximo*, valor_minimo*, Tamanho
# * se os valores forem inteiros ou reais

receita = {'jan': 100, 'fev': 250, 'mar': 400}
print(receita)
print(sum(receita.values()))
print(max(receita.values()))
print(min(receita.values()))
print(len(receita))
#Resposta: {'jan': 100, 'fev': 250, 'mar': 400}
# 750
# 400
# 100
# 3


