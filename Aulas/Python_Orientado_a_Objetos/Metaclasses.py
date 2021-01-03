"""
EM PYTHON TUDO É UM OBJETO: incluindo classes
Metaclasses são as "classes" que criam classes.
type é uma metaclasse (!!!???)
"""
# Criando uma metaclasse que define como as classes que a herdarem devem
# funcionar


class Meta(type):
    def __new__(mcs, name, bases, namespace):
        """
        mcs = Metaclasse
        name = Nome da classe que esta sendo criada
        bases = Classes pai da classe sendo criada
        namespace = Contem todo o atributo de classe e todo o método que é
                    criado na mesma. Toda classe possui um namespace.
        """
        # print(name)   # Saída: A e B, pois são as classes criadas com a Meta

        if name == 'A':   # Definindo o comportamento da classe A
            # Retorna a classe
            return type.__new__(mcs, name, bases, namespace)

        # print(namespace)   # Mostra tudo que existe em B
        """
        Saída seria:
        {'__module__': '__main__', '__qualname__': 'B', 'b_fala':
        <function B.b_fala at 0x000001FD9C25BAF0>}
        """

        if 'b_fala' not in namespace:   # Se b_fala não existir em B, faça:
            print(f'Oi, você precisa criar o método b_fala em {name}')
        else:
            # Se não for um método, faça:
            if not callable(namespace['b_fala']):
                print(f'b_fala precisa ser um método, não atributo em {name}')

        # Impedindo que o attr_classe de A seja sobrescrito pelas instancias
        if 'attr_classe' in namespace:
            """
            Toda vez que a classe B é criada e o atributo attr_classe é
            definido em B ele é removido. Mantendo o valor de attr_classe de A
            """
            print(f'{name} tentou sobrescrever o atributo mas foi impedido!')
            del namespace['attr_classe']

        return type.__new__(mcs, name, bases, namespace)


class A(metaclass=Meta):   # Definindo Meta como a metaclasse de A
    """
    Toda classe que herdar A, se comportará da forma que for definida na
    metaclasse Meta, conforme herança.
    """
    attr_classe = 'Valor A'   # Atributo de exemplo que não deve ser reescrito

    def fala(self):
        self.b_fala()


class B(A):
    attr_classe = 'Valor B'   # Tentanto sobrescrever attr herdado de A
    b_fala = 'Oi'
    # def b_fala(self):
    #     print('Olá')
    pass


class C(B):
    attr_classe = 'Valor C'


b = B()
# b.fala()   # Chamando um método da classe A que chama um método de B
print(b.attr_classe)

c = C()

"""
A type é uma metaclasse também utilizada para criar classes.

Exemplo de criação de classe manualmente com o Type:

A = type(
    'A',   # Nome da classe
    (),   # De quem a classe será herdada
    {'attr': 'Olá mundo!'}   # Atributos da classe
)

a = A()
print(a.attr)   # Olá mundo!
print(type(a))   # <class '__main__.A'>
"""
