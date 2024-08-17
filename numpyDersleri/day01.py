import numpy as np
import time

scaler=np.array([90])
vector=np.array([1,2,3,4,5])
matrix=np.array([[1,2,3],[4,5,6], [7,8,9]])
print(scaler)

print(vector)
print(matrix)


# kuvvetlerini ne kadar sürede aldığını ve lişsteye eklediğini hesapladık
z1 = time.time() # zamanı başlat
l=[]
for a in range(1_000_000):
    kuvvet = a*100
    l.append(kuvvet)

z2 = time.time() # zamanı bitir
print(z2-z1)




# aynı işlemi np ile yapalım
l2=[]
z3 = time.time()
l2=np.arange(1_000_000)**100
z4=time.time()
print(z4-z3)