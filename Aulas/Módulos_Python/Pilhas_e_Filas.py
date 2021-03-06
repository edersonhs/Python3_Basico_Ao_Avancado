"""
Pilhas e filhas
Pilha (stack) - LIFO - last in, first out. (Ultimo a entrar, primeiro a sair)
    Exemplo: Pilha de livros que são adicionados um sobre o outro
Fila (queue) - FIFO - first in, first out. (Primeiro a entrar, primeiro a sair)
    Exemplo: Uma fila de banco (ou qualquer fila da vida real)
Filas podem ter efeitos colaterais em desenpenho, porque a cada item
alterado, todos os indices serão modificados.
"""
# Fila no Python:

# Collections possui estruturas de dados de alto desempenho
# Deque é semelhante a uma lista só que mais otimizado para listas
from collections import deque
from time import sleep


fila = deque(maxlen=10)   # Criando uma lista deque
# maxlen define um limite de indicies para a fila, caso ultrapasse o
# limite a primeira entrada será descartada e todos os atributos dos
# outros indices serão realocados

# Exemplo pratico
for i in range(1000000000000000):
    fila.append(i)
    # sleep(0.2)
    print(fila)

# print(f'Saiu: {fila.popleft()}')
# print(f'Saiu: {fila.popleft()}')
# print(f'Saiu: {fila.popleft()}')
# fila.extend([1, 2, 3, 4, 5, 5])   # Vai adicionar os elementos ao fim da lista
# fila.extendleft([1, 2, 3, 4, 5, 5])   # Vai adicionar os elementos ao inicio da lista

# Pilha no Python:

livros = list()
livros.append(1)
livros.append(2)
livros.append(3)

livros.pop()   # 3
livros.pop()   # 2
livros.pop()   # 1
