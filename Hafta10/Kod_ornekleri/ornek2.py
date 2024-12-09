# Semafor -> kilit, daha yönetilebilir.
# Semafor bir kaynağa aynı anda erişebilecek Thread sayısını belirlememizi sağlayan
# senkronizasyon yöntemidir.
import time
from threading import Semaphore, Thread
# BoundedSemaphore() -> Maksimum thread sayısının aşılmasına asla! izin vermez
semafor = Semaphore(2)
def otopark(arac):
    print(f"{arac} otoparka giriş yapmak istiyor.")
    semafor.acquire()
    print(f"{arac} otoparka giriş yaptı ve bekliyor.")
    time.sleep(2)
    print(f"{arac} otoparktan çıkış yapıyor")
    semafor.release()

araclar = ["opel", "mazda", "bmw", "mercedes", "honda"]
threadler = []
for i in araclar:
    t = Thread(target=otopark, args=(i, ))
    threadler.append(t)

for j in threadler:
    j.start()
for j in threadler:
    j.join()
print("Tüm araçlar otoparktan çıktı")






