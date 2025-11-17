from threading import Condition, Thread
import time


class Banka():
    def __init__(self, para = 100, cv = Condition()):
        self.para = para
        self.cv = cv
    def kazan(self):
        for _ in range(100_000):
            with self.cv:
                p = self.para
                time.sleep(0)
                p += 10
                self.para = p
                self.cv.notify()
            
    def harca(self):
        for _ in range(100_000):
            with self.cv:
                while (self.para < 10):
                    print(f"Para Harcayamazsin!: {self.para}")
                    self.cv.wait()
                p = self.para
                time.sleep(0)
                p -= 10
                self.para = p

b1 = Banka()
t1 = Thread(target=b1.kazan, args=())
t2 = Thread(target=b1.harca, args=())
t1.start()
t2.start()
t1.join()
t2.join()
print(f"Kalan para: {b1.para}")