"""POO - Herança (Inheritance)
A ideia de herança é de reaproveitar código, mas não só isso, também extender nossas classes.

Obs: Com a herança, a partir de uma classe existente, nós extendemos outra classe que passa a herdar ..
.. atributos e métodos da classe herdada.

Cliente
    - nome
    - sobrenome
    - cpf
    - renda

Funcionárip
    - nome
    - sobrenome
    - cpf
    - matrícula





class Cliente:

    def __init__(self, nome, sobrenome, cpf, renda):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf
        self.__renda = renda

    def nome_completo(self):
        return f"{self.__nome} {self.__sobrenome}"


class Funcionario:

    def __init__(self, nome, sobrenome, cpf, matricula):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf
        self.__matricula = matricula

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


cliente1 = Cliente("Angelina", "Jolie", "3215485", 50000)
funcionario1 = Funcionario("Felicyty", "Jones", "54645879788", 52000)

print(cliente1.nome_completo())
print(funcionario1.nome_completo())



# O codigo acima funcionou perfeitamente. Abaixo, vamos usar a HERANÇA


class Pessoa:

    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nome_completo(self):
        return f"{self.__nome} {self.__sobrenome}"


class Cliente(Pessoa):

    def __init__(self, nome, sobrenome, cpf, renda):
        super().__init__(nome, sobrenome, cpf)
        self.__renda = renda


class Funcionario(Pessoa):

    def __init__(self, nome, sobrenome, cpf, matricula):
        super().__init__(nome, sobrenome, cpf)
        self.__matricula = matricula


cliente1 = Cliente("Angelina", "Jolie", "3215485", 50000)
funcionario1 = Funcionario("Felicyty", "Jones", "54645879788", 52000)

print(cliente1.nome_completo())
print(funcionario1.nome_completo())

# Obs: Quando uma classe herda de outra classe ela herda todos os atributos da classe herdada.

# Obs: Quando uma classe herda de outra classe, a classe herdada é conhecida por (neste caso, a classe Pessoa),..
# .. Super Classe, Classe Mãe, Classe Pai, Classe Base, Classe Genérica

# Quando uma classe herda de outra classe, este classe é chamada de (no caso, as classes cliente e funcionário) ...
# .. Sub Classe, Classe Filha, Classe específica.

print(cliente1.__dict__)
print(funcionario1.__dict__)
# Resposta: {'_Pessoa__nome': 'Angelina', '_Pessoa__sobrenome': 'Jolie', '_Pessoa__cpf': '3215485', '_Cliente__renda': 50000}
# {'_Pessoa__nome': 'Felicyty', '_Pessoa__sobrenome': 'Jones', '_Pessoa__cpf': '54645879788', '_Funcionario__matricula': 52000}

"""


class Pessoa:

    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nome_completo(self):
        return f"{self.__nome} {self.__sobrenome}"


class Cliente(Pessoa):

    def __init__(self, nome, sobrenome, cpf, renda):
        super().__init__(nome, sobrenome, cpf)
        self.__renda = renda


class Funcionario(Pessoa):

    def __init__(self, nome, sobrenome, cpf, matricula):
        super().__init__(nome, sobrenome, cpf)
        self.__matricula = matricula

    def nome_completo(self):
        return f'Funcionário: {self.__matricula} Nome: {self._Pessoa__nome}'  #Aqui, ex. de sobescrita


cliente1 = Cliente("Angelina", "Jolie", "3215485", 50000)
funcionario1 = Funcionario("Felicyty", "Jones", "54645879788", 52000)

# Sobescrita de métodos (Overriding)
# Sobescrita de método ocorre quando reescrevemos um método presente na super classe em classes filhas

print(cliente1.nome_completo())
print(funcionario1.nome_completo())

# Resposta: Angelina Jolie
# Funcionário: 52000 Nome: Felicyty

