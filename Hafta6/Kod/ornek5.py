from threading import Lock, Thread


class Banka():
    para = 100
    mtx = Lock()
    def kazan(self):
        with self.mtx:
            for _ in range(10_000_000):
                self.para += 10
    def harca(self):
        with self.mtx:
            for _ in range(10_000_000):
                self.para -= 10

b1 = Banka()
t1 = Thread(target=b1.kazan, args=())
t2 = Thread(target=b1.harca, args=())
t1.start()
t2.start()
t1.join()
t2.join()
print(f"Kalan deger: {b1.para}")