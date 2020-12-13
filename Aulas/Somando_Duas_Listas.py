"""
Considere duas listas de inteiros ou floats (lista A e lista B)
Some os valores nas listas retornando uma nova lista com os valores somados:

Se uma lista for maior que a outra, a soma só vai considerar o tamanho da menor.

Exemplo:
lista_a     = [1, 2, 3, 4, 5, 6, 7]
lista_b     = [1, 2, 3, 4]

========================= Resultado
lista_soma [2, 4, 6, 8]
"""
lista_a = [1, 2, 3, 4, 5, 6, 7]
lista_b = [1, 2, 3, 4]

lista_soma = [x + y for x, y in zip(lista_a, lista_b)]   # Ou [x + y for x, y in zip_longest(lista_a, lista_b, fillvalue=0)] para incluir os outros elementos da lista maior
soma = 0

# for tupla in list(zip(lista_a, lista_b)):
#     for indice in tupla:
#         soma += indice
#     lista_soma.append(soma)
#     soma = 0

print(lista_soma)
