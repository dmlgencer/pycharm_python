from oopConcept.Taşıt import Tasit


class Araba(Tasit):
    def __init__(self, marka, model, yil):
        super().__init__(marka, model)
        self.yil = yil

    def bilgileri_goster(self):
        return f"Araba: {self.marka} {self.model}, Yıl: {self.yil}"


# Nesne oluşturma
araba = Araba("Ford", "Mustang", 1967)

# Bilgileri gösterme
print(araba.bilgileri_goster())


