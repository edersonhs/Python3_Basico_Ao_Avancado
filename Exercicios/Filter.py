from dados import produtos, pessoas, lista

"""
Filter - serve para filtrar coisas
"""
# Filtrar apenas os números maiores que 5 da lista com Filter
nova_lista = filter(lambda x: x > 5, lista)  # Filtr vai retornar ou verdadeiro ou falso para a expressão(função) que passarmos
print(list(nova_lista)) # nova_lista é um iterador, por isso foi convertido para lista

# EX com list comprehension:
"""
nova_lista = [x for x in lista if x > 5]
"""
print()

# Filtrar um dicionario para puxar somente os produtos que tenham o preço maior do que 50 reais
nova_lista1 = filter(lambda prod: prod['preco'] > 50, produtos)
for produto in nova_lista1:
    print(produto)

# Exemplo com função, para caso seja necessario algo mais complexo

"""
def filtra(produto):
    if produto['preco'] > 50:
        return True
    else:
        return False

nova_lista1 = filter(filtra, produtos)
for produto in nova_lista1:
    print(produto)
"""
