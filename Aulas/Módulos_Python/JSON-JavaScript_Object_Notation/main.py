"""
JavaScript Object Notation - JSON
JSON é um formato de troca de dados entre sistemas e programas muito leve e
de facil utilização. Muito utilizado por APIs

Documentação : https://docs.python.org/3/library/json.html
"""
from dados import clientes_dicionario, clientes_json
import json

# ################# Convertendo de Python para JSON ######################
lista = [1, 2, 3, 4, 5, 6]
dados_json = json.dumps(lista)   # Convertendo a lista para um array json
print(type(dados_json))   # É uma string que contem dados na estrutura json

# Convertendo um dicionario para uma string de estrutura json, com dumps
dados_json = json.dumps(clientes_dicionario)
print('\n', dados_json, sep='')
# O formato é bastante similar ao do Python, mas é a estrutura objeto
# json de um dicionario do Python

# Para melhorar a vizualização, habilitar o parametro indent=4 espaços:
dados_json = json.dumps(clientes_dicionario, indent=4)
print('\n', dados_json, sep='')   # Vizualização do json indentado


# ################# Convertendo de JSON para Python ######################
dicionario = json.loads(clientes_json)
print('\n', dicionario, sep='')


# ##### Convertendo de python para json e salvando em um arquivo ##########
with open('clientes.json', 'w') as arquivo:
    json.dump(clientes_dicionario, arquivo, indent=4)
# Para salvar o json em um arquivo deve-se usar o dump ao invez do dunps
# passando nos parametros o dado que esta sendo convertido e o arquivo onde
# será salvo


# ###### Convertendo de json para Python a partir de um arquivo ###########
with open('clientes.json', 'r') as arquivo:
    dados = json.load(arquivo)
    # Para ler um arquivo json e converter para python usamos o load, e não
    # o loads conforme anteriormente
print('\n', dados, sep='')
