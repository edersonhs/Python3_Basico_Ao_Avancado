file = open('test.txt', 'w+')
file.write('Linha 1\n')
file.write('Linha 2\n')
file.write('Linha 3\n') # O ponteiro do python sempre para no fim da ultima string passada para o arquivo.

file.seek(0, 0) # Move o cursor para a posição 0(inicio do arquivo)
print('Lendo linhas: ')
print(file.read())

print('########################')

file.seek(0, 0) # Move o cursor para a posição 0(inicio do arquivo)
print(file.readline(), end='')   # Lê linha por linha
print(file.readline(), end='')
print(file.readline(), end='')

print('########################')

file.seek(0, 0)
print(file.readlines())   # Retorna uma lista com todas as linhas do arquivo

file.close()

print()
"""
-----------------------------------------------------------------------------------------------------
Ao invéz de usar try, ou abrir o arquivo e depois ter de fechar ele, pode-se usar o seguinte:
"""
print('#' * 24, '\nGERENCIADOR DE CONTEXTO NO PYTHON')

with open('abc.txt', 'w+') as file:   # O gerenciador de contexto vai abrir o arquivo e quando terminar de usar, o fechará automaticamente
    file.write('Linha 1\n')
    file.write('Linha 2\n')
    file.write('Linha 3\n')

    file.seek(0, 0)
    print(file.read())

"""
APAGAR O ARQUIVO
"""
import os
os.remove('abc.txt')
os.remove('test.txt')


"""
.JSON
"""
import json 

dicionario = {
    'Pessoa 1': {
        'nome': 'Luiz',
        'idade': 25,
    },
    'Pessoa 2': {
        'nome': 'Rose',
        'idade': 30,
    }
}

dicionario_json = json.dumps(dicionario, indent=True)   # Converte o dicionario para um json. //  indent=True formata o json

with open('dicionario.json', 'w+') as file:   # Cria o arquivo .json
    file.write(dicionario_json)   # escreve o json no arquivo
