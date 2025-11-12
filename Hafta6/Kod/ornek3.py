"""
Threadler race-condition durumu
Mutex - kullanimi
"""
from threading import Lock, Thread
deger = 0
mtx = Lock()
def artir():
    global deger, mtx
    mtx.acquire()
    for _ in range(10_000_000):        
        deger += 10
    mtx.release()

threadler = []
for _ in range(2):
    t = Thread(target=artir, args=())
    threadler.append(t)
for j in threadler:
    j.start()
for j in threadler:
    j.join()

print(f"Son deger: {deger}")