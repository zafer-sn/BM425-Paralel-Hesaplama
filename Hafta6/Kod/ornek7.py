"""
Aynı kilidi aynı thread birden çok kez alirsa
"""
from threading import Lock, RLock, Thread


mtx = RLock()
def rekursif(n):
    if n < 0:
        return
    print(f"{n} kilidi almaya calisiyor...")
    with mtx:
        print(f"{n} kilidi aldi...")
        rekursif(n-1)
    print(f"{n} kilidi birakti...")

t = Thread(target=rekursif, args=(3, ))
t.start()
t.join()