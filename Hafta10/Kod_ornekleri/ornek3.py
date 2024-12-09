import time
from threading import Barrier, Thread, BrokenBarrierError

bariyer = Barrier(2)
def bariyerde_bekle(isim, bekleme_suresi):
    print(f"{isim} çalışmaya başladı")
    time.sleep(bekleme_suresi)
    print(f"{isim} bariyerde bekliyor")
    try:
        bariyer.wait()
    except BrokenBarrierError:
        print("test")

    print(f"{isim} bariyeri geçti")

kirmizi = Thread(target=bariyerde_bekle, args=("kirmizi", 4))
mavi = Thread(target=bariyerde_bekle, args=("mavi", 10))

kirmizi.start()
mavi.start()
time.sleep(8)
bariyer.abort()
kirmizi.join()
mavi.join()
print("Tamamlandı")


