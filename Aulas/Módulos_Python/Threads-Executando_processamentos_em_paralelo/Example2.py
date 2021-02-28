from threading import Thread
from time import sleep


def slower(text, time):
    sleep(time)
    print(text)


# Instanciando Thread com a função criada anteriormente
# Se tiver só um argumento, inserir uma virgula porteirior ao mesmo
t1 = Thread(target=slower, args=('Hello from Thread 1!', 5))
t2 = Thread(target=slower, args=('Hello from Thread 2!', 1))
t3 = Thread(target=slower, args=('Hello from Thread 3!', 2))

# Iniciando as subthreads
t1.start()
t2.start()
t3.start()

# Ecutando na Main Thread
for i in range(20):
    print(i)
    sleep(.5)
