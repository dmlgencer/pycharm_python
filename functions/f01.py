# fonksiyon oluşturmanın iskeleti
'''

İskeleti:

def fonksionAdı():
    kodlar....
    ...
    ...
'''

print("Manava Hoşgeldiniz")
def muhasebe():
    kilo = int(input("Lütfen kaç kilo istediğiniiz giriniz: "))
    tutar = kilo * 5
    print("Ödemeniz gereken tutar : ", tutar, "TL")




meyve = input("Lütfen istediğiniz meyveyi giriniz: ")

if (meyve == "elma"):
    muhasebe()

elif (meyve == "armut"):
    muhasebe()

elif (meyve == "portakal"):
    muhasebe()

else:
    print("Malesef Elimizde bu meyve yok. ")
