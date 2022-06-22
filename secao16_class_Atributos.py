"""
POO - Atributos
Atributos representam as características dos objetos. Ou seja, pelos atributos conseguimos representar
computacionalmente os estados do objeto.

Em Python dividimos os atributos em 3 grupos:
    Atributos de instância:
    Atributos de Classe:
    Atributos de Dinâmicos

# Atributos de instância são declarados dentro do metodo construtor
OBS: Método construtor é um método especial utilizado para construção de um objeto.


# OBS: Lmebre-se que isso é apenas uma convenção, ou seja, a linguagem Python não vai imoedir....
# ... que façamos acesso aos atributos sinalizados como privados fora da classe.


# Abaixo é resultado do codigo da criação de classes. Coloquei aqui para não confundir
# Exemplo:


user = Acesso('user@gmail.com', '123456')

# print(user.email)
# Resposta: user@gmail.com

# print(user.__senha)
# Resposta: AttributeError: 'Acesso' object has no attribute '__senha'
# print(dir(user))
# print(user._Acesso__senha) # Aqui teremos acesso, porém, não é correto. Trata-se de uma manobra para acesso a senha..
# ... caso haja necessidade. O nome disso é o Name Mangling

# user.mostra_senha()  # Esses dois foram criados acima
# user.mostra_email()


# Atributos de instância - Significa que, ao criarmos instâncias/objetos de uma classe, todas as intâncias ...
# ...terão estes atributos.

user1 = Acesso('user1@gmail.com', '14564')  # Aqui é um objeto criado da clasee, igual em baixo user2
user2 = Acesso('user2@gmail.com', '15747')

user1.mostra_email()
user2.mostra_email()



# Classes com atributos de instância públicos.


class Lampada:

    def __init__(self, tensao, cor):  # Aqui é o método construtor. Atributos são tensao, ligada e cor
        self.tensao = tensao
        self.cor = cor
        self.ligada = False


class ContaCorrente:

    def __init__(self, numero, limite, saldo):
        self.numero = numero
        self.limite = limite
        self.saldo = saldo


class Produto:

    def __init__(self, nome, descricao, valor):
        self.nome = nome
        self.descricao = descricao
        self.valor = valor


class Usuario:

    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha

# Obs: O self é o objeto que está executando o método. self = o objeto Usuario no atributo nome recebe nome, ...
# o objeto Usuario no atributo email recebe email e por ai vai


# Atributos publicos e atributos privados,
# Em Python, por convenção, ficou estabelecido que, todo atributo de uma classe é publico. Ou seja, pode ser....
# ...acessado em todo o projeto.
# Caso queiramos demonstrar que determinado atributo deva ser tratado como privado, ou seja, que deve ser acessado...
# ...ou utilizado somente dentro da propria classe onde esta declarado, utiliza-se o __ duplo underscore no inicio...
# ..do nome. Isso é conhecido também como Name Mangling.


# Class com atributos publicos e privados abaixo:


class Acesso:

    def __init__(self, email, senha):
        self.email = email
        self.__senha = senha

    def mostra_senha(self):  # Feito para mostrar a senha
        print(self.__senha)

    def mostra_email(self):  # feito para mostrar email
        print(self.email)


# Atributos de classe

# p1 = Produto('Playstation', 'Videogame', 2300)
# p2 = Produto('Xbox', 'Videogame', 2000)

# Atributos de classe são atributos que declaramos diretamente na classe, ou seja, fora do construtor.
# Geralmente, ja iniciamos um valor e este valor é compartilhado entre todas as intâncias de classe. Assim, ao invés...
# ...de cada instância de classe ter seus proprios valores, como é o caso dos atributos de instância, com os ...
# ... atributos de classe todas as instâncias terão o mesmo valor para este atributo.

# Refatorando a classe Produto

# classe antiga que será refatorada
# class Produto:

#    def __init__(self, nome, descricao, valor):
#        self.nome = nome
#        self.descricao = descricao
#        self.valor = valor


class Produto:

    # Atributo de classe
    imposto = 1.05  # 05 imposto
    contator = 0

    def __init__ (self, nome, descricao, valor):
        self.id = Produto.contator + 1
        self.nome = nome
        self.descricao = descricao
        self.valor = (valor * Produto.imposto)
        Produto.contator = self.id


p1 = Produto('Playstation', 'Videogame', 2300)
p2 = Produto('Xbox', 'Videogame', 2000)

print(p1.imposto)
print(p2.imposto)
# Resposta:
# 1.05
# 1.05  Repara que aqui a resposta é a mesma, pois o imposto é geral.

print(p1.valor)  # Acesso possivel mas incorreto de um atributo de classe
print(p2.valor)
# Resposta: 2415.0
# 2100.0  # Reparar que aqui os valores já estão calculados com o valor de imposto.

# Obs: Não precisamos criar uma instância de uma classe para fazer acesso a um atributo de classe.

print(Produto.imposto)  # Acesso correto a um atributo de classe

print(f'Produto1, ID {p1.id}')
print(f'Produto2, ID {p2.id}')
# Resposta: Produto1, ID 1
# Produto2, ID 2


"""


class Produto:

    # Atributo de classe
    imposto = 1.05  # 05 imposto
    contator = 0

    def __init__ (self, nome, descricao, valor):
        self.id = Produto.contator + 1
        self.nome = nome
        self.descricao = descricao
        self.valor = (valor * Produto.imposto)
        Produto.contator = self.id


# Atributos dinâmicos -> Um atributo de instância que pode ser criado em tempo de execução.
# obs: O atributo dinâmico será exclusivo da instância que o criou

p1 = Produto('Playstation', 'videogame', 2300)
p2 = Produto('Arroz', 'Mercearia', 5.99)

# Criando um atributo dinâmico em tempo real.
p2.peso = '5kg'  # Note que na classe Produto não existe o atributo peso

print(f'Produto: {p2.nome}, Descrição: {p2.descricao}, Valor {p2.valor}, Peso {p2.peso}')
# resposta: Produto: Arroz, Descrição: Mercearia, Valor 6.2895, Peso 5kg

# print(f'Produto: {p1.nome}, Descrição: {p1.descricao}, Valor {p1.valor}, Peso {p1.peso}')
# Resposta: Aqui vai dar erro pois o objeto produto não tem o atributo 'peso'


# Deletando atributos

print(p1.__dict__)
# Resposta: {'id': 1, 'nome': 'Playstation', 'descricao': 'videogame', 'valor': 2415.0}
print(p2.__dict__)
# Resposta: {'id': 2, 'nome': 'Arroz', 'descricao': 'Mercearia', 'valor': 6.2895, 'peso': '5kg'}

del p2.peso

print(p2.__dict__)
# Resposta: {'id': 2, 'nome': 'Arroz', 'descricao': 'Mercearia', 'valor': 6.2895}  peso deletado

# Da pra apagar com qualquer atributo com o comando 'del'

