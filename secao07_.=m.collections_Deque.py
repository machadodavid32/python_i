"""
Módulo Colletions - Deque

Podemos dizer que deque é uma lista de alta performance.


"""

#Importar

from collections import deque

#criando deques

deq = deque('geek')
print(deq)
# Resposta: deque(['g', 'e', 'e', 'k'])   > Criou uma lista, separando cada uma das letras

#Adicionando elementos no deque

deq.append('y')
print(deq)
#resposta: deque(['g', 'e', 'e', 'k', 'y']) > Adicionou 'y' no final

deq.appendleft('k') #adiciona no começo da lista
print(deq)
#resposta: deque(['k', 'g', 'e', 'e', 'k', 'y'])


#remover elementos

print(deq.pop()) #remove e retorna o ultimo elemento
print(deq)
#resposta:
# y          >     Retornou 'y'
# deque(['k', 'g', 'e', 'e', 'k'])  >>Sem o 'y'


print(deq.popleft())
print(deq)
#resposta k    >>Retornou 'k', o primeiro da lista
# deque(['g', 'e', 'e', 'k'])

