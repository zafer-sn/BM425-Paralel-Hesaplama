def faktoriyel(sayi):
    if sayi < 0:
        raise ValueError("Hata!")
    if sayi == 0:
        return 1
    return sayi * faktoriyel(sayi-1)

print(faktoriyel(-5))

try:
    print(1/0)
except Exception as e:
    print(e)