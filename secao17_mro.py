"""
MRO - Method Resolution Order

class Pinguim(Terrestre, Aquatico):
Eu sou Tux da terra!

class Pinguim(Aquatico, Terrestre):
Eu sou Tux do mar!

Reparar acima que, ao inverter a ordem, ele pegou o método diferente. Esse é o Method Resolution Ordem, ou ordem
de execução dos métodos, quem vai primeiro.


Em Python, a gente pode conferir a ordem de execução dos métodos (MRO) de 3 formas:
   Via propriedade da classe__mro__
   Via método mro()
   Via Help

"""


class Animal:

    def __init__(self, nome):
        self.__nome = nome

    def cumprimentar(self):
        return f'Eu sou {self.__nome}'


class Aquatico(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def nadar(self):
        return f'{self._Animal__nome} está nadando'

    def cumprimentar(self):
        return f'Eu sou {self._Animal__nome} do mar!'


class Terrestre(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def andar(self):
        return f'{self._Animal__nome} está andandp'

    def cumprimentar(self):
        return f'Eu sou {self._Animal__nome} da terra!'


class Pinguim(Aquatico, Terrestre):  # Aqui temos duas heranças, o sistema vai herdar pela ordem, primeira primeiro.

    def __init__(self, nome):
        super().__init__(nome)


tux = Pinguim('Tux')
print(tux.cumprimentar())


"""

"""

