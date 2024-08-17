'''
print() sadece bir bilgiyi ekrana bastırmak için kullanılır.
return fonksiyonlara özel bir ifadedir. Geriye değer döndürmesine yarıyor.
'''
def odaAlan(x,y):
    return (x+y)*2


kısaKenar = int(input("Lütfen birinci kısa kenari girin:"))
uzunKenar = int(input("Lütfen birinci uzun kenari girin:"))

kısaKenar2 = int(input("Lütfen ikinci kısa kenari girin:"))
uzunKenar2 = int(input("Lütfen ikinci uzun kenari girin:"))

oda1 = odaAlan(kısaKenar, uzunKenar)
oda2 = odaAlan(kısaKenar2, uzunKenar2)


print("Evinizin metrekaresi: " , oda1+ oda2)