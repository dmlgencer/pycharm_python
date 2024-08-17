
print("Manava Hoşgeldiniz")

meyve = input("Lütfen istediğiniz meyveyi giriniz: ")

if(meyve=="elma"):
    kilo = int(input("Lütfen kaç kilo istediğiniiz giriniz: "))
    tutar = kilo*5
    print("Ödemeniz gereken tutar : " , tutar)

elif(meyve=="armut"):
    kilo = int(input("Lütfen kaç kilo istediğiniiz giriniz: "))
    tutar = kilo * 5
    print("Ödemeniz gereken tutar : ", tutar)

elif(meyve=="portakal"):
    kilo = int(input("Lütfen kaç kilo istediğiniiz giriniz: "))
    tutar = kilo * 5
    print("Ödemeniz gereken tutar : ", tutar)

else:
    print("Malesef Elimizde bu meyve yok. ")