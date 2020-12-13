# Mutável: Listas, dicionários
# Imutável: Tuplas, strings, números, True, False, None

"""
Em uma versão diferente do exemplo abaixo as listas cliente1, cliente2 e cliente 3
seriam as mesmas devido a listas do parametro da função lista-de_clientes ser mutavel (lista={})
"""
def lista_de_clientes(clientes_iteravel, lista=None): 
    if lista is None:   # "Se não houver nada na lista, crie uma nova."
        lista = []
    lista.extend(clientes_iteravel)
    return lista


lista_clientes_1 = ['Fabrício']
clientes1 = lista_de_clientes(['João', 'Maria', 'Eduardo'], lista_clientes_1)
clientes2 = lista_de_clientes(['Marcos', 'Jonas', 'Zico'])
clientes3 = lista_de_clientes(['José'])

print(clientes1)
print(clientes2)
print(clientes3)
