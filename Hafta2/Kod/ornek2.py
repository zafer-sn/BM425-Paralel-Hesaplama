meyveler = ["elma", "armut", "ayva"]
kaloriler = [100, 200, 250]
print(f"{meyveler[0]} nın kalorisi: {kaloriler[0]}")

# key-value, anahtar-deger
sozluk1 = {"cilek":50, "portakal":100}
print(sozluk1["cilek"])

sozluk2 = {11: True, 3.14:"deneme"}
print(sozluk2[11])

sozluk3 = {"plakalar":[11, 34, 1], "ornekler": {"1": 3}}

sozluk4 = {"mandalin":300, "karpuz":1000}
print(sozluk4.items())
print(sozluk4.keys())
print(sozluk4.values())