class Araba():
    def calistir(self):
        print("Araba calisiyor...")

class Ucak():
    def calistir(self):
        print("Ucak calisiyor...")
u1 = Ucak()
a1 = Araba()

def calis(a):
    a.calistir()

calis(u1)
calis(a1)