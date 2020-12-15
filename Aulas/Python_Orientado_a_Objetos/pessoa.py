"""
Classe é como um "Molde"
"""
from datetime import datetime

class Pessoa:
    ano_atual = int(datetime.strftime(datetime.now(), '%Y'))   # Variavel da Classe em sí
    # Mesmo para utilizar uma variavel da classe em sí em um método, é necessario usar o "self". Ou seja, seria self.ano_atual

    # Criando um método.   [ MÉTODO é uma função que pertence a esta classe.]
    # # def falar(self):   # self recebe a instancia que esta chamando a classe. Se no main houver um p1.falar(), self receberia "p1". Serve para que o insterpretador do python entenda de qual instancia o codigo se refere.
    # #     print('Pessoa esta falando...')
    
    def __init__(self, nome, idade, comendo=False, falando=False):   # __init__ é um método especial do Python. Recebe os parametros passados dendro dos parenteses da classe, exemplo: linha 4 do main. p1 = Pessoa(Parametros_Que_O_Init_Recebe_AQUI)
        self.nome = nome   # "instancia.nome = nome" é o mesmo que "p1.nome = nome"
        self.idade = idade
        self.comendo = comendo
        self.falando = falando
       
        # variavel = 'Valor'   # Cria uma variavel valida que existe apenas dentro deste método
        # print(variavel)   # Seria executado quando p1 é instanciado no main (p1 = Pessoa())

    # def outro_metodo(self):
    #     print(self.nome)   # as variaveis definidas lá no __init__ com o self estão disponiveis em todos os métodos.


    def falar(self, assunto):
        if self.comendo:
            print(f'{self.nome} não pode falar comendo.')
            return

        if self.falando:
            print(f'{self.nome} já está falando.')
            return
        
        print(f'{self.nome} esta falando sobre {assunto}.')
        self.falando = True
    

    def parar_falar(self):
        if not self.falando:
            print(f'{self.nome} não esta falando.')
            return
        
        print(f'{self.nome} parou de falar.')
        self.falando = False


    def comer(self, alimento):
        if self.comendo:   # Impede que a mesma pessoa coma enquanto já estiver comendo.
            print(f'{self.nome} já está comendo.')
            return   # Para aqui
        
        if self.falando:
            print(f'{self.nome} não pode comer enquanto fala.')
            return
        
        print(f'{self.nome} está comendo {alimento}.' )
        self.comendo = True


    def parar_comer(self):
        if not self.comendo:
            print(f'{self.nome} não está comendo.')
            return
        
        print(f'{self.nome} parou de comer.')
        self.comendo = False

    def get_ano_nascimento(self):
        return self.ano_atual - self.idade   # Mesmo para utilizar uma variavel da classe em sí em um método, é necessario usar o "self"
