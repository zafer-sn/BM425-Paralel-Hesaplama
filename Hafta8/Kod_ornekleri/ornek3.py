class Bitki:
    # boy = 0
    def __init__(self, boy):
        self.boy = boy
    @staticmethod
    def fotosentez(self):
        print("Fotosentez yapılıyor")

b1 = Bitki(10) # Bitki b1 = new Bitki();
b2 = Bitki(20)
print(b1.boy)
print(b2.boy)
b1.boy = 10
b2.boy = 20
print(b1.boy)
print(b2.boy)
b1 = b2
b2.boy = 50
print(b1.boy)
print(b2.boy)