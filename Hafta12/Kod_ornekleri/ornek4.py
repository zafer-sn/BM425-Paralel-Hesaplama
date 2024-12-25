import math
import multiprocessing
import random
import time
from multiprocessing import Process

# print(math.pi)

baslangic_zamani = time.time()
toplam_nokta_sayisi = 100000000//8
def prcs(icerideki_nokta_sayisi):
    yerel_icerideki_nokta_sayisi = 0
    for _ in range(toplam_nokta_sayisi):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if (x**2 + y**2) <= 1:
            yerel_icerideki_nokta_sayisi += 1
    icerideki_nokta_sayisi.value += yerel_icerideki_nokta_sayisi

if __name__ == '__main__':
    icerideki_nokta_sayisi = multiprocessing.Value("i", 0, lock=True)
    # MPI(Message Passing)
    # print(type(icerideki_nokta_sayisi))
    # print(icerideki_nokta_sayisi.value)
    process_sayisi = 8
    process_listesi = []
    for i in range(process_sayisi):
        p = Process(target=prcs, args=(icerideki_nokta_sayisi, ))
        process_listesi.append(p)
    for j in process_listesi:
        j.start()
    for j in process_listesi:
        j.join()
    PI = (4*icerideki_nokta_sayisi.value)/(toplam_nokta_sayisi*8)
    print(f"Bulunan değer: {PI}, Geçen süre: {time.time()-baslangic_zamani}")


    # print(x)
    # print(f"{x:.4f}")