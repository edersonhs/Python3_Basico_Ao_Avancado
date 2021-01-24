"""
Implementando um iterador para a classe manualmente.

O intuito é deixar a classe o mais semelhante possivel a uma lista.
"""


class MinhaLista:
    def __init__(self):
        self.__items = []
        self.__index = 0   # variável de controle

    def add(self, valor):
        self.__items.append(valor)

    def __getitem__(self, index):   # Buscar elemento da lista por indice
        return self.__items[index]

    def __setitem__(self, index, valor):   # Setando novo valor para indice da lista
        if index >= len(self.__items):
            self.__items.append(valor)
        self.__items[index] = valor

    def __delitem__(self, index):
        del self.__items[index]

    def __iter__(self):   # Definindo o iterador da classe
        return self   # O iterador é a propria classe

    def __next__(self):   # vai retornar o proximo elemento da lista
        try:
            item = self.__items[self.__index]
            self.__index += 1
            return item
        except IndexError:
            raise StopIteration   # Para a iteração do laço quando disparado

    def __str__(self):
        return f'{self.__class__.__name__}({self.__items})'


if __name__ == '__main__':
    lista = MinhaLista()
    lista.add('Luiz')
    lista.add('Maria')

    # print(next(lista))
    print('Laço de repetição:')
    for valor in lista:
        print(valor)

    print('\nPor indice:')
    print(lista[0])
    print(lista[1])

    print('\nAlterando valor por indice:')
    lista[0] = 'João'
    print(lista)
    lista[2] = 'Carlos'   # Adiciona carlos na lista, visto que 2 > range da lista
    print(lista)

    print('\nApagando valor da lista por indice:')
    del lista[2]
    print(lista)

    # Convertendo a instancia da classe MinhaLista para uma lista
    lista = list(lista)
