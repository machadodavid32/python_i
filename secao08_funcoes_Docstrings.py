"""
Documentando funções com Docstrings

OBs: Podemos ter acesso a documentação de uma função em Python utilizando propriedade especial
_doc_

Podemos ainda fazer acesso á documentação com a função help()



#xemplos0
def diz_oi():
    #Uma função simples que retornar a string 'oi'#Isso é uma Docstring

#Ao ir no console e digitar from seca08_funcoes_Docstri ngs import e depois help(diz_oi), a Docstrings que criamos acima aparece

#Resposta:diz_oi()
#   Uma função simples que retornar a string 'oi'
#(END)

"""

def exponencial(numero, potencia=2)
    """
    Função que retorna por padrão o quadrado de 'numero' ou 'numero' á 'potencia' informada 
    :param numero: numero que desejamos gerar o exponencial.
    :param potencia: Potência que queremos gerar o exponencial por padrão é 2
    :return: retorna o exponencial de 'numero' por 'potencia'
    """
    return numero ** potencia


