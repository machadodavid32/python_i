"""
POO - Classes
Classes nada mais são, em POO, do que modelos em objetos do mundo real sendo representados computacionalmente.
Imagine que você queira fazer um sisrema.

Sabemos que idade = 22, preço = 223,02 ou nome = 'David. São representados por, respectivamente, int, floar e string
No caso de uma lampada, não existe representatividade. Por isso que criamos uma classe. Conforme abaixo.

Classes podem conter:

Atributos: Representam as características do objeto. Ou seja, pelos atributos conseguimos representar
computacionalmente os estados de um objeto. No caso da lampada, possivelmente, iriamos querer saber se a lampada é
110 ou 220v, se a cor é branca, amarela, vermelha, etc, luminsidade...

Métodos (funções)- Representam o comportamento dos objetos. Ou seja, as ações que este objeto pode realizar no seu
sistema. No caso da lampada, ṕor exemplo, um comportamento comum que muito provavelmente iríamos querer representar
no nosso sistema é o de desligar e ligar a mesma.

OBS: Em Python, para definir uma classe usamos a palavra reservada class.
Utilizamos a palavra 'pass' em python quando temos um bloco de código que ainda não está implementado,

OBS: Quando nomeamos nossas classes em python, utilizamos por convenção um nome com inicial em maiusculo. Se o nome
for composto, iniciamos as palavras em maiúsculo.

OBS: Quando estamos planejando um software e definimos quais classes queremos no sistemas, chamamos esses objetos que
serão mapeados de classes de entidade. Exemplo: lampada ou a conta corrente.
"""


class Lampada:
    pass  # o comando pass serve para não dar erro de identação, quando um bloco de codigo ainda não está implmentado.


lamp = Lampada()
print(type(lamp))
# Resposta: <class '__main__.Lampada'>


class ContaCorrente:  # Não pode traço. Exemplo: Conta_Corrente > Não pode
    pass

