import multiprocessing
import time
from multiprocessing import Process
# Process ile yapılan örnekte liste değişmez! Bunun için ortak bellek alanı değeri tanımlıyoruz.
def liste_yaz(liste):
    while True:
        print(*liste, sep=",")
        time.sleep(1)

if __name__ == '__main__':
    liste = multiprocessing.Array("i", [0] * 10, lock=True)
    t1 = Process(target=liste_yaz, args=(liste, ))
    t1.start()
    for i in range(10):
        time.sleep(2)
        for j in range(10):
            liste[j] = i