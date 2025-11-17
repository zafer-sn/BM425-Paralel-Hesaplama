from threading import Condition, Thread
import time
sinyal = False
cv = Condition()

def veriyi_hazirla():
    global sinyal
    print("Veri 5 saniye sonra hazir!")
    time.sleep(5)
    with cv:
        print("Veri hazir!")
        sinyal = True
        cv.notify()

def veriyi_isle():
    with cv:
        while not sinyal:
            print("Verinin hazirlanmasini bekliyorum...")
            cv.wait()
    print("Veri islendi!")

t1 = Thread(target=veriyi_hazirla, args=())
t2 = Thread(target=veriyi_isle, args=())
t1.start()
t2.start()
t1.join()
t2.join()