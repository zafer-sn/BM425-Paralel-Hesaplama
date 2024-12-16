import time
from multiprocessing import Process
from threading import Thread
def liste_yaz(liste):
    while True:
        print(*liste, sep=",")
        time.sleep(1)

if __name__ == '__main__':
    liste = [0] * 10
    t1 = Process(target=liste_yaz, args=(liste, ))
    t1.start()
    for i in range(10):
        time.sleep(2)
        for j in range(10):
            liste[j] = i