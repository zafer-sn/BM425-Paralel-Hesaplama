import math
# region Dizi örneği
# import array
# print(array.array("i", [1, 2, 3, "selam"])) -> Hata!
# endregion
"""
Değişken tanımlama gelenekleri
pi_sayisi -> snake_case
piSayisi -> camelCase
PiSayisi -> PascalCase
+ -> Toplama
- -> Çıkarma
* -> Çarpma
/ -> Bölme
% -> Mod alma
** -> üs alma
"""
# region Değer tipli değişken
yas = 30
pi_sayisi = 3.14
giris_yapildimi = True
isim_soyisim = "Zafer SERİN"
# endregion
# region type classı ve math modülü
print(type(yas))
print(2 ** 3)
print(math.pow(2, 3))
# endregion
# print(isim_soyisim[0])
# immutable -> değiştirilemez
isim_soyisim = "ahmet YILMAZ"
print(isim_soyisim)
# isim_soyisim[0] = "D" -> Hata!
print(isim_soyisim)
print(type(isim_soyisim.split()))
# region Listeler - Referans tipler
# meyveler = ["elma", "armut", "ayva", 11, 3.14, False]
# print(meyveler[-1])
meyveler = ["elma", "armut", "ayva"]
sebzeler = ["domates", "salatalik", "biber"]
meyveler = sebzeler
meyveler[0] = "cilek"
sebzeler[1] = "patlican"
meyveler[2] = "portakal"
print(meyveler)
print(sebzeler)
# endregion
