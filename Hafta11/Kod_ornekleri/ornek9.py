import time
from threading import Thread
# Thread ile yapılan örnekte liste değişir!

def liste_yaz(liste):
    while True:
        print(*liste, sep=",")
        time.sleep(1)

liste = [0] * 10
t1 = Thread(target=liste_yaz, args=(liste, ))
t1.start()
for i in range(10):
    time.sleep(2)
    for j in range(10):
        liste[j] = i