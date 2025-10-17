import numpy as np
rastgele = np.random.randint(0, 100)
sayac = 0
while True:
    tahmin = int(input("Lütfen tahmininizi giriniz..:"))
    sayac += 1
    if tahmin == rastgele:        
        print("Tahmin dogru")
        break
    elif tahmin > rastgele:        
        print("Daha kucuk bir deger giriniz!")
    else:        
        print("Daha buyuk bir deger giriniz!")
print(f"{sayac} kadar tahminde dogru degeri buldunuz!")