import math
from multiprocessing import Process
import multiprocessing
import os
import random
from threading import Thread
import time

icerideki_nokta_sayisi = multiprocessing.Value("i", 0)
# print(type(icerideki_nokta_sayisi))
toplam_nokta_sayisi = 10_000_000
def pi_sayisi(icerideki_nokta_sayisi):
    yerel_icerideki_nokta_sayisi = 0
    for _ in range(toplam_nokta_sayisi):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        r = math.sqrt(x**2 + y**2)
        if r <= 1:
            yerel_icerideki_nokta_sayisi += 1
    with icerideki_nokta_sayisi.get_lock():
        icerideki_nokta_sayisi.value += yerel_icerideki_nokta_sayisi
if __name__ == "__main__":
    # print(os.cpu_count())
    baslangic_zamani = time.time()
    threadler = []
    thread_sayisi = 12
    for i in range(thread_sayisi):
        t = Process(target=pi_sayisi, args=(icerideki_nokta_sayisi, ))
        threadler.append(t)
    for j in threadler:
        j.start()
    for j in threadler:
        j.join()
    pi = 4 * icerideki_nokta_sayisi.value/(toplam_nokta_sayisi * thread_sayisi)
    bitis_zamani = time.time()

    print(f"Pi degeri: {pi}, Gecen sure: {bitis_zamani-baslangic_zamani}")
