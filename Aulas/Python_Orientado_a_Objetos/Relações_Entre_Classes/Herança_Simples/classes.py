# SUPER CLASSE
class Pessoa:   # Define os metodos principais e mais genéricos de Pessoa para as classes Especializadas Cliente e Pessoa
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nomeclasse = self.__class__.__name__   # Recebe o nome da classe sendo utilizada no momento
    
    def falar(self):   # Falar pertence tanto a Pessoa quando a Cliente e Aluno
        print(f'{self.nomeclasse} falando...')

"""
Para não repetir o código, no exemplo de herança abaixo, as duas classes precisariam dos mesmo dados,
e por este motivo estão herdando a classe Pessoa, que coleta os dados necessarios para ambos os casos.
"""

#SUB CLASSES
class Cliente(Pessoa):   # Cliente herda da classe pessoa Pessoa. ("Um Cliente é uma pessoa")
    def comprar(self):   # comprar pertence a Cliente, e somente ao Cliente
        print(f'{self.nomeclasse} comprando...')


class Aluno(Pessoa):   # # Aluno herda da classe pessoa Pessoa   ("Um aluno é uma pessoa")
    def estudar(self):   # Estudar pertence a aluno, e somente ao aluno
        print(f'{self.nomeclasse} estudando...')
