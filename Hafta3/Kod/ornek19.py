class Ogrenci():
    def __init__(self, isim, soyisim):
        self.isim = isim
        self.soyisim = soyisim
        self.tam_isim = isim + " " + soyisim

ogr1 = Ogrenci("Zafer", "SERİN")
ogr1.isim = "Ahmet"
print(ogr1.tam_isim)