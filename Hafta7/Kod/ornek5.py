from threading import Condition, Thread
import time


liste = []
cv = Condition()

"""def kontrol():
    return len(liste) > 0"""

kontrol = lambda : len(liste) > 0

def listeye_ekle():
    print("3 saniye sonra ekliyorum...")
    time.sleep(3)
    with cv:
        liste.append("veri")
        cv.notify()     

def listeyi_isle():
    with cv:
        cv.wait_for(kontrol)
    print("Liste islendi!")

t1 = Thread(target=listeye_ekle, args=())
t2= Thread(target=listeyi_isle, args=())
t1.start()
t2.start()
t1.join()
t2.join()