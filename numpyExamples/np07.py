'''

1) Bir 3x4 lük ve elemanları 1-50 arasındaki sayılardan oluşan numpy matrisi oluşturun
2) Bu matrisin elemanlarından 20 den küçük olanların hangi sayılar olduğunu ve kaç adet olduğunu ekrana bastırın.
3) Bu matrisin elemanlarının toplamını ve ortalamasını ekrana bastırın
4) Bu matrisi tek boyutlu bir diziye dönüştürün



'''
from runpy import run_path

import numpy as np
counter = 0
sum = 0
avg = 0
m = np.random.randint(1, 51, (3,4))
print(m)
for r in m:
    for e in r:
        if e<20:
            print("20 den küçük değer: ", e)
            counter = counter +1
        sum += e
        avg = sum/12


print("20 den küçük sayı adedi: ",counter, "\n")
print("Sayıların toplamı: ", sum, "\n")
print("Sayıların ortlaması: ", avg, "\n")
print(m.reshape(12))

m.reshape(3,4)
print(m)
