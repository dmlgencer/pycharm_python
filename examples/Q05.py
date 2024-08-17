'''
4-) Rastgele 600 adet 0 ile 1000 arasında sayı oluşturup bir liste içerisine aktaran ve 100’den
küçük olan sayıların adedini ekrana yazdıran python kodlarını yazınız?
'''
import random

liste = []
counter = 0
for i in range(15):
    k = random.randint(0, 1001)
    liste.append(k)

    if k<100:
        counter+=1

print(liste)
print("100 den küçük olanların adedi: ", counter)