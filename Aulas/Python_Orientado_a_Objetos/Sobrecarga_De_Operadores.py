"""
No python, o comprimento dos operadores é definido por métodos especiais.
Vamos alterar o comportamento de operadores com classes definidaas pelo usuário

Métodos especiais do Python:
------------------------------------------------------
Operador    Método          Operação
------------------------------------------------------
+           __add__         adição
-           __sub__         subtração
*           __mul__         multiplicação
/           __div__         divisão
//          __floordiv__    divisão inteira
%           __mod__         Módulo
**          __pow__         Potência
+           __pos__         Positivo
-           __neg__         Negativo
<           __lt__          Menor que
>           __gt__          Maior que
<=          __le__          Menor ou igual a
>=          __ge__          Maior ou igual a
==          __eq__          Igual a
!=          __ne__          Diferente de
<<          __lshift__      Deslocamento para a esquerda
>>          __rshift__      Deslocamento para a direita
&           __and__         E bit-a-bit
|           __or__          OU bit-a-bit
^           __xor__         OU exclusivo bit-a-bit
~           __inv__         inversão
"""

# Todo método que inicia e termina com dois underlines é conhecido como método
# magico. Ex: __init__


class Retangulo:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_area(self):
        return self.x * self.y

    # Muda o comportamento do python quando ocorre o print de uma instancia
    # Desta classe
    def __repr__(self):
        return f"<Class 'Retangulo({self.x}, {self.y})'>"

    # Configurando o método __add__ do python, que ensina o python a manipular
    # os objetos do tipo "Retangulo" quando houver um operador de +
    def __add__(self, other):   # Factory method - Cria um obj para a classe
        """
        Self: representa o primeiro objeto ou a instancia em sí recebido na
        operação. (***r1*** + r2)

        Other: outro objeto, que nesse caso seria o r2.
        """
        novo_x = self.x + other.x   # Soma o x dos dois Retangulos
        novo_y = self.y + other.y   # Soma o y dos dois Retangulos
        # Retorna a classe Retangulo com o novo retangulo
        return Retangulo(novo_x, novo_y)

    def __lt__(self, other):   # Configurando o comportamento do "< que".
        a1 = self.get_area()
        a2 = other.get_area()

        if a1 < a2:
            return True
        else:
            return False

    def __gt__(self, other):   # Configurando o comportamento do > que".
        a1 = self.get_area()
        a2 = other.get_area()

        if a1 > a2:
            return True
        else:
            return False

    def __eq__(self, other):   # Configurando igualdade para o tipo de dado.
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False


r1 = Retangulo(10, 20)
r2 = Retangulo(10, 20)

"""
ANTES DE DEFINIR O MÉTODO __add__
"""
# TypeError: unsupported operand type(s) for +: 'Retangulo' and 'Retangulo'
# print(r1 + r2)
"""
O  interpretador do Python não saberia o que fazer com esse tipo de
dado, visto que ele foi criado pelo programador.
"""
# --------------------------------------------------------------------------
"""
DEPOIS DE DEFINIR O MÉTODO __add__
"""
r3 = r1 + r2

"""
Antes de definir o método __repr__ a saída era:

print(r3)   # Saída: <__main__.Retangulo object at 0x000002DB0BBC2E50>
"""
print(r3)   # <Class 'Retangulo(20, 40)'>
print(r3 < r1)   # False
print(r1 == r2)  # True
