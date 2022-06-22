"""
Decoradores ou decorators -

O que são decorators?
- Decorators são funções
- Decorators envolvem outras funções e aprimoram seus comportamentos
- Decorators também são exemplos de Higher Order Functions
- Decorators sem sintaxe propria, usando @ (Syntact Sugar / Açucar sintático)




# Decorators como funções

# Sintax não recomendada - (sem açucar sintático)


def seja_educado(funcao):  # função decoradora
    def sendo():
        print('Foi um prazer conhecer você')
        funcao()
        print('Tenha um ótimo dia')
    return sendo()


def saudacao():
    print('Seja bem vindo')


# testando 1


teste = seja_educado(saudacao)  # Aqui estamos decorando a função, ou seja, através de outra temos duas em uma

# REsposta: Foi um prazer conhecer você
# Seja bem vindo
# Tenha um ótimo dia



# Decorators com syntax sugar (recomendado)


def seja_educado_mesmo(funcao):
    def sendo_mesmo():
        print('Foi um prazer conhecer você')
        funcao()
        print('Tenha um excelente dia')
    return sendo_mesmo


@seja_educado_mesmo  # Modo correto de decorar a função
def apresentando():  # Está colocando esta função no lugar da funcao() da sequência acima
    print('Meu nome é David')

# Testando


apresentando()

# REsposta: Foi um prazer conhecer você
# Meu nome é David
# Tenha um excelente dia


@seja_educado_mesmo
def dormir():
    print('Quero dormir')


dormir()

# Resposta: Foi um prazer conhecer você
# Quero dormir
# Tenha um excelente dia

"""



