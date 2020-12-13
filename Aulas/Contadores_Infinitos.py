"""
count - Itertools
"""
from itertools import count

contador = count(start=5, step=0.5)   # Inicia no 5 e segue incrementando 0.5 (o Step aceita numero negativo pra fazer a contagem invertida também)


for valor in contador:
    print(round(valor, 2))   # Round arredonda o valor, neste caso, com duas casas decimais.

    if valor >= 10:
        break


################################################################
# WXEMPLO DE USO PRATICO
# =============================================================-
# Númerar uma lista

contador2 = count()
lista = ['ederson', 'João', 'Gustavo']
lista = zip(contador2, lista)

print(list(lista))   # [(0, 'ederson'), (1, 'João'), (2, 'Gustavo')]
