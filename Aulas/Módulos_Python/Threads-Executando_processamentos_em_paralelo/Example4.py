from threading import Thread
from threading import Lock
from time import sleep

"""
Quando se utiliza threads e manipula dados ao mesmo tempo, um grande problema
pode ocorrer devido a falta de sincronia.
"""


class Ingressos:
    def __init__(self, estoque) -> None:
        self.estoque = estoque
        self.lock = Lock()   # Instanciando Lock

    def comprar(self, quantidade):
        # Sempre que qualquer thread entre no método, ele será trancado para
        # que outras não o acessem
        self.lock.acquire()   # Trancando o método internamente

        if self.estoque < quantidade:
            print('Não temos ingressos suficientes.')
            self.lock.release()
            return

        sleep(1)   # Sem o lock as threads vão aguardar aqui por um segundo.
        # Como todas as threads já estão após a verificação de estoque,
        # mesmo que o estoque esteja menor que zero, será subtraida
        # a quantidade como se ainda houvesse estoque.

        self.estoque -= quantidade

        print(
            f'Você comprou {quantidade} ingresso(s). '
            f'Ainda temos {self.estoque} em estoque.')

        # Destrancando o método internamente para a proxima thread
        self.lock.release()


if __name__ == '__main__':
    ingressos = Ingressos(10)

    for i in range(1, 20):
        """
        Enquanto a subthread executa a classe, a mainthread vai para o proximo
        laço e inicia outra subthread para executar a classe também, e assim
        por diante.
        """
        t = Thread(target=ingressos.comprar, args=(i,))
        t.start()

    # Esta sendo executado antes do for por que as threads estão aguradando um
    # segundo no método comprar. (Solução no exemplo 5)
    print(ingressos.estoque)
