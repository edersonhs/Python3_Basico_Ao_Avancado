"""
Zip - Nativo (Junta apenas até o número de elementos da menor lista)
Zip_Longest - Itertools
"""

from itertools import zip_longest

cidades = ['São Paulo', 'Belo Horizonte', 'Salvador', 'Monte Belo']

estados = ['SP', 'MG', 'BA']

cidadesEstados = zip(estados, cidades)   # É um iterador

# print(next(cidadesEstados))     # EX SAÍDA PRIMEIRA VEZ: ('SP', 'São Paulo')

# for valor in cidadesEstados:
#     print(valor)

print(list(cidadesEstados))   # Saída: [('SP', 'São Paulo'), ('MG', 'Belo Horizonte'), ('BA', 'Salvador')]

# Pode-se também converter para um dicionario
print(dict(cidadesEstados))   # Ficando: {'SP': 'São Paulo', 'MG': 'Belo Horizonte', 'BA': 'Salvador'}


###############################################################################################################

# Zip_Longest     Junta até o numero de elementos da maior lista, se uma das listas for menor o elemento dela é
# Substituido por "None"
# -------------------------------------------------------------------------------------------------------------

cidadesEstados2 = zip_longest(estados, cidades)   # iterador
print(list(cidadesEstados2))   # Saída: [('SP', 'São Paulo') ... (None, 'Monte Belo')]

# -------------------------------------------------------------------------------------------------------------
# Definir valor padrão para substituir o None

cidadesEstados3 = zip_longest(estados, cidades, fillvalue='Estado')   # O None será substituido por Estado
print(list(cidadesEstados3))   # [('SP', 'São Paulo') ... ('Estado', 'Monte Belo')]
