"""
POO - Herança Multipla

Herança multipla nada mais é a possibilidade de uma classe herdar de multiplas classes, fazendo com que a classe
filha herde todos os atributos e métodos de todas as classes herdadas.

obs: A herança multipla pode ser feita de duas maneiras:
Por multiderivação direta:

Por multiderivação indireta:



# Exemplo 1 - Multiderivação direta


class Base1:
    pass


class Base2:
    pass


class Base3:
    pass


class Multiderivada(Base1, Base2, Base3):
    pass


# Exemplo 2 - Multiderivação indireta

class Base1:
    pass


class Base2(Base1):
    pass


class Base3(Base2):
    pass


class Multiderivada(Base3)


Obs: Não importa se a derivação é direta ou indireta, a classe que realizar a herança, herdará todos os atributos...
.. e métodos das outras classes.

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


class Pinguim(Terrestre, Aquatico):  # Aqui temos duas heranças, o sistema vai herdar pela ordem, primeira primeiro.

    def __init__(self, nome):
        super().__init__(nome)


baleia = Aquatico('Wally')
print(baleia.nadar())
print(baleia.cumprimentar())

tatu = Terrestre('Xim')
print(tatu.andar())
print(tatu.cumprimentar())

tux = Pinguim('Tux')
print(tux.andar())
print(tux.nadar())
print(tux.cumprimentar())

# Resposta: Wally está nadando
# Eu sou Wally do mar!
# Xim está andandp
# Eu sou Xim da terra!
# Tux está andandp
# Tux está nadando
# Eu sou Tux da terra!

# O objeto de instância é:

print(f'Tux é instancia de Pinguim? {isinstance(tux, Pinguim)}')
print(f'Tux é instancia de Aquatico? {isinstance(tux, Aquatico)}')
print(f'Tux é instancia de Terrestre? {isinstance(tux, Terrestre)}')
print(f'Tux é instancia de Animal? {isinstance(tux, Animal)}')
print(f'Tux é instancia de object? {isinstance(tux, object)}')

# Resposta: Tux é instancia de Pinguim? True
# Tux é instancia de Aquatico? True
# Tux é instancia de Terrestre? True
# Tux é instancia de Animal? True
# Tux é instancia de object? True ->>>Obs: Aqui, quando uma classe não herda de ninguém, é object


