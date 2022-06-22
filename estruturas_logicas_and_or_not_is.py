"""
Etruturas logicas: and (e), or (ou), not (não), is (é)

Nós temos os operadores unários: not, is
E os operadores binários: and, or

Para and, ambos os valores precisam ser verdadeiros (True)
Para or, um dos valores precisam ser verdadeiros (True)
Para not, o valor do booleano é invertido, ou seja, se for True vira False, se for False, vira True
Para o is, o primeiro valor é comparado com o segundo, pra dizer se é verdadeiro ou falso. 1 = 1 = verdadeiro, 1=2 falso.

"""

"""ativo = True
logado = True

if ativo and logado:
    print('Bem-vindo Usuário!')
else:
    print('Você precisa ativar sua conta. Por favor, cheque seu email')
"""
"""
Acima, se alterar a variável "ativo" para False ou True, ele vai dar respostas diferentes
"""

"""
ativo = True
logado = False

if not ativo:
    print('Você precisa ativar sua conta, cheque seu email')
else:
    print('Bem-vindo Usuario')

#Abaixo o porque de ser o operador de negação. De o play e veja o resultado
print(not False)

"""

ativo = False
logado = True

if ativo:
    print('Você precisa ativar sua conta, cheque seu email')
else:
    print('Bem-vindo Usuario')

#Ativo é True?, o "is" diz se é verdadeiro ou não, conforme abaixo. Teste mudando a variável "ativo"
print(ativo is True)


