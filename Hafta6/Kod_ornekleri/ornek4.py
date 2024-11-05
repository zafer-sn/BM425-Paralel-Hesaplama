import time


def asal_sayi_bul(sayi):
    asalmi = True
    for i in range(2, sayi):
        if sayi % i == 0:
            asalmi = False
            break
    return asalmi

bas_zamani = time.time()
for i in range(2, 100001):
    asal_sayi_bul(i)
bit_zamani = time.time()
print(f"Geçen süre: {bit_zamani-bas_zamani}")

