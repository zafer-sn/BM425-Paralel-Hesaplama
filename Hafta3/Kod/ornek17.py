class Musteri():
    def __init__(self, isim, bakiye):
        self.isim = isim
        self.bakiye = bakiye

m1 = Musteri("A", 30)
m2 = Musteri("B", 20)
m1 = m2
m1.isim = "Zafer"
print(m2.isim)