from threading import Thread
import time


def is_yap():
    print("is basladi")
    time.sleep(0.5)
    print("is bitti")

t1 = Thread(target=is_yap, args=())
t2 = Thread(target=is_yap, args=())
t1.start()
t2.start()
t1.join()
t2.join()