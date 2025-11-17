from threading import Condition, Thread


cv = Condition()
sira = 3
def gorev1():
    global sira
    with cv:
        while sira != 1:
            cv.wait()
        print("T1 basladi")
        print("T1 bitti")
        sira = 2
        cv.notify_all()
def gorev2():
    global sira
    with cv:
        while sira != 2:
            cv.wait()
        print("T2 basladi")
        print("T2 bitti")
        
def gorev3():
    global sira
    with cv:
        while sira != 3:
            cv.wait()
        print("T3 basladi")
        print("T3 bitti")
        sira = 1
        cv.notify_all()

t1 = Thread(target=gorev1, args=())
t2 = Thread(target=gorev2, args=())
t3 = Thread(target=gorev3, args=())
t1.start()
t2.start()
t3.start()
t1.join()
t2.join()
t3.join()

