from multiprocessing import Process
from threading import Thread
import time

def is_yap():
    print("is basladi")
    # time.sleep(1)
    i = 0
    for _ in range(200000000):
        i+=1
    print("is bitti")

baslangic_zamani = time.time()
"""for _ in range(5):
    is_yap()"""
liste = []
for _ in range(5):
    t = Process(target=is_yap, args=())
    liste.append(t)
for j in liste:
    j.start()
for j in liste:
    j.join()
bitis_zamani = time.time()
print(f"Gecen sure: {bitis_zamani-baslangic_zamani}")