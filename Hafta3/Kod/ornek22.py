from abc import ABC, abstractmethod

class Arac(ABC):
    @abstractmethod
    def maksimum_hiz(self):
        pass

class Honda(Arac):
    def hesapla(self):
        return 5
    def maksimum_hiz(self):
        print("Maksimum hiza ulasildi")

h1 = Honda()
h1.maksimum_hiz()