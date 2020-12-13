# https://docs.python.org/3/library/exceptions.html

"""
Raise serve para lançar e relançar uma exceção no python
"""

def divide(n1, n2):
    try:
        return n1/ n2
    except ZeroDivisionError as error:
        print('Log:', error) # Loguei o error
        raise # reloga o erro (Retorna a descrição da exceção disparada novamente

try:
    print(divide(2, 0))
except ZeroDivisionError as error:
    print(error)

"""
------------------------------------------------------------------------------------------------------------
Levantar uma exceção propia
"""
def divide2(n1, n2):
    if n2 == 0:
        raise ValueError('n2 não pode ser 0.')   # Define o tipo de exceção e a mensagem da descrição.
    return n1 / n2

try:
    print(divide2(2, 0))
    """   Saída no terminal:
    Traceback (most recent call last):
    line 24, in <module>
        print(divide2(2, 0))
    line 21, in divide2
        raise ValueError('n2 não pode ser 0.')
    ValueError: n2 não pode ser 0.
    """
except ValueError as error:
    print(error)
