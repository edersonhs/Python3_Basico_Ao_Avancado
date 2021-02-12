import random
# Contem funções que retornam o abecedario maiusculo/minusculo e todos os
# números.
import string

# Gera um numero inteiro aleatorio entre A e B
inteiro = random.randint(1, 100)

# Gera um número aleatorio usando a função range()
# Vai retornar um número inteiro aleatorio entre 900 e 1000 pulando de 10 em 10
inteiro2 = random.randrange(900, 1000, 10)

# Gera um numero de ponto flutuante aleatorio entre A e B
flutuante = random.uniform(1, 100)

# Gera um número de ponto flutuante aleatorio entre 0 e 1
flutuante2 = random.random()

# Sorteando um elemento da lista randomicamento com choice
lista = ['Luiz', 'Otavio', 'Maria', 'Rose', 'Jenny', 'Danilo', 'Felipe']
sorteio = random.choice(lista)

# Sorteando UM ou MAIS elementos da lista com choices
sorteio2 = random.choices(lista, k=2)
"""
Choices() permite um fatiamento aleatorio da lista com o parametro k:
k=2   # Sorteia dois itens selecionados aleatoriamente e retorna uma lista

choices pode repetir os elementos sorteados, ou seja, pode ocorrer de 
['Luiz', 'Luiz'] ser retornado.
"""

# Sorteando UM ou MAIS elementos da lista sem repetir elementos já sorteados
sorteio3 = random.sample(lista, 2)   # Lista, Quantidade de elementos sorteados

# Embaralhar uma lista (Reordenar aleatoriamente)
random.shuffle(lista)

"""
EXEMPLO PRATICO:   Gerae senha aleatoria
"""
# Retorna todas as letras do alfabeto maiusculas e minusculas
letras = string.ascii_letters
# string.ascii_lowercase   # Para retornar apenas letras minusculas
# string.ascii_uppercase   # Para retornar apenas letras maiusculas

# Retorna todos os digitos possiveis (0...9)
digitos = string.digits

caracteres_especiais = '!@#$%¨&*._-'
geral = letras + digitos + caracteres_especiais

# Retorna uma senha de 20 caracteres
senha = "".join(random.choices(geral, k=20))

print(senha)
