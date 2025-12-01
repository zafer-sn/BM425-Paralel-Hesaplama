from threading import Barrier, Thread
import time
def son_islem():
    print("Bariyer kirildi, son işlem!")
    print("-" * 50)
thread_sayisi = 4
bry = Barrier(thread_sayisi, action=son_islem)

def bariyerde_bekle(isim):
    for i in range(10):
        print(f"{isim} veriyi yukluyor...")
        time.sleep(1 + (isim * 0.5))
        bry.wait()
        print(f"{isim} bariyeri gecti!")

threadler = []
for i in range(thread_sayisi):
    t = Thread(target=bariyerde_bekle, args=(i, ))
    threadler.append(t)

for j in threadler:
    j.start()
for j in threadler:
    j.join()
