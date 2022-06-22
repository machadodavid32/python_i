"""
Dunder Name e Dunder Main

Dunder -> doble under (dois underlines)

Dunder Name -> __name__

Dunder Main  -> __main__

Em python, são utilizados dunder para criar funções, atributos, propriedades e etc utilizando  double under
para não gerar conflito com o nome desses elementos na programação.

# Na linguagem C, temos um programa na seguinte forma:
int main(){

    return 0;
}

# Na linguagem java temos um programa da seguinte forma:

public static void main(String[] args) {}

# main significa principal


# Em Python, se executarmos um módulo diretamente na linha de comando, internamente o Python atribuirá a
variável __name__ o valor __main__ indicando que este módulo é o módulo da execução principal.

"""

from secao08_funcoes_parametros import soma_impares
print(soma_impares([1, 2, 4, 5, 7, 9]))
# Resposta: 22

import primeiro
import segundo
# Se colocar o programa para rodar apenas usando o import dos modulos, ele roda neste caso.
# REsposta: primeiro.py foi importado
# segundo.py foi importado

# Existem alguns programas feitos para serem executados diretamente, como o exemplo acima. Mas a maioria não.
# Quem faz essa verificação, de quem pode ser executado diretamente, é o __name__ e o __main__
# Se o programa for executado diretamente, ele se chama  __main__
# Se o programa for importado, ele é chamado pelo proprio nome

