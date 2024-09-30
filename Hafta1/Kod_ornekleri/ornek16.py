deger = int(input("Lütfen değer giriniz..:"))
asalmi = True
for i in range(2, deger):
    if deger % i == 0:
        asalmi = False
        break
    else:
        asalmi = True
print(asalmi)