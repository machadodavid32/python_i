"""
POO - Objetos -> São instancias da classe. Após o mapeamento do objeto do mundo real para sua representação...
... computacional, devemos podemos criar quantos objetos forem necessários. Podemos pensar nos objetos/instancias...
... de uma classe como variaveis do tipo definido na classe.

"""


class Lampada:
    def __init__(self, cor, tensao, luminisidade):
        self.__cor = cor
        self.__tensao = tensao
        self.__luminosidade = luminisidade
        self.__ligada = False

    def checa_lampada(self):
        return self.__ligada

    def ligar_desligar(self):
        if self.__ligada:
            self.__ligada = False
        else:
            self.__ligada = True


class Cliente:

    def __init__(self, nome, cpf):
        self.__nome = nome
        self.__cpf = cpf

    def diz(self):
        print(f'O cliente {self.__nome} diz oi')


class ContaCorrente:
    contador = 4999

    def __init__(self, limite, saldo, cliente):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        self.__cliente = cliente
        ContaCorrente.contador = self.__numero

    def mostra_cliente(self):
        print(f'O cliente é {self.__cliente._Cliente__nome}')  # reparar que estamos usando uma classe dentro de um...
        # ...método


class Usuario:
    def __init__(self, nome, sobrenome, email, senha):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = senha


lamp1 = Lampada('Branca', 110, 60)  # Isso é uma instância/objeto.
lamp1.ligar_desligar()  # ao acionar este metodo, o resultado é True. Caso acione o mesmo metodo na linha de baixo...,
# ...vai dar False
print(f'A Lampada está ligada? {lamp1.checa_lampada()}')


cc1 = ContaCorrente(5000, 20000, "machado")

user1 = Usuario('David', 'Machado', 'david@gmail.com', '13456')


cli1 = Cliente('David', '123.4546.789-85')
cc = ContaCorrente(5000, 10000, cli1)

cc.mostra_cliente()

# Quando criamos uma classe, criamos um tipo de dado, como int ou float. Neste caso, podemos utilizar da melhor...
# ...maneira possivel, inclusive dentro de outras classes, dentro de variaveis, etc.



