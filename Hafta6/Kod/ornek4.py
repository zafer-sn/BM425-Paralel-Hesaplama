class Banka():
    para = 100
    def kazan(self):
        for _ in range(10_000_000):
            self.para += 10
    def harca(self):
        for _ in range(10_000_000):
            self.para -= 10

b1 = Banka()
b1.kazan()
b1.harca()
print(f"Kalan deger: {b1.para}")