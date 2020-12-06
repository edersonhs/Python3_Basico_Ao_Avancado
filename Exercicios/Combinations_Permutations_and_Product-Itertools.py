"""
Combinations, Permutations e Product - Itertools
Combinação - Ordem não importa
Permutação - Ordem importa
Ambos não repetem valores únicos
Produto - Ordem importa e repete valores únicos 
"""
from itertools import combinations, permutations, product

pessoas = ['Luiz', 'Andre', 'Eduardo', 'Letícia', 'Fabrício', 'Rose']

print('\nCOMBINATIONS >>>>>>\n')
for grupo in combinations(pessoas, 2):
    """
    Mostra todas as combinações possiveis em grupos de dois da lista onde a ordem NÃO IMPORTA.
    Ou seja, se ('Luiz', 'Andre') existe, a ordem ('Luiz', 'Andre') não existirá, visto que é como se fosse a mesma coisa
    """
    print(grupo)

print('\nPERMUTATIONS >>>>>>\n')
for grupo in permutations(pessoas, 2):
    """
    Mostra todas as combinações possiveis em grupos de dois da lista onde a ordem IMPORTA.
    Ou seja, se ('Luiz', 'Andre') existe, a ordem ('Luiz', 'Andre') EXISTIRÁ também, visto que são diferentes quando levamos em consideração a ordem
    """
    print(grupo)

print('\nPRODUCT >>>>>>\n')
for grupo in product(pessoas, repeat=2):
    """
    Mostra, desta vez realmente TODAS as combinações possiveis em grupos de dois da lista onde a ordem IMPORTA e os valores podem ser repetidos.
    Ou seja, se ('Luiz', 'Andre') existe, a ordem ('Luiz', 'Andre') EXISTIRÁ também, visto que são diferentes quando levamos em consideração a ordem.
    ('Luiz', 'Luiz') também será uma combinação possivel.
    """
    print(grupo)
