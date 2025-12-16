import math
import random
from threading import Thread
import time

icerideki_nokta_sayisi = 0
toplam_nokta_sayisi = 10_000_000
def pi_sayisi():
    global icerideki_nokta_sayisi
    for _ in range(toplam_nokta_sayisi):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        r = math.sqrt(x**2 + y**2)
        if r <= 1:
            icerideki_nokta_sayisi += 1
baslangic_zamani = time.time()
threadler = []
thread_sayisi = 12
for i in range(thread_sayisi):
    t = Thread(target=pi_sayisi)
    threadler.append(t)
for j in threadler:
    j.start()
for j in threadler:
    j.join()
pi = 4 * icerideki_nokta_sayisi/(toplam_nokta_sayisi * thread_sayisi)
bitis_zamani = time.time()

print(f"Pi degeri: {pi}, Gecen sure: {bitis_zamani-baslangic_zamani}")
