'''
# Funções como variáveis
def fala_oi():
    print('Oi')


# A variável é igual a função/ Torna-se a função
variavel = fala_oi
print(type(variavel))  # function
variavel()  # Oi
'''

'''
# Uma função dentro de outra
def master():
    # Função interna
    def slave():
        print('Oi')
    # Função a ser executada
    return slave   # a função master retorna a função Slave, ou seja, a variavel recebera a função slave

variavel = master()   # Variável recebe função slave
variavel()   # Executa a função interna de master
'''

'''
# Função como parâmetro
def master(funcao):
    # Função interna
    def slave():
        # executa a função enviada
        funcao()
    # Retorna a função interna sem executar
    return slave

# Função de exemplo
def fala_oi():
    print('Oi')

variavel = master(fala_oi)   # Passando a função de exemplo como parametro para a master
variavel() # Executa a variável/função que retornaria umm'Oi'
'''

'''
# Recebe uma função
def master(funcao):
    # Cria uma função interna
    def slave():
        # Decora
        print('Estou decorada.')
        # Executa a função enviada
        funcao()
    # Retorna a função interna sem executar
    return slave

# Uma função qualquer
def fala_oi():
    print('Oi')

# Decorando
fala_oi = master(fala_oi)   # Apóes decorar, a função fala oi para a executar o conteudo lá da slave que esta no master
fala_oi()
'''

'''
# Função decoradora
def master(funcao):
    def slave():
        print('Estou decorada.')
        funcao()
    return slave

# Sintax sugar do decorador
@master   #  DECORADOR - Decora a função fala_oi com a função decoradora master
def fala_oi():
    print('Oi')

fala_oi()
'''

'''
# Decorando com parâmetros
def master(funcao):
    def slave(*args, **kwargs):
        print('Estou decorada.')
        funcao(*args, **kwargs)
    return slave

@master
def fala_oi(msg):
    print(msg)


fala_oi('Olá, sou Luiz')
'''

from time import time
from time import sleep


def velocidade(funcao):
    """
    Função decoradora: Verifica o tempo que uma função leva para executar
    """
    def envolve(*args, **kwargs):
        """ Função que envolve e executa outra função """
        # Tempo inicial
        start = time()   # Pega o tempo atual
        # Executa a função
        resultado = funcao(*args, **kwargs)   # executa a função demora()
        # Tempo final
        end = time()   # Pega o tempo atual
        # Resultado de tempo em ms
        tempo = (end - start) * 1000   # * 1000 para converter para ms
        # Mostra o tempo
        print(f'\nA função {funcao.__name__} levou {tempo:.2f}ms para ser executada.')
        # Retorna a função original executada
        return resultado
    # Retorna a função que envolve
    return envolve


@velocidade
def demora(qtd):
    """ Função decorada """
    for i in range(qtd):
        print(i, end='')

print()
# Executa a função decorada
demora(100)
