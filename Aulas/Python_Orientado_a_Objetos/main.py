from pessoa import Pessoa

# p1 e p2 são pessoas! Entretanto estão em locais diferentes da memoria
p1 = Pessoa('Luiz', 29)   # Criando um objeto a partir de uma classe (Utilizando um molde(classe) para criar uma pessoa)
p2 = Pessoa('João', 32)   # Utilizando um molde(classe) para criar outra pessoa

"""
# mostrando as posição dos objetos na memoria
print(p1)
print(p2)
"""

"""
# Exemplo de atribuição em uma classe (Cria variavel diretamente na instancia)
p1.nome = 'Luiz'   # É o mesmo que passar o nome para o método __init__ da classe. Como no ex: p1 = Pessoa('Luiz')
p2.nome = 'João'

print(p1.nome)
print(p2.nome)
"""

p1.comer('Maçâ')   # Saída: Luiz esta comendo maçâ.
p1.comer('Maçâ')   # Saída: Luiz já está comendo.

p1.falar('POO')   # Saída: Luiz não pode falar comendo.

p1.parar_comer()   # Saída: Luiz parou de comer.
p1.parar_comer()   # Saída: Luiz não está comendo. 

p1.falar('POO')   # Saída: Luiz não pode falar comendo.

p1.comer('Maçâ')   # Saída: Luiz não pode comer enquanto fala.

p1.parar_falar()   # Saída: Luiz parou de falar.
p1.parar_falar()   # Saída: Luiz não esta falando.

p1.comer('Abacaxi')   # Saída: Luiz está comendo Abacaxi.

print('\n----------------------------------------------------------------------\n')
"""
Cada "pessoa" utiliza a mesma classe modelo e funciona indiferente da situação das outras pessoas
"""
p2.comer('Churrasco')
p2.falar('Programação')
p2.parar_comer()
p2.falar('Programação')

# ------------------------------------------------------------------------------------------------------------------------
print('\n----------------------------------------------------------------------\n')
print(p1.ano_atual)   # Pega a variavel do escopo global da classe Pessoa
print(p2.ano_atual)   # Pega a variavel do escopo global da classe Pessoa
print(Pessoa.ano_atual)   # # Exemplo direto com a classe em Sí

print('\n----------------------------------------------------------------------\n')
print(p1.get_ano_nascimento())   # 1991
print(p2.get_ano_nascimento())   # 1988
