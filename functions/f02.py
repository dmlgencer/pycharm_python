

print("Manava Hoşgeldiniz")
def muhasebe(meyve_ismi):
    kilo = int(input("Lütfen kaç kilo istediğiniiz giriniz: "))
    tutar = kilo * 5
    print(kilo, " kilo", meyve_ismi, "için ödemeniz gereken tutar : ", tutar, "TL")



meyve = input("Lütfen istediğiniz meyveyi giriniz: ")

if (meyve == "elma"):
    muhasebe(meyve)

elif (meyve == "armut"):
    muhasebe(meyve)

elif (meyve == "portakal"):
    muhasebe(meyve)

else:
    print("Malesef Elimizde bu meyve yok. ")
