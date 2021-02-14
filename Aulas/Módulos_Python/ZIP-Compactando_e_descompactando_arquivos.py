from zipfile import ZipFile
import os   # Para listar arquivos do SO

caminho = r'C:\Users\eders\Downloads'

# Escrevendo um arquivo zip (caso já exista, sobrescreve)
with ZipFile('arquivo.zip', 'w') as zip:
    # Vai listar todos os arquivos do diretorio definido (não unclui subpastas)
    for arquivo in os.listdir(caminho):
        caminho_completo_arquivo = os.path.join(caminho, arquivo)
        print(caminho_completo_arquivo)

        # Zipando os arquivos do diretorio a partir do diretorio inicial do
        # caminho. Ou seja, Users > eders > Downloads > arquivo
        # zip.write(caminho_completo_arquivo)

        # Para zipar apenas os arquivos do diretorio informado:
        zip.write(caminho_completo_arquivo, arquivo)   # Caminho + nome arquivo

# Listando os arquivos contidos no zip
with ZipFile('arquivo.zip', 'r') as zip:
    for arquivo in zip.namelist():
        print(arquivo)

# Extraindo um arquivo zip
with ZipFile('arquivo.zip', 'r') as zip:
    # Definindo destino da extração (se não existir, cria) e extraindo
    zip.extractall('Descompactado')
