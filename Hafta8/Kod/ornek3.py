import random
# Meta-heuristic algoritmalar-sezgisel algoritmalar
# PSO, Genetik Algoritma, Bat algortihm
hedef_konum = 50_000
mevcut_konum = random.randint(0, 1_000_000)
print(f"Mevcut konum:{mevcut_konum}")
for epoch in range(2500):   

    hata = abs(hedef_konum-mevcut_konum) # rmse, mse, mae

    if hata <= 10:
        print(f"Tebrikler, dogru konumdasiniz!")

    adim_buyuklugu = random.randint(-5_000, 5_000)
    yeni_konum = mevcut_konum + adim_buyuklugu

    yeni_hata = abs(hedef_konum-yeni_konum)
    if yeni_hata < hata:
        mevcut_konum = yeni_konum
        durum = "Dogru yoldasin, sonuca yaklasiyor..."
    else:
        durum = "Yanlis yoldasin, sonuctan uzaklasiyor..."

    print(f"Tur: {i}, Mevcut Konum: {mevcut_konum}, Durum: {durum}, Uzaklik: {abs(hedef_konum-mevcut_konum)}")