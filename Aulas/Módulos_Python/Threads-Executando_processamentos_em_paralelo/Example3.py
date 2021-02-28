from threading import Thread
from time import sleep


def slower(text, time):
    sleep(time)
    print(text)


t1 = Thread(target=slower, args=('Hello from Thread 1!', 10))
t1.start()   # Starting subthread

# Juntando a subthread com a main thread
t1.join()
# Desta forma a main thread vai aguardar o fim da subthread para continuar.

# Running on main thread
while t1.is_alive():   # Enquanto a thread estiver ativa...
    print('Waiting for the Thread...')
    sleep(2)

print('Threads is over!')
