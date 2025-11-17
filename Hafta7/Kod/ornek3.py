from threading import Condition, Thread
import time


cv = Condition()
sinyal = False

def basla(isim):
    print(f"{isim} baslangic noktasinda bekliyor...")
    with cv:
        while not sinyal:
            cv.wait()
    print(f"Yaris Bitti {isim}")

threadler = []
for i in range(3):
    t = Thread(target=basla, args=(i, ))
    threadler.append(t)

for j in threadler:
    j.start()

print("3 saniye sonra yaris basliyor...")
time.sleep(3)
with cv:
    sinyal = True
    cv.notify_all()

for j in threadler:
    j.join()

