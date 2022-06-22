"""
Pacotes

Módulos -> é apenas um arquivo Python que pode ter diversas funções para utilizarmos
Pacotes -> É um diretório contendo uma coleção de módulos. Ex nosso diretório guppe

Nas versões 2.x, um pacote python deveria conter dentro dele um arquivo chamado __init__.py
Nas versões 3.x, não é mais obrigatório a utilização deste arquivo, mas normalmente ainda é utilizado para
manter a compatibilidade.
Vamos agora clicar em guppe e criar um python package e trabalhar lá

Nós criamos um pacote com submodulos e modulos e abaixo vamos testar

from geek import geek1, geek2
from geek.university import geek3, geek4  # Aqui estamos acessando o submodulo

print(geek1.pi)
print(geek1.funcao(4, 6))
# Reposta: 3.1456  -> Imprimiu o pi
# 10 -> imprimiu a função 4 + 6 = 10

print(geek2.curso)  # Aqui estamos falando, do modulo geek2 use a variável curso
print(geek2.funcao2())  # Aqui estamos falando, do modulo geek2, use a funcao2
# Resposta: Programação em Python: Essencial
# Programação em Python: Essencial


print(geek3.funcao3())
print(geek4.funcao4())
# Resposta: Geek
# University
"""

from geek.geek1 import funcao  # Aqui estamos importando apensas a funcao criada dentro do modulo geek1
from geek.university.geek4 import funcao4  # Aqui estamos importanto a funcao4 crida dentro do submodulo univerisity


print(funcao(9, 6))
print(funcao4())
# Resposta: 15
# University


