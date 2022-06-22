"""
Modulos Externos
Uitilizamos o gerenciador de pacotes Python chamado Pip - Python Installer Package

Você pode conhecer todos os pacotes externos oficiais em https://pypi.org

Como fazer para instalar um pacote? vai no terminal e coloque pip install nome_do_pacote

Instalei o pacote chamado 'colorama'. É um pacote que permite impressão de textos coloridos no terminal

from colorama import init, Fore
init()
print(Fore.MAGENTA + 'Geek Univeristy')
# Resposta: Geek Univeristy
print(Fore.BLUE + 'Geek Univeristy')
"""

# Fiz a instalação do pacote para criar pdf -> pip install pydf

import pydf

pdf = pydf.generate_pdf('<h1>David</h1>')
with open('teste_doc.pdf', 'wb') as f:  # Aqui criei um arquivo no direotrio guppe chamado teste_doc.pdf
    f.write(pdf)

