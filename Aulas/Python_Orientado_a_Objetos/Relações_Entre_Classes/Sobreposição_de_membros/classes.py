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
    
    def falar(self):   # Definindo o método falar aqui, a classe Cliente se tornaria a "super" de falar
        print('Estou em Cliente.')


class Aluno(Pessoa):   # Aluno herda da classe pessoa Pessoa   ("Um aluno é uma pessoa")
    def estudar(self):   # Estudar pertence a aluno, e somente ao aluno
        print(f'{self.nomeclasse} estudando...')


class ClienteVIP(Cliente):    # ClienteVIP herda da classe Cliente e consequentemente a classe Pessoa ("Um ClienteVIP também é um Cliente/Pessoa")
    """
    Sobreposição de métodos, atributos de classe e atributos de instancia
    """
    def __init__(self, nome, idade, sobrenome): # Sobrescreve o contrutor herdado de Pessoa.   |  Recebe no contrutor os mesmos parametros do contrutor de Pesoa
            super().__init__(nome, idade)   # Executa o contrutor de Pessoa e configura os atributos nome, idade e nomeclasse
            # Pessoa.__init__(self, nome, idade)   # Chamando o contrutor de Pessoa manualmente
            self.sobrenome = sobrenome
    
    def falar(self):   #  # Sobrescreve o método falar que é herdado de Cliente
        Pessoa.falar(self)
        Cliente.falar(self)
        print(f'{self.nome} {self.sobrenome}')
    """
    def falar(self):   # Sobrescreve o método falar que é herdado de Pessoa
        # super().falar()   # Super executa primeiro o que esta no método falar da super classe, que neste caso é Pessoa. Util para caso o contrutor(__init__) seja reescrito.
        Pessoa.falar(self)   # Chamar o método de outra classe "manualmente"
        Cliente.falar(self)
        print('Outra coisa qualquer.')
    """