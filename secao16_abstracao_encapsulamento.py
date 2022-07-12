"""
POO - Abstração e encapsulamento

O grande objetivo da programação orientada a objeto é encapsular nosso codigo dentro de um grupo logico e hierarquico
utilizando classes.

Abstração - Em POO, é o ato de expor apenas dados relevantes de uma classe, escondendo atributos e métodos privados
do usuário.





class Conta:
    contador = 400

    def __init__(self, titular, saldo, limite):
        self.numero = Conta.contador
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def extrato(self):
        print(f'Saldo de {self.saldo} do titular {self.titular} com limite de {self.limite} ')

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        self.saldo -= valor


# testando

conta1 = Conta('Geek', 150.00, 1500)
print(conta1.titular)
print(conta1.numero)
print(conta1.saldo)
print(conta1.limite)

# Resposta: Geek
# 400
# 150.0
# 1500
# No codigo acima, os dados do cliente estão expostos e também podem ser modificados. Exemplo abaixo:

conta1.numero = 42
conta1.titular = "Xuxa"
conta1.saldo = 999999999999
conta1.limite = 99999999999999999999
print(conta1.__dict__)

# Resposta: {'numero': 42, 'titular': 'Xuxa', 'saldo': 999999999999, 'limite': 99999999999999999999}
# Reparar que consegui ver e modificar os dados. Isso não pode. Então, vamos tornar os dados mais seguros refatorando..
# o codigo acima




class Conta:
    contador = 400

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print(f'Saldo de {self.__saldo} do titular {self.__titular} com limite de {self.__limite} ')

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor


# testando

conta1 = Conta('Geek', 150.00, 1500)
print(conta1.__dict__)
conta1.extrato()

# acima é o codigo considerado seguro. Porém, utilizando o name mangling, podemos ter acesso.

print(conta1._Conta__titular)  # Acesso na safadeza com mangling
# Resposta: Geek

"""


class Conta:
    contador = 400

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print(f'Saldo de {self.__saldo} do titular {self.__titular} com limite de {self.__limite} ')

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
        else:
            print("O valor precisa ser positivo")

    def sacar(self, valor):
        if valor > 0:
            if self.__saldo >= valor:
                self.__saldo -= valor
            else:
                print("Saldo insuficiente")
        else:
            print("O valor deve ser positivo")

    def transferir(self, valor, conta_destino):
        # remover o valor da conta de origem
        self.__saldo -= valor
        # Adicionar este valor na conta destino
        conta_destino.__saldo += valor


# testando


conta1 = Conta('Geek', 150.00, 1500)
print(conta1.__dict__)
conta1.depositar(150)
print(conta1.__dict__)
conta1.sacar(200)
print(conta1.__dict__)


# Resposta: {'_Conta__numero': 400, '_Conta__titular': 'Geek', '_Conta__saldo': 150.0, '_Conta__limite': 1500}
# {'_Conta__numero': 400, '_Conta__titular': 'Geek', '_Conta__saldo': 300.0, '_Conta__limite': 1500}
# Saldo insuficiente
# {'_Conta__numero': 400, '_Conta__titular': 'Geek', '_Conta__saldo': 300.0, '_Conta__limite': 1500}
# Acima reparar que o depositar deu certo. Temos saldo de 300 agora.

conta2 = Conta("felicity", 300, 2000)
conta2.extrato()
conta2.transferir(100, conta1)
conta1.extrato()
conta2.extrato()


# Resposta: {'_Conta__numero': 400, '_Conta__titular': 'Geek', '_Conta__saldo': 150.0, '_Conta__limite': 1500}
# {'_Conta__numero': 400, '_Conta__titular': 'Geek', '_Conta__saldo': 300.0, '_Conta__limite': 1500}
# {'_Conta__numero': 400, '_Conta__titular': 'Geek', '_Conta__saldo': 100.0, '_Conta__limite': 1500}
# Saldo de 300 do titular felicity com limite de 2000
# Saldo de 200.0 do titular Geek com limite de 1500
# Saldo de 200 do titular felicity com limite de 2000

