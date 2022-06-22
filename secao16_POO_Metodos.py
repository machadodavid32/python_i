"""
POO - Métodos
Representam os comportamentos do objeto, ou seja, as ações que este objeto pode realizar no seu sistema.

Em Python, dividimos o metodos em dois grupos: Métodos de instância e métodos de classe

O método dunder init é um metodo especial chamado construtor. Sua função é construir um objeto a partir da classe.

obs: Todo elemento em Python que inicia e finaliza com duplo underline é chamado de dunder (double underline)

Os métodos dunder em Python são chamados métodos mágicos.

Atenção - Por mais que possamos criar nossas próprias funções utilizando dunder, não é aconselhavel. O Python ...
... possui vários métodos com essa nomenclatura e pode ser que mudemos o comportamento dessas funções mágicas ...
... interna da linguagem. Então, evite ao maximo. De preferência nunca faça.


Obs: Métodos são escritos em letras minúsculas. Caso seja nome composto, os nomes serão separados por underline.

Os métodos de instancia são os que ficam abaixo da classe, ou seja,começam a partir do def__init__ ...


Obs: Métodos de classe são conhecidos como métodos estáticos em outras linguagens

# Métodos de instancia

#####
class Lampada:
    
    def __init__(self, cor, tensao, luminosidade):
        self.__cor = cor
        self.__tensao = tensao
        self.__luminosidade = luminosidade
        self.__ligada = False


class ContaCorrente:

    contador = 4999

    def __init__(self, limite, saldo):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        ContaCorrente.contador = self.__numero


class Produto:

    contador = 0

    def __init__(self, nome, descricao, valor):
        self.__id = Produto.contador + 1
        self.__nome = nome
        self.__descricao = descricao
        self.__valor = valor
        Produto.contador = self.__id

    def desconto(self, porcentagem):
        #Retorna o valor do produto com desconto#
        return (self.__valor * (100 - porcentagem)) / 100


from passlib.hash import pbkdf2_sha256 as cryp


class Usuario:
    def __init__(self, nome, sobrenome, email, senha):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = cryp.hash(senha, rounds=200000, salt_size=16)

    def nome_completo(self):  # Isso é chamado de método.
        return f'{self.__nome} {self.__sobrenome}'

    def checa_senha(self, senha):
        if cryp.verify(senha, self.__senha):
            return True
        return False


nome = input("Informe o nome: ")
sobrenome = input("Informe o sobrenome: ")
email = input("Informe o email: ")
senha = input("Informe a senha: ")
confirma_senha = input("Confirme a sua senha: ")

if senha == confirma_senha:
    user = Usuario(nome, sobrenome, email, senha)
else:
    print('Senha não confere')
    exit(1)

print('Usuario criado com sucessso!')

senha = input("Informe a sua senha: ")

if user.checa_senha(senha):
    print('Acesso permitido')
else:
    print('Acesso negado')

print(f'Senha User Criptografada: {user._Usuario__senha}') # Método errado
# p1 = Produto('Playstation 4', 'VideoGame', 2300)  # Aqui criamos um produto
# print(p1.desconto(20))  # Aqui aplicamos o desconto
# Resposta: 1840

# user1 = Usuario('Angelina', 'Jolie', 'angelina@gmail.com', '12345')
# user2 = Usuario('Felicity', 'Jones', 'jones@gmail.com', '78912')

# print(user1.nome_completo())  # Aqui se chama instancia
# print(user2.nome_completo())  # Importante notar que, neste comando, o 'user1 ou user2' é o chamado self

# Resposta: Angelina Jolie
# Felicity Jones


# REsposta da senha
# Informe o nome: david
# Informe o sobrenome: machado
# Informe o email: machado@gmail.com
# Informe a senha: 102030
# Confirme a sua senha: 554848
# Senha não confere



# Métodos de classe


class Lampada:

    def __init__(self, cor, tensao, luminosidade):
        self.__cor = cor
        self.__tensao = tensao
        self.__luminosidade = luminosidade
        self.__ligada = False


class ContaCorrente:
    contador = 4999

    def __init__(self, limite, saldo):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        ContaCorrente.contador = self.__numero


class Produto:
    contador = 0

    def __init__(self, nome, descricao, valor):
        self.__id = Produto.contador + 1
        self.__nome = nome
        self.__descricao = descricao
        self.__valor = valor
        Produto.contador = self.__id

    def desconto(self, porcentagem):
        # Retorna o valor do produto com desconto
        return (self.__valor * (100 - porcentagem)) / 100


from passlib.hash import pbkdf2_sha256 as cryp


class Usuario:

    contador = 0

    @classmethod
    def conta_usuarios(cls):  # cls é a classe. Neste caso, a classe Usuário
        print(f'Temo(s) {cls.contador} usuarios no sistema')

    def __init__(self, nome, sobrenome, email, senha):
        self.__id = Usuario.contador + 1
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = cryp.hash(senha, rounds=200000, salt_size=16)
        Usuario.contador = self.__id

    def nome_completo(self):  # Isso é chamado de método.
        return f'{self.__nome} {self.__sobrenome}'

    def checa_senha(self, senha):
        if cryp.verify(senha, self.__senha):
            return True
        return False


user = Usuario('Felicy', 'Jones', 'felicity@gmail.com', '123456')

Usuario.conta_usuarios()  # Forma correta
user.conta_usuarios()  # Possivel, mas é incorreto

# Resposta:
#Temo(s) 1 usuarios no sistema
#Temo(s) 1 usuarios no sistema



##



class Lampada:

    def __init__(self, cor, tensao, luminosidade):
        self.__cor = cor
        self.__tensao = tensao
        self.__luminosidade = luminosidade
        self.__ligada = False


class ContaCorrente:
    contador = 4999

    def __init__(self, limite, saldo):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        ContaCorrente.contador = self.__numero


class Produto:
    contador = 0

    def __init__(self, nome, descricao, valor):
        self.__id = Produto.contador + 1
        self.__nome = nome
        self.__descricao = descricao
        self.__valor = valor
        Produto.contador = self.__id

    def desconto(self, porcentagem):
        # Retorna o valor do produto com desconto
        return (self.__valor * (100 - porcentagem)) / 100


from passlib.hash import pbkdf2_sha256 as cryp


class Usuario:

    contador = 0

    @classmethod
    def conta_usuarios(cls):  # cls é a classe. Neste caso, a classe Usuário
        print(f'Temo(s) {cls.contador} usuarios no sistema')

    def __init__(self, nome, sobrenome, email, senha):
        self.__id = Usuario.contador + 1
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = cryp.hash(senha, rounds=200000, salt_size=16)
        Usuario.contador = self.__id
        print(f'Usúario criado {self.__gera_usuario()}')

    def nome_completo(self):  # Isso é chamado de método.
        return f'{self.__nome} {self.__sobrenome}'

    def checa_senha(self, senha):
        if cryp.verify(senha, self.__senha):
            return True
        return False
# Os métodos acima são métodos publicos. Mas podemos criar métodos privados

    def __gera_usuario(self):
        return self.__email.split('@')[0]


user = Usuario('felici', 'jone', 'feli@gmail.com', '123456')
# Resposta: Usúario criado feli  Ou seja, temos acesso diretamente a um método dentro da estância.

# print(user.Usuario__gera_usuario())  # Acesso errado, pois está fora da classe. Vai dar erro

"""
# Métodos estáticos

from passlib.hash import pbkdf2_sha256 as cryp


class Usuario:

    contador = 0

    @classmethod
    def conta_usuarios(cls):  # cls é a classe. Neste caso, a classe Usuário
        print(f'Temo(s) {cls.contador} usuarios no sistema')

    def __init__(self, nome, sobrenome, email, senha):
        self.__id = Usuario.contador + 1
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = cryp.hash(senha, rounds=200000, salt_size=16)
        Usuario.contador = self.__id
        print(f'Usúario criado {self.__gera_usuario()}')

    def nome_completo(self):  # Isso é chamado de método.
        return f'{self.__nome} {self.__sobrenome}'

    def checa_senha(self, senha):
        if cryp.verify(senha, self.__senha):
            return True
        return False
# Os métodos acima são métodos publicos. Mas podemos criar métodos privados

    def __gera_usuario(self):
        return self.__email.split('@')[0]
