from time import sleep
from threading import Thread


class MyThread(Thread):
    def __init__(self, text, time):
        self.text = text
        self.time = time

        super().__init__()   # Executando o init da classe Thread (herdada)

    def run(self):   # Sobrescrevendo run de Thread
        sleep(self.time)
        print(self.text)


# Criando e executando subthreads
# (será executado independemente do que ocorre na main thread)
t1 = MyThread('Hello From Thread 1', 5)   # Instanciando
t1.start()   # Iniciando a Thread

t2 = MyThread('Hello From Thread 2', 3)   # Instanciando
t2.start()   # Iniciando a Thread

t3 = MyThread('Hello From Thread 3', 2)   # Instanciando
t3.start()   # Iniciando a Thread


# Main Thread
for i in range(20):
    print(i)
    sleep(1)
