class Musteri():
    def __init__(self, yas):
        self.yas = yas
    
    @property
    def yas(self):
        return self._yas

    @yas.setter
    def yas(self, deger):
        self._yas = deger

m1 = Musteri(30)
m1._yas = 50
print(m1._yas)