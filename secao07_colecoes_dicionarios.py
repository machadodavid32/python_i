"""
Em algumas linguagens de programação são conhecidos por mapas.

Dicionarios são coleções do tipo chave/valor

Dicionários são representados por chave {}.

OBS:
Tanto chave como o valor pode ser de qualquer tipo
Chave e valor são separados por dois pontos - 'br': 'Brasil'
Podemos misturar tipos de dados
"""
"""
#print(type({}))
#Resposta: <class 'dict'>


#***Criação de dicionários***

#FORMA 1 (mais comum)
paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'} #le-se chaves, dois pontos, valor
print(paises)
print(type(paises))
#Resposta:
# {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}
#<class 'dict'>

#FORMA 2 (menos comum)

paises = dict(br='Brasil', eua='Estados Unidos', py='Paraguai')
print(paises)
print(type(paises))
#Resposta:
# {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}
# <class 'dict'>



#Acessando elementos

paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}

# FORMA - Acessando via chave, da mesma forma que lista/tupla

print(paises['br'])
print(paises['py'])
#Resposta:
# Brasil
#Paraguai

#Caso utilizamos uma acesso para uma chave que não existe, vai dar erro.

# FORMA 2 - Acessando via get - recomendada

print(paises.get('br'))
print(paises.get('py'))
print(paises.get('ru'))
#Brasil
#Paraguai
#None - tipo de dado que representa o tipo sem tipo, ou poderia ser conhecido também como tipo vazio, porém,
#falar que é um tipo sem tipo é mais apropriado.

#Caso o get não encontre o objeto com a chave informada, será retonado o valor None e não vai dar mensagem de erro
paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}
pais = paises.get('py')
if pais:
    print(f'Encontrei o país {pais}')
else:
    print('Não encontrei o país')
#Resposta:
# Encontrei o país Paraguai



paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}
pais = paises.get('ru', 'Não encontrado')
print(f'Encontrei o país {pais}')
#Resposta: Encontrei o país Não encontrado

#Abaixo com py

#Podemos definir um valor padrão para caso não encontremos um objeto com a chave informada
paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}
pais = paises.get('py', 'Não encontrado')
print(f'Encontrei o país {pais}')
#Resposta:
#Encontrei o país Paraguai


paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}
#Podemos verificar se determinada chave se encontra em um dicionário
print('br' in paises)
print('ru' in paises)
print('Estados Unidos' in paises)
#Resposta:
#True
#False
#False > Estados Unidos é valor, por isso deu False.



#Podemos utilizar qualquer tipo de dado (int, float, string, booleano), inclusive lista, tupla, dicionario
#oomo chaves de dicionários.
#Exemplo:
#Tuplas, por exemplo, são bastante utilizadas como chaves de dicionarios, pois as mesmas são imutáveis
localidades = {
    (35.6895, 39.6917): 'Escritório em Tokio',
    (40.7128, 74.0060): 'Escritório em Nova York',
    (37.7749, 122.4194): 'Escritório em São Paulo'
}
print(localidades)
print(type(localidades))
#Resposta: {(35.6895, 39.6917): 'Escritório em Tokio', (40.7128, 74.006): 'Escritório em Nova York', (37.7749, 122.4194): 'Escritório em São Paulo'}
#<class 'dict'>



#Adicionar elementos em um dicionário

receita = {'jan': 100, 'fev': 120, 'mar': 300}
print(receita)
print(type(receita))
#Resposta:
# {'jan': 100, 'fev': 120, 'mar': 300}
#<class 'dict'>

#FORMA 1 - mais comum
receita['abr'] = 350
print(receita)
#resposta: {'jan': 100, 'fev': 120, 'mar': 300, 'abr': 350}

#FORMA 2
novo_dado = {'mai': 500}
receita.update(novo_dado) #poderia também fazer receita.update({'mai': 500})
print(receita)
#Resposta: {'jan': 100, 'fev': 120, 'mar': 300, 'abr': 350, 'mai': 500}

#Atualizando dados em um dicionário
#FORMA 1
receita['mai'] = 550
print(receita)
#Resposta: {'jan': 100, 'fev': 120, 'mar': 300, 'abr': 350, 'mai': 550}

# FORMA 2
receita.update({'mai': 600})
print(receita)
#Resposta: {'jan': 100, 'fev': 120, 'mar': 300, 'abr': 350, 'mai': 600}

#Conclusão 1 - A forma de adicionar novos elementos ou atualizar dados em um dicionário é a mesma
#Conclusão 2 - Em dicionários NÃO podemos ter chaves repetidas. Se fizer isso pode subsecrever os dados anteriores



#Remover dados de um dicionário

#FORMA1 -
receita = {'jan': 100, 'fev': 120, 'mar': 300}
print(receita)
receita.pop('mar')
print(receita)
#{'jan': 100, 'fev': 120, 'mar': 300}
#{'jan': 100, 'fev': 120}  > 'mar' foi retirado

#obs1: No "pop" sempre precisamos informar a chave e, caso não encontre o elemento, um KeyError é retonnado.
#obs2: Ao remover o objeto, ele retorna o valor do objeto

#FORMA 2 - forma mais comum
del receita['fev']
print(receita)
#resposta: {'jan': 100}

del receita['fev'] #Se a chave não existir, da erro. Acima ja excluimos fevereiro
#OBS: Neste caso não retorna o valor



#ONDE USAR DICIONARIOS -
#Imagina se você tem um comercio eletrônico, onde temos um carrinho de compras na qual adicionamos produtos.
"""
"""Carrinho de compras:
   produto1:
        nome:
        quantidade:
        preço:
   produto2:
        nome:
        quantidade:
        preço:     
"""
"""

# 1 - Poderíamos utiliar uma Lista para isso? sim.

carrinho = []
produto1 = ['Playstation 4', 1, 2300]
produto2 = ['God of War', 1, 150]

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)
#Resposta: [['Playstation 4', 1, 2300], ['God of War', 1, 150]]
#Teríamos de saber qual é o indice de cada informação do produto

# 2 - Poderiamos utilizar uma Tupla para isso?

produto1 = ('Playstation 4', 1, 2300)
produto2 = ('God of war', 1, 150)
carrinho = (produto1, produto2)
print(carrinho)
#Resposta: (('Playstation 4', 1, 2300), ('God of war', 1, 150))

# 3 - Poderíamos utilizar um dicionário para isso? Sim

carrinho = []
produto1 = {'nome': 'Playsation 4', 'Quantidade': 1, 'Preço': 2300}
produto2 = {'nome': 'God of War', 'Quantidade': 1, 'Preço': 150}

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)
#Resposta: [{'nome': 'Playsation 4', 'Quantidade': 1, 'Preço': 2300}, {'nome': 'God of War', 'Quantidade': 1, 'Preço': 150}]]
#Desta forma, facilmente, adicionamos ou removemos produtos do carrinho. E em cada produto podemos ter certeza sobre cada informação.



d = dict(a=1, b=2, c=3) #outro metodo de criar um dicionario
print(d)
print(type(d))
#Resposta:
# {'a': 1, 'b': 2, 'c': 3}
#<class 'dict'>

#d.clear() #zera o dicionario
#print(d)
#Resposta: {}


#Copiando um dicionario para outro

# FORMA 1 - Deep Copy
novo = d.copy()
print(novo)

novo['d'] = 4

print(d)
print(novo)
#REsposta:
#{'a': 1, 'b': 2, 'c': 3}
#{'a': 1, 'b': 2, 'c': 3, 'd': 4}


# FORMA 2 - Shallow Copy

d = dict(a=1, b=2, c=3) #outro metodo de criar um dicionario
print(d)
print(type(d))

novo = d
print(novo)

novo['d'] = 4
print(d)
print(novo)
#Resposta:
# {'a': 1, 'b': 2, 'c': 3}
# <class 'dict'>
# {'a': 1, 'b': 2, 'c': 3}
# {'a': 1, 'b': 2, 'c': 3, 'd': 4} #Repare que os dois foram alterados conforme abaixo
# {'a': 1, 'b': 2, 'c': 3, 'd': 4} # Repare que os dois foram alterados conforme acima
"""

#Forma não usual de criação de dicionários

outro = {}.fromkeys('a', 'b')
print(outro)
print(type(outro))
#Resposta:
# {'a': 'b'}
# <class 'dict'>

usuario = {}.fromkeys(['nome', 'pontos', 'email', 'profile'], 'desconhecido')
print(usuario)
print(type(usuario))
#Resposta:
# {'nome': 'desconhecido', 'pontos': 'desconhecido', 'email': 'desconhecido', 'profile': 'desconhecido'}
# <class 'dict'>
#No caso acima, o 'desconhecido' virou valor para cada chave

#Obs: O método fromkeys recebe dois parametros, dois dados, um iterável(siginifca algo como repetição ) e um valor. Ele vai gera para cada valor do
#iterável uma chave e ira atribuir a esta chave o valor informado.

veja = {}.fromkeys('teste', 'valor')
print(veja)
#Resposta: {'t': 'valor', 'e': 'valor', 's': 'valor'} #para cada letra do 'teste', ele atribuiu o valor 'valor'

veja = {}.fromkeys(range(1, 11), 'novo')
print(veja)
#Resposta: {1: 'novo', 2: 'novo', 3: 'novo', 4: 'novo', 5: 'novo', 6: 'novo', 7: 'novo', 8: 'novo', 9: 'novo', 10: 'novo'}

