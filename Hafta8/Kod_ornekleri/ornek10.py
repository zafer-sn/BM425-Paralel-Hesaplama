import time
from threading import Thread


def parent():
    t = Thread(target=child)
    t.start()
    t.join()
    print("Parent çalıştı")

def child():
    print("Child çalışıyor")
    time.sleep(1)
    print("Child bitti")

parent()