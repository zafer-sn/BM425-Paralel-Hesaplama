from threading import RLock

mtx = RLock()
def fonk1():
    mtx.acquire()
    print("Fonksiyon1 başladı")
    fonk2()
    print("Fonksiyon1 bitti")
    mtx.release()

def fonk2():
    mtx.acquire()
    print("Fonksiyon2 başladı")
    print("Fonksiyon2 bitti")
    mtx.release()

fonk1()