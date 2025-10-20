def asal(sayi):
    if sayi < 2:
        raise ValueError("Tanimsiz sayi!")
    gelen_sayi_asalmi = True
    for i in range(2, sayi):
        if sayi % i == 0:
            gelen_sayi_asalmi = False
            break
    return gelen_sayi_asalmi

l = list(range(2, 10000))
f = list(filter(asal, l))
print(f)
# print(asal(-5))
# palindrome - 1221, 5335