"""

Question3: Kullanıcıdan üçgenin kenar uzunluklarını al.
           Üçgenin çevresini ve alanını ayrı ayrı hesaplayan 2 adet fonksiyon yaz.
"""


def alan(z, h):
    return (z * h) / 2


def cevre(x, y, z):
    return x + y + z


kenar1 = int(input("Üçgenin 1. kenar uzunluğunu giriniz: "))
kenar2 = int(input("Üçgenin 2. kenar uzunluğunu giriniz: "))
kenar3 = int(input("Üçgenin 3. kenar uzunluğunu giriniz: "))
yukseklik = int(input("Üçgenin yüksekliğini giriniz: "))

alan = alan(kenar3, yukseklik)
cevre = cevre(kenar1, kenar2, kenar3)

print("Üçgenin alanı: ", alan)

print("Üçgenin çevresi: ", cevre)
