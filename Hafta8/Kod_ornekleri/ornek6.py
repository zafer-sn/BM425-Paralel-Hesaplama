import time
from threading import Thread, Lock
#Race Condition(Yarış Durumu - Yarış Koşulu)
bakiye = 100
def artir(mtx):
    for _ in range(1000000):
        mtx.acquire()
        global bakiye
        bakiye += 10
        mtx.release()
    print("Artirma bitti")

def azalt():
    for _ in range(1000000):

        global bakiye
        bakiye -= 10

    print("Azaltma bitti")
mutex = Lock()

t1 = Thread(target=artir, args=(mutex, ))
t2 = Thread(target=azalt)
t1.start()
t2.start()
time.sleep(5)
print(bakiye)