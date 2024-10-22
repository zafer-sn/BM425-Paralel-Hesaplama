import os
import time
from threading import Thread


def is_yap():
    print("İş başladı")
    time.sleep(1)
    print("İş bitti")

for i in range(8):
    thr1 = Thread(target=is_yap())
    thr1.start()