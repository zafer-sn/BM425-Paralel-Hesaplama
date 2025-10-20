meyveler = ["elma", "armut", "ayva", "cilek"]
kaloriler = [100, 150, 250, 350]
renkler = ["kirmizi", "turuncu", "sari"]
z = list(zip(meyveler, kaloriler, renkler, strict=True))
print(z)

for (e, k, r) in z:
    print(k)