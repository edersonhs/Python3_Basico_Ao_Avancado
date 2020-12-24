from classes import *

"""
Assosiação - Usa  |  Agregação - Tem  |  Composição - É dono  |  Herança = Um objeto É outro objeto
"""

c1 = Cliente('Luiz', 45)
c1.falar()   # Cliente falando...
c1.comprar()   # Cliente comprando..
# c1.estudar()   # O MÉTODO NÃO EXISTE EM CLIENTE
# print(c1.nome)   # Luiz

a1 = Aluno('Maria', 54)
a1.falar()   # Aluno falando...
a1.estudar()  # Aluno estudando...  
# a1.comprar()   # # O MÉTODO NÃO EXISTE EM ALUNO
# print(a1.nome)   # Maria

"""
p1 = Pessoa('João', 43)
print(p1.nome)
p1.falar()
"""
