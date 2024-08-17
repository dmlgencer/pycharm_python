import numpy as np

matrix= np.array([[1,2,3,4], [5,6,7,8], [9,4,3,2], [5,4,1,2,]])
print(matrix[0] ,"\n")

print(matrix)
print(matrix[1:3])# 1. ve 2. satırlar gekecek 3. satur dahil değil
print(matrix[0:4,0:1])# ilk sütundaki elemanları aldık

print(matrix[0:4, 1:3])

print(matrix[1:3, 1:3])