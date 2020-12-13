from dados import produtos, pessoas, lista
from functools import reduce   # Reduce é uma função acumuladora

"""
EXEMPLO DE ACUMULADOR
---------------------------------
acumula = 0
for item in lista:
    acumula += item

print(acumula)
"""

soma_lista = reduce(lambda ac, item: item + ac, lista, 0)   # reduce(lambda acumulador, item sendo somado ao acumulador, lista, valor inicial do acumulador)
print(soma_lista)

# ---------------------------------------------------------------------------------------------
print('\nSoma de todos os preços do dicionario de produtos: ')
soma_precos = round(reduce(lambda ac, p: p['preco'] + ac, produtos, 0), 2)   # round para arredondar o valor
print(soma_precos)   # ou print(soma_precos / len(produtos)) para ver a média de preço dos produtos

# ---------------------------------------------------------------------------------------------
print('\nSoma da idade de todas as pessoas do dicionario de pessoas: ')
soma_idades = reduce(lambda ac, p: p['idade'] + ac, pessoas, 0)
print(soma_idades)
print('Médida de idade:')
print(soma_idades / len(pessoas))