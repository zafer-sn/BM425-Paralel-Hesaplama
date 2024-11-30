def mukemmelmi(sayi):
    mukemmel = True
    toplam = 0
    for i in range(1, sayi):
        if sayi % i == 0:
            toplam += i
    if toplam == sayi:
        return True
    else:
        return False

liste = []
for i in range(1, 10001):
    if mukemmelmi(i) == True:
        liste.append(i)
print(*liste)


