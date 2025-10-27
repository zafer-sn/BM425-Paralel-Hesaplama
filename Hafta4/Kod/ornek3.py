from threading import Thread
import time

def is_yap():
    print("is basladi")
    time.sleep(1)
    print("is bitti")

for _ in range(5):
    t = Thread(target=is_yap, args=())
    t.start()