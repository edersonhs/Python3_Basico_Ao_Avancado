from itertools import groupby   # Serve para agrupar os elementos de um dicionario
from itertools import tee   # Copia um iterador

"""
*Groupby precisa que o dicionario esteja ordenado

EX: Se ordenar por nota, todas as notas devem estar ordenados (ordem alfabética)
"""
alunos = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Letícia', 'nota': 'B'},
    {'nome': 'Fabricio', 'nota': 'A'},
    {'nome': 'Rosemary', 'nota': 'C'},
    {'nome': 'Joana', 'nota': 'D'},
    {'nome': 'João', 'nota': 'A'},
    {'nome': 'Eduardo', 'nota': 'B'},
    {'nome': 'André', 'nota': 'A'},
    {'nome': 'Anderson', 'nota': 'C'},
    {'nome': 'José', 'nota': 'B'},
]

ordena = lambda item: item['nota']
alunos.sort(key=ordena)
alunos_agrupados = groupby(alunos, ordena)

#for agrupamento, valores_agrupados in alunos_agrupados:
#    print(f'Agrupamento: {agrupamento}')   # A notas são as chaves/indice
#    for aluno in valores_agrupados:
#        print(aluno)
#    print()

"""
Agrupamento: A
{'nome': 'Luiz', 'nota': 'A'}
{'nome': 'Fabricio', 'nota': 'A'}
{'nome': 'João', 'nota': 'A'}
{'nome': 'André', 'nota': 'A'}

Agrupamento: B
{'nome': 'Letícia', 'nota': 'B'}
{'nome': 'Eduardo', 'nota': 'B'}
{'nome': 'José', 'nota': 'B'}

Agrupamento: C
{'nome': 'Rosemary', 'nota': 'C'}
{'nome': 'Anderson', 'nota': 'C'}

Agrupamento: D
{'nome': 'Joana', 'nota': 'D'}
"""

for agrupamento, valores_agrupados in alunos_agrupados:
    va1, va2 = tee(valores_agrupados)   # Copia o iterador calores_agrupados para os outros dois iteradores va1 e va2

    print(f'Agrupamento: {agrupamento}')   # A notas são as chaves/indice
    
    for aluno in va1:
        print(f'\t{aluno}')
    
    quantidade = len(list(va2))
    print(f'\t{quantidade} Alunos tiraram a nota {agrupamento}')
    print()
