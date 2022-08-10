""" Conhecendo o Pickle

A função do Pickle é realizar o seguinte processo:

objeto python -> Binárização

Binárização -> Objeto Python

Este processo é chamado serialização / deserialização

# OBS - O módulo Pickle não é seguro contra dados maliciosos e desta forma não é recomendado trabalhar com arquivos...
... pickle vindo de outras pessoas que você não conheça ou de fontes desconhecidas

# Fazendo a escrita do arquivi pickle

felix = Gato('Felix')
pluto = Cachorro('Pluto')

with open('animais.pickle', 'wb') as arquivo:  # obs: 'wb' w de write e b de binário
    pickle.dump((felix, pluto), arquivo)

    # dump é para receber dois parâmetros, no caso (felix,pluto) e arquivo

import pickle


class Animal:

    def __int__(self, nome):
        self.__nome = nome

    def comer(self):
        print(f'{self.__nome} está comendo...')


class Gato(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def mia(self):
        print(f'{self._Animal__nome} está miando ...')


class Cachorro(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def late(self):
        print(f'{self._Animal__nome} está latindo...')


# Fazendo a escrita do arquivi pickle


felix = 'Félix'
pluto = 'Pluto'

with open('animais.pickle', 'wb') as arquivo:  # obs: 'wb' w de write e b de binário
    pickle.dump((felix, pluto), arquivo)

"""

import pickle


class Animal:

    def __int__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    def comer(self):
        print(f'{self.__nome} está comendo...')


class Gato(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def mia(self):
        print(f'{self.nome} está miando ...')


class Cachorro(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def late(self):
        print(f'{self.nome} está latindo...')


# Leitura em arquivos pickle

with open('animais.pickle', 'rb') as arquivo:  # rb de leitura
    gato, cachorro = pickle.load(arquivo)
    print(f'O gato chama-se {gato.nome}')
    gato.mia()
    print(f'O tipo de gato é {type(gato)}')

    print(f'O cachorro chama-se {cachorro.nome}')
    cachorro.late()
    print(f'O tipo do cachorro é {type(cachorro)}')


