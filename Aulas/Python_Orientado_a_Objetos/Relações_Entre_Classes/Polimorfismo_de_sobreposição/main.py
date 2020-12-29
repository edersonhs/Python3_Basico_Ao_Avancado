"""
Polimorfismo é o principio que permite que classes derivadas de uma mesma
superclasse tenham métodos iguais (de mesma assinatura) mas comportamentos diferentes.

Mesma assinatura = Mesma quantidade e tipo de parâmetros
"""

from abc import ABC, abstractmethod


class A(ABC):
    @abstractmethod
    def fala(self, msg):
        pass


class B(A):
    def fala(self, msg):   # Mesma assinatura, mesma quantidade de parâmetros
        # comportamento diferente do método da classe super
        print(f'B esta falando {msg}')


class C(A):
    def fala(self, msg):   # Mesma assinatura, mesma quantidade de parâmetros
        # comportamento diferente do método da classe super
        print(f'C esta falando {msg}')


b = B()
c = C()
b.fala('Um assunto')
c.fala('Outro assunto')

"""
Obs: Python não suporta polimorfismo de sobrecarga.
"""
