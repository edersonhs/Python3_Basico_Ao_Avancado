"""
# Usa o r no inicio para poder usar a contrabarra
caminho_windows = r'C:\programas\exemplo'
"""
import os
import shutil   # MOVER E COPIAR ARQUIVOS

caminho_original = r'D:\Documents'
caminho_novo = r'D:\Documents\Exemplo'

try:
    os.mkdir(caminho_novo)   # Cria a pasta
except FileExistsError:
    print(f'Pasta {caminho_novo} já existe.')

for root, dir, files in os.walk(caminho_original):
    """
    root: Caminho do diretorio original até o arquivo
    dir: lista com os diretorios dentro do diretorio original
    files: lista com os arquivos contidos do diretorio original em diante
    """
    for file in files:
        old_file_path = os.path.join(root, file)  # caminho antigo do arquivo
        new_file_path = os.path.join(
            caminho_novo, file)   # Caminho novo do arquivo

        # Copiar o arquivo de uma pasta para outra pasta
        shutil.copy(old_file_path, new_file_path)
        print(f'Arquivo {file} copiado com sucesso!')

        # Mover o arquivo do caminho antigo para o novo caminho
        shutil.move(old_file_path, new_file_path)
        print(f'Arquivo {file} movido com sucesso!')

        # os.remove(file_path)   # Para excluir
        """
        shutil.move também serve para renomear arquivos, desde que o caminho
        original esteja correto pode-se inserir o novo nome desejado no
        caminho de destino
        """
