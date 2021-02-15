"""
Executar programas python como scripts no sistema. (Sem IDE)

Para execução no windows:
- No cmd: python <nomeDoArquivo.py>

Para execução no windows com argumentos:
- No cmd: python <nomeDoArquivo.py> -a -b -teste
-a, -b e -teste seriam argumentos que podem ser interpretados no codigo
"""
import sys
import os

# Lendo e armazenando os argumentos passados na execução para a variavel
argumentos = sys.argv   # Será uma lista.
# A primeira posição da lista sempre será o nome do arquivo, depois os
# argumentos informados na execução

# print(argumentos)   # ['NomeDoArquivo.py', '-a', '-b', '-teste']

# Impedindo que o código seja executado sem argumentos
qtd_argumentos = len(argumentos)
if qtd_argumentos <= 1:
    print('Faltam Argumentos:')
    print('-a', ' Para listar todos os arquivos nesta pasta', sep='\t')
    print('-d', ' Para listar todos os diretorios nesta pasta', sep='\t')
    sys.exit()

so_arquivos = False
if '-a' in argumentos:
    so_arquivos = True

so_diretorios = False
if '-d' in argumentos:
    so_diretorios = True

# Direotirio . é o diretorio atual em que o script foi executado
for arquivo in os.listdir('.'):
    if so_arquivos:
        if os.path.isfile(arquivo):   # Verificando se é um arquivo
            print(arquivo)

    if so_diretorios:
        if os.path.isdir(arquivo):   # Verificando se é um arquivo
            print(arquivo)
