class Musteri():
    def __init__(self, isim, bakiye):
        self.isim = isim
        self.__bakiye = bakiye
    
    def get_bakiye(self):
        return self.__bakiye * 2
    
    def set_bakiye(self, deger):
        self.__bakiye = deger * 3


m1 = Musteri("Zafer", 10000)
m1.set_bakiye(5000)
print(m1.get_bakiye())