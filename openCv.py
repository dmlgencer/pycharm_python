'''

GENEL TEKRAR NUMPY
NUMPY kütüphanesi tekli veya çoklu diziler üstünde kolay işlemler yapabilmemiz için var. bir python kütüphanesidir.
içerisinde farklı metodlar barındırır ve bunlar sayesinde tek boyutlu ya da iki veya çok boyutlu matrisler için diziler için
matematiksel işlemler yapma olanağı tanır.


'''

import numpy as np
#we can create an array with using numpy library.
a = np.array([2,5,7])
print(a)

#we can create to matrix 3x4
m = np.array([[2,7,8, 9], [1,3,1,2], [9,7,5,1]])
print(m, "\n")
#we can change to matrix shape


# copy & view
# copt metot kullanılındığında yapılan değişiklik sadece kopyalanan matrisi etkiler. esas matriste bir değişiklik olmaz.
e = m.copy()
m[1,2]=8
print(e, "\n")
print(m, "\n")

# view metot kullandığımızda bir değişiklik yaptığımızda bundan esas olan veri de sonraki veri de etkilenir.
r = m.view()
m[1,3] = 0
print(m,"\n")
print(r)

# zeros & ones & full
# zeros: sıfırlardan oluşan yapı getirir.
arr = np.zeros(3) # tek noyutlu bir dizi
brr = np.zeros((3,2)) # iki boyutlu dizi
crr = np.zeros((3,3,3)) # üç boyutlu dizi
print(arr, "\n")
print(brr, "\n")
print(crr, "\n")

# ones: birlerden oluşan yapı getirir. kullanımı zeros ile aynı
# full: sen sayı seçersin ve o sayıdan oluşan yapı getirir. içinde sadece o sayı olur.

drr = np.full((3,3), 5)# üçe üçlük 5 lerden oluşan bir matris.
print(drr)






