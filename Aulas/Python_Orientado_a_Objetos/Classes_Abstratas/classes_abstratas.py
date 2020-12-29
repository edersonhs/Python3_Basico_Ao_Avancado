"""
Classes Abstratas:

Classe generica que não é criada com o intuito de ser instanciada.
Geralmente não contem um "corpo"
Um método é criado e definido como abstrato para que as outras
classes filhas herdem este método e sejam obrigadas a crialo dentro
das classes filhas.
"""
# Criando uma classe abstratas
from abc import ABC, abstractmethod  # Abstratic Base Class


# Criando a classe A e herdando a classe ABC importada do módulo abc
class A(ABC):
    @abstractmethod   # Decora o método falar como abstrato
    def falar(self):
        """
        método abstrato que deve ser obrigatoriamente escrito em
        todas as classes que herdem A

        O método não necessariamente precisa ter algo, pode ser
        criado apenas para tornar a classe abstrata.

        Todas as classes que herdarem A terão este metodo, tornando-as
        abstratas também, não podendo ser instanciadas.
        """
        pass


class B(A):   # Herda a classe A e sobrescreve o metodo falar
    """
    Para fazer com que a classe volte ao normal, mesmo herdando a classe A
    basta reescrever o método abstrato.
    """

    def falar(self):
        print('Falando...')


a = A()
