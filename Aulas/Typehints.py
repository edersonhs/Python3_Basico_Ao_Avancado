"""
Typing = https://docs.python.org/3/library/typing.html

Definir o tipo do atributo na definição para melhor entendimento do código

Ps: Isso não necessariametne define o tipo. Ex:
x: int = 'Teste'   # não levantaria um erro, só avisos na indentação

"""
from typing import Union

x: int = 10
y: float = 10.5
z: bool = False


# -> float: Significa que a função retorna um float
def funcao(p1: float, p2: str, p3: dict) -> float:
    return 10.10


# Caso a função retorne mais de um tipo de dado:
def funcao2() -> Union[list, dict]:
    return []


print(funcao(10.1, 'str', {}))
