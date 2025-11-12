"""
Threadler race-condition durumu
"""
from threading import Thread
deger = 0
def artir():
    global deger
    for _ in range(10_000_000):
        deger += 10

threadler = []
for _ in range(2):
    t = Thread(target=artir, args=())
    threadler.append(t)
for j in threadler:
    j.start()
for j in threadler:
    j.join()

print(f"Son deger: {deger}")