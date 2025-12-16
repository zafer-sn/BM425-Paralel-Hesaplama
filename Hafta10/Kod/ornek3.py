import ctypes
from multiprocessing import Process
import multiprocessing
from threading import Thread
import time


def listeyi_yazdir(liste):
    while True:
        print(*liste, sep=",")
        time.sleep(1)

if __name__ == "__main__":
    liste = multiprocessing.Array(ctypes.c_int, [-1]*10)
    p1 = Process(target=listeyi_yazdir, args=(liste, ))
    p1.start()
    for j in range(10):
        time.sleep(2)
        for i in range(10):
            liste[i] = j