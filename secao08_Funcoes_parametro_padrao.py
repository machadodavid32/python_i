"""
Funções com parametros padrão (Default Parameters)

Funções onde a passagem de parâmetros seja opcional

#Eexmplo de função onde a passagem de parametro é opcional

print('geek')
print()


#Exemplo de função onde a passagem de parametro é obrigatoria

def quadrado(numero):
    return numero ** 2
print(quadrado(3))
print(quadrado()) # TYPE ERROR Aqui vai dar erro pois o parametro é obrigatorio


def exponencial(numero, potencia):
    return numero ** potencia

print(exponencial(2, 3)) # = 2 * 2 * 2
print(exponencial(3, 2)) # = 3 * 3
#Reposta:
# 8
# 9


def exponencial(numero, potencia=2):  #ao colocar um valor no parametro 'potencia'....
    return numero ** potencia

print(exponencial(3)) #...colocar outro valor aqui se tornar opcional. Se colocar um segundo valor aqui, o valor 2 será substituito
print(exponencial(3, 5))
#Resposta:
# 9
#243



#Em funções Python, os parâmetros com valores default (padrão) DEVEM estar sempre ao final da declaração

#ERRO!
def teste(num=2, potencia)
    return num ** potencia
print(teste(6))
#REsposta: ERRO


#Abaixo, modo correto
def teste(potencia, num=2):
    return num ** potencia
print(teste(6))
#Resposta: 64



#Outros exemplos:

def soma(num1, num2):
    return num1 + num2

print(soma(4, 3))
print(soma(4))  #TYpe error
print(soma())  #Type error
#Para corrigir o erro, é só adicionar um valor para os parametros num1 e num2. num1=2, num2=545




#Exemplo mais complexo

def mostra_informacao(nome='geek', instrutor=False):
    if nome == 'geek' and instrutor:
        return 'Bem vindo instrutor Geek'
    elif nome == 'geek':
        return 'Eu pensei que voce era o instrutor'
    return f'Olá {nome}'

print(mostra_informacao()) #Aqui informamos valores, portanto, será utilizado os parametros com valores (nome='geek', instrutor=False)
print(mostra_informacao(instrutor=True)) #Aqui será utilizado o valor do primeiro padrão ja definido('geek') e novo valor ao segundo parâmetro (instrutor)
print(mostra_informacao(True)) #Aqui o True não vai funcionar como True, ja que está somente para substituir o pridmeiro parametro
print(mostra_informacao(nome='Stephany'))
#Resposta:
# Eu pensei que voce era o instrutor
# Bem vindo instrutor Geek
# Olá True
# Olá Stephany



#Mas porque utilizar os parametros com valores default?

#Nos permite ser mais flexiveis nas funções
#Evitam erros de parâmetros incorretos
#Nos permite trabalhar com exemplos mais legiveis de codigo


#Quais tipos de dados podemos utilizar para valores defaults para parâmetros? Qualquer tipo de dado, entre eles:
#numeros, strings, floats, booleanos, listas, tuplas, dicionarios, funções e etc.



#Exemplos:
def soma(num1, num2):
    return num1 + num2

def mat(num1, num2, fun=soma):
    return fun(num1, num2)
    return fun(num1, num2)

def subtracao(num1, num2):
    return num1 - num2

print(mat(2, 3)) #soma
print(mat(2, 2, subtracao)) #2 - 2 = 0(subtração)


#Escopo - Evitar problemas e confusões

#Variaveis globais

#Variaveis locais

instrutor = 'geek' #Variavel global > Aqui está fora

def diz_oi():
    instrutor = 'Python' #Aqui a variável se torna local e se sobrepoe a variavel global.
    return f'oi {instrutor}'  #Aqui está dentro
print(diz_oi())

#Resposta: oi Python

#OBS:Se tivermos uma variavel local com o mesmo nome de uma variavel global, a local terá preferência.



def diz_oi():
    prof = 'geek' #variavel local
    return f'ola {prof}'

print(diz_oi())
print(prof) #Aqui da errp pois trata-se de uma variavel local. Se fosse global funcionaría
#Resposta ola geek
#nameError



#Atenção com variáveis globais (Se puder evitar, evite)

total = 0

def incrementa():
    total = total +1 #Aqui é um erro pois a variável local total não foi inicializada(localmente) e foi colocada para ser processada.
    return total

print(incremental())
#REsposta: Erro.




#Abaixo, vamos refatorar o codigo acima com o comando 'global'

total = 0

def incrementa():
    global total #Avisamos que queremos utilizar a variavel global
    total= total + 1
    return total

print(incrementa())
print(incrementa())
print(incrementa())
#REsposta 1
#REsposta 2
#REsposta 2
#Ao colocar mais print(incrementa()) ele vai incrementando + 1




# Podemos ter funções que são declaradas dentro de funções e também tem uma forma especial de escopo de variavel

def fora():
    contador = 0

    def dentro():
        nonlocal contador #Comando nonlocal faz valor uma variavel que, neste caso, não é global nem local, mas sim da função acima desta função
        contador = contador + 1
        return contador
    return dentro()

print(fora())

#REsposta: 1

"""

