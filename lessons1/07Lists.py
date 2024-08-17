'''
- Boş bir liste oluştur.
- Kullanıcıdan isim al.
- Bu isimleri listede tut
- Listedeki isimleri alfabetik sırala
- 




'''
import numpy as np


isimler = []

while True:
    isim = input("İsim Giriniz: ")
    if isim =='q' or isim=='Q' or len(isim)<=1:
        break
    isimler.append(isim)
    isimler.sort()

print(isimler)


