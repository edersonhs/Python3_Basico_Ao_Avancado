from random import randint

class Pessoa:
    ano_atual = 2019   # Atributo de classe  /  Esta disponivel pela classe

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    

    def get_ano_nascimento(self):
        print(self.ano_atual - self.idade)
    
    # Factory mode - Fabrica internamente o objeto da classe
    @classmethod   # Decorando o metodo como um metodo de classe
    def por_ano_nascimento(cls, nome, ano_nascimento):   # Quando refere-se a classe, utiliza-se "cls", por convenção.   *Não é uma referencia a instancia.  Ps: Pode ser qualquer nome.
        """
        Cria uma pessoa por ano de nascimento
        """
        idade = cls.ano_atual - ano_nascimento

        return cls(nome, idade)   # Retorna o objeto da da propria classe baseado nos parametros passados. É semelhante ao que foi feito no escopo global. EX: p1 = Pessoa('Luiz', 32)
        # cls(nome, idade) esta executando a classe Pessoa
    
    @staticmethod
    def gera_id():   # Pode receber parametros, mas não recebe a classe ou instancia
        rand = randint(1, 100)
        return rand



p1 = Pessoa('Luiz', 32)
print(p1.idade)
p1.get_ano_nascimento()

print()

p2 = Pessoa.por_ano_nascimento('João', 1987)   # Retorna Pessoa(nome, idade)
print(p2)   # <__main__.Pessoa object at 0x000001E906571F10>   / __main__ = Nme do modulo   /   Pessoa = Nome da classe   /   object at 0x000001E906571F10 = Local do objeto na memoria
print(p2.nome, p2.idade)   # João 32
p2.get_ano_nascimento()   # 1987

print()

print(Pessoa.gera_id())
print(p1.gera_id())   # Caso seja necessario, é possivel chamar o metodo estatico pela instancia também

"""
Método de instancia: precisam de uma instancia para funcionar

Método de classe: não precisa da instancia mas sim a classe em sí

Metodo Estatico: não precisa nem da instancia nem da classe, tanto que a classe e a instancia não podem ser referenciados nele,
* É como uma função normal que por questões de organização ficou na classe
"""
