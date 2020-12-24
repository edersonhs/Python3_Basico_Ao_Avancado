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

print()

c2 = ClienteVIP('Rose', 25, 'Miranda')
c2.falar()
"""
Quando um método é chamado o interpretador do python procura por ele primeiramente na classe instanciada, neste exemplo, 
ClienteVIP. Caso não encontre ele vai subindo a cadeia. Ou seja, de ClienteVIP ele vai para Cliente e de Cliente para Pessoa, 
encontrando o metodo.
"""
