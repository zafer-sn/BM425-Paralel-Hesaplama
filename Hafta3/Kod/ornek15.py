class Ogrenci():
    """isim = ""
    yas = 0"""
    def __init__(self, isim, yas):
        self.isim = isim
        self.yas = yas
        print("Ogrenci nesnesi olusturuldu")

ogr1 = Ogrenci("Zafer", 30)
print(ogr1.isim)
ogr2 = Ogrenci("Ahmet", 20)
print(ogr2.isim)
     