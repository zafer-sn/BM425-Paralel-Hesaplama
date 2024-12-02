# Condition Variables(Koşul Değişkenleri)
import time
from threading import Thread, Lock, Condition
class StingySpendy():
    money = 0
    cv = Condition()
    def Stingy(self):
        for i in range(10000000):
            self.cv.acquire()
            self.money += 10
            self.cv.notify_all()
            self.cv.release()
    def Spendy(self):
        for i in range(10000000):
            self.cv.acquire()
            # Spurious wakeup
            """if self.money < 10:
                self.cv.wait()"""
            while self.money < 10:
                self.cv.wait()
            self.money -= 10
            if self.money < 0:
                print(f"Money is negative: {self.money}")
            self.cv.release()
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

"""
cv1 -> while wait
cv2 -> if wait
cv2.notfiy_all()
"""




