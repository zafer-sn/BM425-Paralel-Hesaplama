import math
import random
import time


# print(math.pi)

baslangic_zamani = time.time()
toplam_nokta_sayisi = 100000000
icerideki_nokta_sayisi = 0
for _ in range(toplam_nokta_sayisi):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if (x**2 + y**2) <= 1:
        icerideki_nokta_sayisi += 1

PI = (4*icerideki_nokta_sayisi)/toplam_nokta_sayisi
print(f"Bulunan değer: {PI}, Geçen süre: {time.time()-baslangic_zamani}")


# print(x)
# print(f"{x:.4f}")