isimler = ["Zafer", "Ahmet", "Mehmet", "Veli", "Sare"]

def a_bul(kelime):
    return "a" in kelime.lower()

f = list(filter(a_bul, isimler))
print(f)