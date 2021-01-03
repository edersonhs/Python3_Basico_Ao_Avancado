"""
Métodos mágicos modificam o comportamento da classe.

A Guide to Python's Magic Methods:
https://rszalski.github.io/magicmethods/
"""


class A:
    # Método mágico responsavel por construir a classe
    def __new__(cls, *args, **kwargs):
        """
        É um contrutor. Quando é definido na classe, precisa ser implementado,
        se não, quando a classe for instanciada não ocorrera nada. O objeto
        instanciado seria uma classe do tipo None E o __init__ não seria
        executado.
        """
        # Cria um atributo de classe logo na contrução da mesma
        cls.nome = 'Luiz Otávio'

        # Define um método logo na contrução da classe
        def haha(*args, **kwargs):   # Vai sempre receber a instancia
            print('Fala OI')

        cls.haha = haha

        print('Eu sou o NEW')   # Executa antes do __init__

        """
        Retorna a classe super e executa o __new__ com a instancia informada
        contida em cls(nesse caso é "a"), super() nesses caso é Object().
        Todas as classes do Python herdam de Object quando não há uma herança
        especifica.
        """
        return super().__new__(cls)

        """
        Caso seja necessario criar uma classe que deverá ser instanciada só
        uma vez, util para recursos de BD que devem ser sincronizados, usamos:
        """
        if not hasattr(cls, '_jaexiste'):
            # Se não existe o atributo _jaexiste, faça:
            cls._jaexiste = super().__new__(cls)   # Cria o atributo _jaexiste

        return cls._jaexiste
        """
        Desta forma caso a classe seja instanciada novamente, o atributo
        receberá a o objeto já instanciado anteriormente.

        Exemplo 1:
        a = A()   # Instancia a classe A pela primeira vez
        b = A()   # Tenta instancias a classe A, mas recebe novamente o obj de
                  # _jaexiste que foi criado quando a foi instanciado
        c = A()   # Novamente recebe _jaexiste

        Exemplo 2:
        print(a == b)   # True, pois as duas instancias são copias de _jaexiste
        """

    # Método mágico que sempre é executado quando a classe é instanciada
    def __init__(self):
        """
        O __init__ costuma ser chamado de contrutor mas não é necessariamente
        um contrutor, pois não é a primeira coisa a ser chamada quando a classe
        é instanciada.
        """
        print('Eu sou o INIT')

    # Faz com que a classe funcione como uma função quando chamada como no EX
    def __call__(self, *args, **keywargs):
        # args = arumentos   |   keywargs = argumentos nomeados
        print(args)
        print(keywargs)

    # Sera chamado toda vez que um novo atributo for configurado na classe
    def __setattr__(self, key, value):
        self.__dict__[key] = value   # Configurando o valor de nome manualmente

        print(key, value)

    # Método magico não recomendado a ser utilizado pela documentação do Python
    def __del__(self):
        """
        Executa sempre que o garbage collector for executado para limpar a
        o objeto. Entretanto não tem utilização recomendada na documentação
        oficial por nãe ser certo que o método será sempre executado.
        """
        print('objeto coletado')   # Será executado no fim da execução

    # Será executado toda vez que a classe for utilizada como uma string
    def __str__(self):
        return 'Essa é a classe A criada para testes!'

    # Será executado quando a função len for utilizada na classe
    def __len__(self):
        return 55


a = A()   # Eu sou o INIT
print(a.nome)   # Luiz Otávio
a.haha()   # Fala OI

# Exemplo do __call__:
a(1, 2, 3, 4, 5, nome='Luiz')  # instancia a funciona como uma função
# Saída:   (1, 2, 3, 4, 5)
#          {'nome': 'Luiz'}

# Exemplo do __setattr__:
a.nome = 'Douglas'   # nome Douglas
print(a.nome)   # Douglas

# Exemplo do __str__:
print(a)   # Essa é a classe A criada para testes!

# Exemplo do __len__:
print(len(a))   # 55
