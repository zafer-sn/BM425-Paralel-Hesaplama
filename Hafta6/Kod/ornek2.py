"""
Threadler race-condition durumu
Mutex
"""
from threading import Lock, Thread
deger = 0
mtx = Lock()
def artir():
    global deger, mtx
    for _ in range(10_000_000):
        mtx.acquire()
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