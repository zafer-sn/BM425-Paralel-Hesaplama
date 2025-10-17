# 0 1 1 2 3 5 8
"""sayi1 = 0
print(sayi1)
sayi2 = 1
print(sayi2)
for i in range(8):
    sayi3 = sayi1 + sayi2
    print(sayi3)
    sayi1 = sayi2
    sayi2 = sayi3"""

liste1 = [0, 1]
for i in range(8):
    liste1.append(liste1[-1] + liste1[-2])

print(liste1)
