# Condition Variables(Koşul Değişkenleri)
import time
from threading import Thread, Lock
class StingySpendy():
    money = 0
    mutex = Lock()
    def Stingy(self):
        self.mutex.acquire()
        for i in range(10000000):
            self.money += 10
        self.mutex.release()
    def Spendy(self):
        self.mutex.acquire()
        for i in range(10000000):
            self.money -= 10
        self.mutex.release()
ss = StingySpendy()
t1 = Thread(target=ss.Spendy)
t2 = Thread(target=ss.Stingy)
start = time.time()
t1.start()
t2.start()
t1.join()
t2.join()
finish = time.time()

print(ss.money)
print(f"Elapsed time: {finish-start}")
