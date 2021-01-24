"""
Documentação: https://docs.python.org/pt-br/3/library/enum.html
"""
from enum import Enum, auto


class Directions(Enum):
    # Enum: permite TypeHinting. EX: "isinstance(direction, Directions)"
    right = auto()   # Gera os valores automaticamente. De 1 em diante...
    left = 2
    up = 3
    down = 4


def move(direction):
    # verifica se direção é uma instancia de Directions
    if not isinstance(direction, Directions):
        raise ValueError('Cannot move in this direction!')
    return f'Moving {direction.name}'   # Retorna o nome do atributo da classe


if __name__ == '__main__':
    print(move(Directions.right))
    print(move(Directions.left))
    print(move(Directions.up))
    print(move(Directions.down))

    print()

    for direction in Directions:
        print(direction, direction.value, direction.name)
