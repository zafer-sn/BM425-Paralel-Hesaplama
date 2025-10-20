class Ogrenci():
    def __init__(self, isim, soyisim, yas):
        self.isim = isim
        self.soyisim = soyisim
        self.yas = yas
    
    def bilgi_ver(self):
        print(f"İsmi: {self.isim}, soyismi: {self.soyisim}, yasi: {self.yas}")

class UniversiteOgrencisi(Ogrenci):
    def __init__(self, isim, soyisim, yas):
        # super().__init__(isim, soyisim, yas)
        Ogrenci.__init__(self, isim, soyisim, yas)
        print("Universite Ogrencisi nesnesi olusturuldu")

uo = UniversiteOgrencisi("Zafer", "SERİN", 30)
uo.bilgi_ver()

"""class ysa(nn.Module)
    def __init__(self):
        super().__init__()"""

