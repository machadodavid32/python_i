"""
Modulo Collections - Default Dict

"""

"""
#relembrando dicionário
dicionario = {'curso' : 'Programação em Python Esencial'}
print(dicionario)
print(dicionario['curso'])
#Resposta: {'curso': 'Programação em Python Esencial'}  > Imprimiu dicionário
# Programação em Python Esencial > imprimiu o valor da chave 'curso'
#Nos dicionário se solicitar uma chave que não existe, aparece o 'keyError'


Ao criar um dicionario utlizando o Default Dict nós informamos um valor default, podendo utilizar um lambda para isso.
Este valor será utilizado sempre que não ouver um valor definido. Caso tentenmos acessar uma chave que não existe, 
essa chave será criada e o valor default será atribuido.

OBS: Lambdas são funções sem nome que podem ou não receber parametros de entrada e retornar valores.
"""

from collections import defaultdict

dicionario = defaultdict(lambda: 0)
print(dicionario)

dicionario['curso'] = "Programação em Python: Essencial"
print(dicionario)
#Resposta: defaultdict(<function <lambda> at 0x7f674ec5fd90>, {})
# defaultdict(<function <lambda> at 0x7f674ec5fd90>, {'curso': 'Programação em Python: Essencial'})

print(dicionario['outro']) #KeyError no dicionario comum, mas aqui não!
print(dicionario)
#Resposta: defaultdict(<function <lambda> at 0x7f5f88dcfd90>, {'curso': 'Programação em Python: Essencial', 'outro': 0})
#Aqui ele adiciona o elemento 'outro' e adiciona um valor  de zero, que atribuimos ao comando defaultdict acima.

