"""
POO - Métodos mágicos
Métodos Mágicos são todos os métodos que utilizam dunder.

dunder init __init__()

dunder -> double underscore

dunder repr ->Representação do objeto




class Livro:

    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __repr__(self):
        return f'{self.titulo} escrito por {self.autor}'


livro1 = Livro('Python Rocks!', 'Geek University', 400)
livro2 = Livro('Inteligência Artificial com Python', 'Geek University', 350)

print(livro1)
# Resposta: <__main__.Livro object at 0x7efcba3a1ff0>   endereço de memoria
# Resposta Após introdudir o __repr__  >  Python Rocks! escrito por Geek University
print(livro2)
# Resposta: <__main__.Livro object at 0x7efcba3a1f00>
# Resposta após introduzir o __repr__  >  Inteligência Artificial com Python escrito por Geek University

"""


class Livro:

    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __str__(self):
        return self.titulo

    def __len__(self):
        return self.paginas

    def __add__(self, outro):
        return f'{self} - {outro}'


livro1 = Livro('Python Rocks!', 'Geek University', 400)
livro2 = Livro('Inteligência Artificial com Python', 'Geek University', 350)

print(livro1)  # Resposta: Python Rocks!
print(livro2)  # Resposta: Inteligência Artificial com Python

print(len(livro1))  # 400
print(len(livro2))  # 350

print(livro1 + livro2)  # Resposta: Python Rocks! - Inteligência Artificial com Python
