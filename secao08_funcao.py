"""Definindo funções

- Funções são pequenas partes de codigo que realizam tarefas específicas
- pode ou não receber entrada de dados e retornar uma saída de dados
- Muito uteis para executar procedimento similires por repetidas vezes

OBS: Se você escrever uma função que realiza varias tarefas dentro dela, é bom fazer uma verificação
para que a função seja simplificada

Já utilizamos varias funções desde que ja iniciamos este curso:
print()
len()
max()
min()
count()

"""

#Exemplo de utilização de funções

#cores = ['verde', 'amarel', 'azul', 'branco']

#Utilizando uma função integrada (Built-in) do Python print()
#print(cores)

#curso = 'Programação em Python: Essencial'
#print(curso)

#cores.append('roxo')
#print(cores)

# Conceito DRY - Don´t repet yourself - Não repita você mesmo / Não repita seu codigo

#Mas então, como definir função:

"""
Em Python, de forma geral, uma função é:

def nome_da_funcao(parametros_de_entrada):
    bloco_da_funcao
    
Onde: 
nome da função -> SEMPRE com letras minusculas, e se for nome composto, separado por underline (Snake Case):

parametros_de_entrada -> Opcionais, onde tendo mais de um, cada um separado por virgula, podendo ser opcionais ou não.
    
bloco_da_funcao -> também chamado de corpo da função ou implementação, é onde o processamento da função acontece.
Neste bloco, pode ter ou não o retorno da função.

OBS: Para definir uma função utilizamos a palavra reservada 'def', informando ao Python que estamos definindo 
um função. Também abrimos o bloco de codigo com o ja conhecido dois pontos :  que é utilizado em Python para 
definir blocos

"""

#Definindo a primeira função

#Exemplo 1

#definicação
def diz_oi():
    print('oi') #Até aqui o codigo não vai imprimir. Só vai imprimir quando 'chamar a função'

"""
OBS: 
1 - Veja que dentro das nossas funções, podemos utilozar outras funções
2 - Veja que nossa função só executa uma tarefa, ou seja, a unica coisa que ela faz é dizer 'oi'
3 - Veja que esta função não recebe nenhum parametro de entrada
4 - Veja que esta função não retorna nada 
"""

#Utilizando funções

#chamada de execução

diz_oi() #Aqui estamos chamando a função. Agora vai imprimir.
# É necessário abrir e fechar os parenteses () pois toda função tem o parenteses ()

"""
Atenção:
Nunca esqueça de utilizar parenteses numa função

errado: diz_oi
certo: diz_oi()

"""

#Exemplo 2

def cantar_parabens():
    print('Parabéns para você')
    print('Nesta data querida')
    print('Muitas felicidades')
    print('Muitos anos de vida')
    print('Viva o aniversariante!')

cantar_parabens()
#Resposta:
# Parabéns para você
# Nesta data querida
# Muitas felicidades
# Muitos anos de vida
# Viva o aniversariante!

cantar_parabens()
cantar_parabens() #Vai imprimir mais vezes aqui

#Em Python podemos, inclusive, podemos criar variaveis do tipo de uma função e executar esta função através da variável.
# exemplo:
canta = cantar_parabens
canta()

