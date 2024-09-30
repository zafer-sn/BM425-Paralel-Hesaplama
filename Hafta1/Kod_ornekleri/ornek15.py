# 1 1 2 3 5 8 13 ...
deger1 = 1
deger2 = 1
print(deger1)
print(deger2)
deger_sayisi = int(input("Kaç sayı yazılsın..:"))
for i in range(1, deger_sayisi-1):
    deger3 = deger1 + deger2
    deger1 = deger2
    deger2 = deger3
    print(deger3, end="-")
    # deger2 = deger1