"""
https://openpyxl.readthedocs.io/en/stable/
pip install openpyxl
pipenv install openpyxl
"""
import openpyxl

pedidos = openpyxl.load_workbook('pedidos.xlsx')   # Carregando a planilha na variável
nome_planilhas = pedidos.sheetnames   # Vai retornar o nome das planilhas que o arquivo contem
# print(nome_planilhas)   # ['Página1']    sÓ tem uma pagina no arquivo

planilha1 = pedidos['Página1']   # Passando a pagina 1 para outra variável

# Acessando os dados por coluna e linha
# print(planilha1['b4'].value)   # b4 = Coluna B linha 4

# Mostrar uma coluna inteira:
# Exemplo1
# print([x.value for x in planilha1['b']])

# Exemplo2
# for campo in planilha1['b']:
#     print(campo.value)

# Acessando de um range especifico
# for linha in planilha1['a1:c2']:   # Coleta as duas primeiras linhas do planilha
#     for coluna in linha:
#         print(coluna.value)

# Acessando toda a planilha (com formatação especial)
for linha in planilha1:
    if linha[0].value is not None:
        print(linha[0].value, end='\t\t')
    if linha[1].value is not None:
        print(linha[1].value, end='\t\t')
    if linha[2].value is not None:
        print(linha[2].value)

