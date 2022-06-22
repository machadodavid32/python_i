"""
Sistemas de arquivos e negaveção.

Para fazer uso de manipulação de arquivos do sistema operacional, precisamos importar e fazer uso do modulo 'os'

os -> operation system



# Fazer o import

import os

# getcwd() - > pega o current work directory - diretório de trabalho corrente
# getcwd - > retorna o path (caminho absoluto)
print(os.getcwd())
# Resposta: /home/david/PycharmProjects/guppe

# Para mudar o diretório, podemos usar o chdir

os.chdir('..')  # dois pontos .. para voltar um diretório
print(os.getcwd())
# Resposta: /home/david/PycharmProjects/guppe
# /home/david/PycharmProjects

os.chdir('..')
print(os.getcwd())
# Resposta:
# /home/david/.virtualenvs/guppe/bin/python /home/david/PycharmProjects/guppe/secao13_sistemas_de_arquivos_navegacao.py
# /home/david/PycharmProjects/guppe
# /home/david/PycharmProjects
# /home/david

os.chdir('..')
print(os.getcwd())
# Resposta: /home/david/.virtualenvs/guppe/bin/python /home/david/PycharmProjects/guppe/secao13_sistemas_de_arquivos_navegacao.py
# /home/david/PycharmProjects/guppe
# /home/david/PycharmProjects
# /home/david
# /home

os.chdir('..')
print(os.getcwd())
# REsposta: /home/david/.virtualenvs/guppe/bin/python /home/david/PycharmProjects/guppe/secao13_sistemas_de_arquivos_navegacao.py
# /home/david/PycharmProjects/guppe
# /home/david/PycharmProjects
# /home/david
# /home
# /  -> Aqui é a raiz. Não vai mais do que isso.



import os

# Podemos chegar se um diretório é absoluto ou relativo
print(os.path.isabs('/home/david/'))
# Resposta: True  -> Pois sim, é absoluto.


import os

# Podemos identificar o sistema operacional com o os
print(os.name)
# Resposta: posix -> (linux e mac) No caso do windows, a resposta seria 'nt'


# Podemos ter mais detalhes do sistema operacional

print(os.uname())
# Resposta:
# posix.uname_result(sysname='Linux', nodename='david-550XCJ-550XCR', release='5.13.0-30-generic', version='#33~20.04.1-Ubuntu SMP Mon Feb 7 14:25:10 UTC 2022', machine='x86_64')



import sys
print(sys.platform)  # Aqui mostra o sistema operacional
# Resposta: linux



import os

print(os.getcwd())
# Resposta: /home/david/PycharmProjects/guppe
res = os.path.join(os.getcwd(), 'geek')
os.chdir(res)
print(os.getcwd())
# REsposta: /home/david/PycharmProjects/guppe
# /home/david/PycharmProjects/guppe/geek

# Obs: Veja que o os.path.join() recebe dois parâmetros, sendo o primeiro o diretório atua e o segundo ...
# ... e o segundo o diretório que será adicionado ao atual.



import os

# podemos listar os diretórios e arquivos com listdir()

print(os.listdir())
# Resposta: /home/david/.virtualenvs/guppe/bin/python /home/david/PycharmProjects/guppe/secao13_sistemas_de_arquivos_navegacao.py
# ['mais.txt', 'secao13_modo_abertura_arquivo.py', 'exerc_secao08_funcao.py', 'teste.py', 'secao08_funcoes_Docstrings.py', 'geek', 'novo.txt', 'secao12_modulo_random.py', 'secao10_Sorted.py', '.idea', 'interface.py', 'secao09_listas_aninhadas.py', 'secao12_pacotes.py', 'secao07_colecoes_mapas.py', 'secao13_sistemas_de_arquivos_navegacao.py', 'secao11_Erros_Comuns.py', 'secao07_tuplas.py', 'outro.txt', 'secao08_Funcoes_parametro_padrao.py', 'secao07_colecoes_listas.py', 'secao06_loop_while.py', 'teste_doc.pdf', 'testes.py', 'secao07_m.collections_ordereddict.py', 'secao09_set_comprehension.py', '__pycache__', 'secao10_filter.py', 'secao09_list_comprehension_p2.py', 'estruturas_logicas_and_or_not_is.py', 'texto.txt', 'secao06_exercicios.py', 'exerc_secao07_listas.py', 'secao07_.=m.collections_Deque.py', 'secao10_zip.py', 'secao07_colecoes_dicionarios.py', 'secao13_escrever_em_arquivos.py', 'secao11_debugando_codigo_PDB.py', 'secao13_bloco_with.py', 'Geek', 'secao06_loop.py', 'secao10_min_max.py', 'condicionais_if_else_elif.py', 'revisao_secao07.py', 'secao07_m.collections_NamedTupla.py', 'secao08_funcoes_parametros.py', 'secao09_dictionary_Comprehension.py', 'secao12_modulos_customizados.py', 'secao10_utilizando_lambdas.py', 'secao_11_levantando_erros_raise.py', 'secao12_modulos_built-in.py', 'questão4.py', 'questão3.py', 'secao10_map.py', 'secao12_dunderMain_dunderName.py', 'tipo_none.py', 'secao08_funcoes_com_retorno.py', 'secao10_generators.py', 'university.txt', 'secao07_m.collections_counter.py', 'segundo.py', 'secao10_len_abs_sum_round.py', 'secao06_loop_break.py', 'secao07_colecoes_conjuntos.py', 'secao09_list_comprehension.py', 'exerc_secao08_funcoes.py', 'secao08_funcao.py', 'interface3.py', 'exerc_secao07_tuplas.py', 'frutas.txt', 'secao12_instalando_utilizando_mod_externos.py', 'interface2.py', 'secao08_funcoes_*args.py', 'secao13_leitura_de_arquivos.py', 'secao10_reversed.py', 'secao13_stringIO.py', 'secao11_try_except_else_finally.py', 'Treinamento.py', 'secao10_any_e_all.py', 'escopo_de_variaveis.py', 'secao06_range.py', 'secao13_Seek_Cursors.py', 'primeiro.py', 'secao08_funcoes_*kwargs.py', 'secao10_reduce.py', 'secao07_m.collections_DefaultDict.py', 'Exer_Secao_5.py', 'secao11_bloco_try_except.py']

# Acima, dentro do diretorio onde o arquivo foi executado tem todos esses arquivos

# Abaixo, da pra contar quantos arquivos tem

print(len(os.listdir()))
# Resposta: 87

print(os.listdir('/etc'))  # etc é um equivalente ao que é o c: do windows
# Resposta: ['java-11-openjdk', 'bluetooth', 'runit', 'ssh', 'passwd-', 'console-setup', 'update-manager', 'debconf.conf', 'sudoers.d', 'xdg', 'acpi', 'machine......

print(len(os.listdir('/etc')))
# Resposta: 239

"""

import os

# podemos listar os arquivos e diretórios com mais detalhes com scandir()

print(os.scandir('/etc'))
# Resposta: <posix.ScandirIterator object at 0x7f9ea3a80340>


