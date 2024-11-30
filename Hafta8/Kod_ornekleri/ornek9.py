import time
from threading import Thread


def is_yap():
    print("İş başladı")
    time.sleep(2)
    print("İş bitti")

t1 = Thread(target=is_yap)
t2 = Thread(target=is_yap)
t1.start()
t1.join()

t2.start()
print("Selam")
t2.join()