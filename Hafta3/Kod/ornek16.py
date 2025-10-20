class Ogrenci():
    def __init__(self, isim, yas):
        self.isim = isim
        self.yas = yas
    def bilgi_ver(self):
        return f"Ogrencinin ismi: {self.isim}, Ogrencinin yasi: {self.yas}"

ogr1 = Ogrenci("Ahmet", 20)
print(ogr1.bilgi_ver())