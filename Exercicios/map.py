from dados import produtos, pessoas, lista

"""
map recebe uma função como primeiro argumento, no exempço usamos uma função lambda

* map não retorna uma lista pronta, e sim um iterador.
"""
nova_lista = map(lambda x: x * 2, lista)   # Retornara uma nova lista com os valores multiplicados por 2

print(lista)
print(list(nova_lista))   # convertendo o iterador do map para uma lista

# ----------------------------------------------------------------------------------------------------------------
# Pegar só os preços do dicionário de produtos com o map
print('-'*150, f'\nDicionarios de Produtos: \n{produtos}')
precos = map(lambda p: p['preco'], produtos)

print('\nApenas os preços:')
for preco in precos:
    print(preco)

# ----------------------------------------------------------------------------------------------------------------

print('\nPreços com +5%')
def aumenta_preco(p):
    p['preco'] = round(p['preco'] * 1.05, 2)   # Arredondando para no maximo duas casas decimais
    return p

novos_produtos = map(aumenta_preco, produtos)   # Passa cada elemento de produtos para a função aumenta preco

for prod in novos_produtos:
    print(prod)

# ----------------------------------------------------------------------------------------------------------------
print('\nApenas os nomes das pessoas do dicionario de pessoas:') 

nomes = map(lambda p: p['nome'], pessoas)

for nome in nomes:
    print(nome)

# ----------------------------------------------------------------------------------------------------------------
print('\nAumentando em 20% a idade das pessoas:') 

def aumenta_idade(p):
    p['nova_idade'] = round(p['idade'] * 1.20)   # Aumentando em 20% a idade de cada pessoa do dicionario e arredondando
    return p

idades = map(aumenta_idade, pessoas)

for pessoa in idades:
    print(pessoa)
