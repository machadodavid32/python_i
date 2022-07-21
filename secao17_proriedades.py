"""
POO - Propriedades - Properties

Em linguagens de programação como o Java, ao declararmos atributos privados nas classes, costumamos a criar
métodos públicos para manipulação desses atributos. Estes métodos são conhecidos por getters e setters, onde ..
.. os getters retornam o valor do atributo e os setters alteram o valor do mesmo.



class Conta:

    contador = 0

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador + 1
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    def extrato(self):
        return f'Saldo de {self.__saldo} do cliente {self.__titular}'

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor

    def transferir(self, valor, destino):
        self.__saldo -= valor
        destino.__saldo += valor

    def get_numero(self):
        return self.__numero

    def get_titular(self):
        return self.__titular

    def set_tituar(self, titular):
        self.__titular = titular

    def get_saldo(self):
        return self.__saldo

    def get_limite(self):
        return self.__limite

    def set_limite(self, limite):
        self.__limite = limite


conta1 = Conta('Felicity', 3000, 5000)
conta2 = Conta('Angelina', 2000, 4000)

print(conta1.extrato())
print(conta2.extrato())

soma = conta1.get_saldo() + conta2.get_saldo()
print(f'A soma dos saldos da conta é {soma}')

# Resposta: Saldo de 3000 do cliente Felicity
# Saldo de 2000 do cliente Angelina
# A soma dos saldos da conta é 5000

print(conta1.__dict__)
conta1.set_limite(999999)
print(conta1.__dict__)

# Resposta: {'_Conta__numero': 1, '_Conta__titular': 'Felicity', '_Conta__saldo': 3000, '_Conta__limite': 5000}
# {'_Conta__numero': 1, '_Conta__titular': 'Felicity', '_Conta__saldo': 3000, '_Conta__limite': 999999}

# Acima, o limte que era 5000, aumentamos para 999999

"""


class Conta:

    contador = 0

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador + 1
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    @property
    def numero(self):
        return self.__numero

    @property
    def titular(self):
        return self.__titular

    @property
    def saldo(self):
        return self.__saldo

    @property
    def limite(self):
        return self.__limite

    @limite.setter   # Este serve para adicionar um novo limite na conta
    def limite(self, novo_limite):
        self.__limite = novo_limite

    def extrato(self):
        return f'Saldo de {self.__saldo} do cliente {self.__titular}'

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor

    def transferir(self, valor, destino):
        self.__saldo -= valor
        destino.__saldo += valor


conta1 = Conta('Felicity', 3000, 5000)
conta2 = Conta('Angelina', 2000, 4000)

print(conta1.extrato())
print(conta2.extrato())

soma = conta1.saldo + conta2.saldo  # Reparar aqui que o 'saldo' agora é uma propriedade
print(f'A soma dos saldos da conta é {soma}')

# Resposta: Saldo de 3000 do cliente Felicity
# Saldo de 2000 do cliente Angelina
# A soma dos saldos da conta é 5000

print(conta1.__dict__)
conta1.limite = 76543
print(conta1.__dict__)
print(conta1.limite)

# Resposta: {'_Conta__numero': 1, '_Conta__titular': 'Felicity', '_Conta__saldo': 3000, '_Conta__limite': 5000}
# {'_Conta__numero': 1, '_Conta__titular': 'Felicity', '_Conta__saldo': 3000, '_Conta__limite': 76543}
# 76543




