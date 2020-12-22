"""
Getter - Obtem um valor
Setter - Configurar um valor

Serve como uma "proteção" para o atributo
"""
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
    
    def desconto(self, percentual):
        self.preco = self.preco - (self.preco * (percentual / 100))
    
    # EX1 - PRECO
    # Getter
    @property   # Decorador de propriedade
    def preco(self):   # Vai ter o mesmo nome do atributo a ser obtido
        return self._preco   # Retornar o mesmo nome da variavel obtida pode gerar um loop, portanto por conveção usa-se o nome do atributo com um _ antes

    # Setter
    """
    Sempre que um valor for atribuido a algo, antes o valor passará pelo setter
    """
    @preco.setter   # o decorador tem que ser @NomeDaPropriedade.setter
    def preco(self, valor):
        if isinstance(valor, str):   # retorna True se o valor for uma instancia de string
            valor = float(valor.replace('R$', ''))
        self._preco = valor   # retorna o _preco para o self.preco do __init__
    
    # EX2 - NOME
    # Getter
    @property
    def nome(self):
        return self._nome

    # Setter
    @nome.setter
    def nome(self, valor):
        self._nome = valor.title()


p1 = Produto('CAMISETA', 50)
p1.desconto(10)   # Aplicando 10% de desconto
print(p1.nome, p1.preco)   # Saida: 45.0n

p2 = Produto('CANECA', 'R$15')
p2.desconto(10)
print(p2.nome, p2.preco)
