isim = "Zafer"
yas = 29
print("İsminiz:" + isim + "Yaşınız:" + str(yas))
print("İsminiz:", isim, "Yaşınız", yas)
print("İsminiz: {1}, Yaşınız: {0}".format(isim, yas))

print(f"İsminiz: {isim.startswith("Z")}, Yaşınız: {yas*2}")