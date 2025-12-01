from threading import Barrier, Thread
import time

bry = Barrier(2)
def bariyerde_bekle(isim, sure):
    for _ in range(10):
        print(f"{isim} threadi basladi....")
        time.sleep(sure)
        print(f"{isim} threadi bariyerde bekliyor...")
        bry.wait()

kirmizi = Thread(target=bariyerde_bekle, args=("kirmizi", 4))
mavi = Thread(target=bariyerde_bekle, args=("mavi", 10))

kirmizi.start()
mavi.start()

#time.sleep(8)
#bry.abort()

kirmizi.join()
mavi.join()