"""
POO - Polimorfismo

Poli - muitos, muitas
Morfis -> Formas

Quando a gente reimplementa um método presente na classe pai em classes filhas, estamos realizando ...
.. uma sobrescrita de método (Overriding)

O overriding é a melhor representação do polimorfismo

"""


class Animal(object):

    def __init__(self, nome):
        self.__nome = nome

    def falar(self):
        raise NotImplementedError('A classe filha precisa implementar este método')

    def comer(self):
        print(f'{self.__nome} está comendo...')


class Cachorro(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f'{self._Animal__nome} fala au au')


class Gato(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f'{self._Animal__nome} fala miau')


class Rato(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f'{self._Animal__nome} fala algo ...')


# Testes

felix = Gato('Felix')
felix.comer()
felix.falar()

pluto = Cachorro('Pluto')
pluto.comer()
pluto.falar()

mickey = Rato('Mickey')
mickey.comer()
mickey.falar()

# Resposta: Felix está comendo...
# Felix fala miau
# Pluto está comendo...
# Pluto fala au au
# Mickey está comendo...
# Mickey fala algo ...
