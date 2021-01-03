# Cria um gerenciador de contexto sem precisar usar classe
from contextlib import contextmanager


@contextmanager   # Tranformando a função em um gerenciador de contexto
def arquivo(arquivo, modo):
    try:
        print('Abrindo arquivo')
        arquivo = open(arquivo, modo)
        yield arquivo   # Retorna o arquivo para o "with" sem parar a função.
    finally:
        print('Fechando arquivo')
        arquivo.close()


with arquivo('abc.txt', 'w') as arquivo:
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')
    arquivo.write('Linha 3\n')
