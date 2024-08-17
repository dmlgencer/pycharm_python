
import numpy as np

matrix = np.ones((5,5))
matrix2 = np.full((5,5), 19)
matrix=matrix.astype("int")# biçimini değiştirdik
print(matrix, "\n")
print(matrix2, "\n")

print(matrix*4, "\n")

print(matrix2 + matrix, "\n")

print((matrix2 + matrix)//4)# bölme işlemi // tam sayı olarak getirir   / float olarak getirir.
