import math
from multiprocessing import Process
import multiprocessing
import os
import random
from threading import Thread
import time
from numba import njit, prange

toplam_nokta_sayisi = 120_000_000
@njit(parallel=True)
def pi_sayisi(adet):
    yerel_icerideki_nokta_sayisi = 0
    for _ in prange(adet):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        r = math.sqrt(x**2 + y**2)
        if r <= 1:
            yerel_icerideki_nokta_sayisi += 1
    return yerel_icerideki_nokta_sayisi
if __name__ == "__main__":
    # print(os.cpu_count())
    baslangic_zamani = time.time()
    sonuc = pi_sayisi(toplam_nokta_sayisi)
    pi = 4 * sonuc/toplam_nokta_sayisi
    bitis_zamani = time.time()

    print(f"Pi degeri: {pi}, Gecen sure: {bitis_zamani-baslangic_zamani}")
