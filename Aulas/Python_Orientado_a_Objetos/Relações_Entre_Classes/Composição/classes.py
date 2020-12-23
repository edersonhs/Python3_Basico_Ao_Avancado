"""
Neste caso, a classe endereço, pertence a classe cliente. Ou seja, quando a classe Cliente é criada,
e cria uma classe endereço, assim que ela for apagada, a classe endereço que foi usada por ela também 
será apagada da memoria.
"""

class Cliente:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.enderecos = []   # Irá receber objetos da classe endereço, visto que um cliente pode ter mais de um endereço
    
    def insere_endereco(self, cidade, estado):
        self.enderecos.append(Endereco(cidade, estado))   # "instancia" o objeto da classe endereço na ultima posição da lista
    
    def lista_enderecos(self):
        for endereco in self.enderecos:
            print(endereco.cidade, endereco.estado)
    
    def __del__(self):
        print(f'{self.nome} FOI APAGADO')
    

class Endereco:
    def __init__(self, cidade, estado):
        self.cidade = cidade
        self.estado = estado
    
    def __del__(self):
        print(f'{self.cidade}/{self.estado} FOI APAGADO')
